import json
import uuid
from pathlib import Path
from rdflib import Graph
from django.core.management.base import BaseCommand

from arches.app.models.models import Concept, NodeGroup, Value, Node
from arches.app.models.tile import Tile
from arches.app.utils.betterJSONSerializer import JSONSerializer, JSONDeserializer

class Command(BaseCommand):
    """
    inspect graph json
    """

    verbosity = 1

    def add_arguments(self, parser):

        parser.add_argument(
            "type",
            choices=["graph", "resource", "collections", "fix-resources"],
            help="type of validation to run"
        )
        parser.add_argument(
            "--file",
            help="individual JSON file to inspect"
        )
        parser.add_argument(
            "--dir",
            help="directory of JSON files to inspect"
        )
        parser.add_argument(
            "--resid",
            help="single resourceintance id to process"
        )

    def handle(self, *args, **options):

        self.verbosity = options['verbosity']
        self._make_lookup()

        paths = []
        if options['file']:
            paths += [Path(options['file'])]

        if options['dir']:
            paths += Path(options['dir']).glob("*.json")

        for path in paths:
            if options['type'] == "graph":
                self.inspect_graph_file(path)
            elif options['type'] == 'resource':
                self.inspect_resource_file(path)
            elif options['type'] == 'collections':
                self.inspect_collections_file(path)
            elif options['type'] == 'fix-resources':
                self.fix_resources(path, resid=options['resid'])

    def _read_json_file(self, file_path):
        with open(file_path, "r") as o:
            return json.load(o)

    def _make_lookup(self):

        self.lookup = {
            "Criterion A": str(Node.objects.get(name="Criterion A Score").pk),
            "Criterion B": str(Node.objects.get(name="Criterion B Score").pk),
            "Criterion C": str(Node.objects.get(name="Criterion C Score").pk),
            "Criterion D": str(Node.objects.get(name="Criterion D Score").pk),
            "Integrity": str(Node.objects.get(name="Integrity Score").pk),
            "National Significance": str(Node.objects.get(name="National Significance Score").pk),
            "Total": str(Node.objects.get(name="Total Quantitative Score").pk),
        }

        self.reassigned_location_nodes = {
            "da46289a-60f1-11eb-b848-3af9d3749918": "Archaeological Zones",
            "f5d5fca2-60f1-11eb-b848-3af9d3749918": "Master Plan Zones",
            "09b8a7a6-60f2-11eb-b848-3af9d3749918": "Character Areas",
        }

    def inspect_resource_file(self, json_path):
        data = self._read_json_file(json_path)

        try:
            resource_list = data["business_data"]["resources"]
        except KeyError:
            print("file structure error")
            exit()

        print(f"{json_path.name} - {len(resource_list)}")
        resource_info = []
        for resource in resource_list:
            data = self.inspect_resource(resource)
            resource_info.append(data)
        missing_nodegroups = set()
        missing_nodes = set()
        for info in resource_info:
            missing_nodegroups.update(info['missing_nodegroups'])
            missing_nodes.update(info['missing_nodes'])
        
        print(f"invalid nodegroups: {len(missing_nodegroups)}")
        for mng in missing_nodegroups:
            print(mng)
        print(f"invalid nodes (excluding those within invalid nodegroups): {len(missing_nodes)}")
        for mn in missing_nodes:
            print(mn)

    def inspect_resource(self, resource):
        resid = resource['resourceinstance']['resourceinstanceid']
        tile_ct = len(resource['tiles'])
        missing_nodegroups = set()
        missing_nodes = set()
        for t in resource['tiles']:
            try:
                NodeGroup.objects.get(pk=t['nodegroup_id'])
                for nodeid in t['data'].keys():
                    try:
                        Node.objects.get(pk=nodeid)
                    except Node.DoesNotExist:
                        missing_nodes.add(nodeid)
            except NodeGroup.DoesNotExist:
                missing_nodegroups.add(t['nodegroup_id'])

        return {
            "resourceid": resid,
            "tile_ct": tile_ct,
            "missing_nodegroups": list(missing_nodegroups),
            "missing_nodes": list(missing_nodes),
        }

    def fix_resources(self, file_path, resid=None):
        data = self._read_json_file(file_path)

        resources = data['business_data'].pop('resources')
        new_resources = []
        for r in resources:
            if resid and r['resourceinstance']['resourceinstanceid'] != resid:
                continue
            new_resource = self.fix_resource(r)
            new_resources.append(new_resource)

        data['business_data']['resources'] = new_resources
        export = JSONDeserializer().deserialize(JSONSerializer().serialize(JSONSerializer().serializeToPython(data)))
        if resid:
            outfile = str(file_path).replace(".json", f"-{resid}.json")
        else:
            outfile = str(file_path).replace(".json", "-fixed.json")
        with open(outfile, "w") as out:
            json.dump(export, out, indent=2)
        print("complete")

    def fix_resource(self, resource):
        """ takes in the original resource instance, and returns the same resource
        with adjusted tiles as necessary. 
        Currently, only implemented for the Inventory Resource resource model instance, 
        which need a lot of changes to fit the altered Inventory Resource model.


        """

        def get_new_important_date_tile(resid):
            ## the nodeid used here is the id of the Date E52 node. The tile returned is for
            ## the Important Dates node and it has tiles[0] which a Date E32 node with the proper
            ## data keys
            new_tile = Tile().get_blank_tile("d7c28dca-6473-11ed-adda-09c2399aacac", resourceid=resid)
            new_tile.tileid = str(uuid.uuid4())
            return new_tile

        resid = resource['resourceinstance']['resourceinstanceid']
        print(f"\n~~~ FIXING RESOURCE: {resid} ~~~")

        tiles = resource.pop('tiles')
        new_tiles = []
        new_score_tile_data = {}
        reassigned_location_values = {}
        new_important_date_parent = None
        original_eval_tile = None
        phase_type_cult_period = None
        
        eval_ct = 0

        # the labels here give extra context and are used below in if/elif. but
        # they are not actually present in Arches or the database
        ng_to_correct = {
            "db6bbf76-3d77-11ea-b9b7-027f24e6fd6b": "Quant Score Total (InvRes)",
            "4d452e84-3d78-11ea-b9b7-027f24e6fd6b": "Quant Score Value (InvRes)",
            "9058b28b-3bc1-11ea-b9b7-027f24e6fd6b": "Phase Type (InvRes)",
            "e22938bc-3d76-11ea-b9b7-027f24e6fd6b": "Relative Level of Significance (InvRes)",
            "ed94aeed-3bc4-11ea-b9b7-027f24e6fd6b": "Important Date (InvRes)",
            "62c71694-3d75-11ea-b9b7-027f24e6fd6b": "Evaluation (InvRes)",
            "802f79cd-3bc4-11ea-b9b7-027f24e6fd6b": "Image (InvRes)",
            "87fad7b9-46c4-11ea-b9b7-027f24e6fd6b": "Location (InvRes)"
        }

        # iterate all tiles and handle each one individually, in many cases
        # this loop is only applicable to the Inventory Resource instances
        for tile in tiles:

            # for v in tile.data.values():
            #     if "3700 North Capitol Street NW" in v:
            # print(json.dumps(tile, indent=4))

            ng_label = ng_to_correct.get(tile['nodegroup_id'])
            if ng_label:

                # print(f"Processing NodeGroup: {ng_label} ({tile['nodegroup_id']})\n")
                # print("-- current data --")
                # for k, v in tile['data'].items():
                #     try:
                #         node_name = Node.objects.get(nodeid=k).name
                #     except Node.DoesNotExist:
                #         node_name = f"(no match for {k})"
                #     print(f"Node Name: {node_name}")
                #     print(f"Node Value: {v}")

                # these two are for the quantitative score
                if ng_label == "Quant Score Total (InvRes)":
                    # this is the quant score total and it will be recalculated at the end
                    # skip it here so it is not added to new_tiles
                    pass
                elif ng_label == "Quant Score Value (InvRes)":
                    cval = Value.objects.get(pk=tile['data']['054bb518-63dd-11ea-a3d5-acde48001122'])
                    score = tile['data']['8869662e-3d78-11ea-b9b7-027f24e6fd6b']
                    new_score_tile_data[cval.value] = score

                # this is the Phase Type Cultural Preiod(s) originally,
                # and I don't know where it's supposed to go now, so remove it that particular node
                elif ng_label == "Phase Type (InvRes)":
                    # print(json.dumps(tile, indent=5))
                    # collect this node value now, but it should be removed from this tile
                    phase_type_cult_period = tile['data'].pop("9058b28e-3bc1-11ea-b9b7-027f24e6fd6b", None)
                    new_tiles.append(tile)

                elif ng_label == "Relative Level of Significance (InvRes)":
                    # this data is used later in the new AFRH-W designation tile that gets created
                    pass

                elif ng_label == "Location (InvRes)":
                    # this is reacquired later and processed at that time, skip for now.
                    pass

                elif ng_label == "Important Date (InvRes)":

                    # the first time an important date is encountered, create the parent
                    # tile with one date tile in its tiles attribute
                    if new_important_date_parent is None:
                        new_important_date_parent = get_new_important_date_tile(resid)
                        # print(new_important_date_parent.serialize())
                        # print(new_important_date_parent.tiles[0].serialize())

                        # add this parent tile to the output JSON list
                        new_tiles.append({
                            "data": {},
                            "nodegroup_id": str(new_important_date_parent.nodegroup_id),
                            "parenttile_id": None,
                            "provisionaledits": None,
                            "resourceinstance_id": resid,
                            "sortorder": 0,
                            "tileid": str(new_important_date_parent.tileid)
                        })

                    end_date = tile['data']["ed94aef1-3bc4-11ea-b9b7-027f24e6fd6b"]
                    date_type = tile['data']["ed94aef2-3bc4-11ea-b9b7-027f24e6fd6b"]
                    date_note = tile['data']["ed94aef3-3bc4-11ea-b9b7-027f24e6fd6b"]
                    begin_date = tile['data']["ed94aef4-3bc4-11ea-b9b7-027f24e6fd6b"]

                    new_date = None
                    if end_date:
                        new_date = end_date
                    elif begin_date:
                        new_date = begin_date

                    try:
                        # in some cases, the uuid for the date qualifier was placed in the date note field (wtf)
                        # convert this to a string here.
                        date_note = Value.objects.get(pk=date_note).value
                    except:
                        pass

                    # use the qualifier value to set a new EDTF value where needed
                    if new_date and date_note == "ca.":
                        new_date = f"~{new_date[:4]}"
                    elif new_date and date_note == "pre":
                        new_date = f"1700/{new_date[:4]}"

                    placeholder_notes = [
                        " (note that month and day are placeholders)",
                        " (note that month and day of revised construction date are placeholders)",
                        " (date and month are placeholders)",
                        " (note that month and day are placeholders)",
                        " (Note that month and day are placeholders)",
                        " (note that the month and day are placeholders)",
                        "  (note that the month and day are placeholders)",
                        " (note that day and month are placeholders)",
                    ]
                    for pn in placeholder_notes:
                        if pn in date_note:
                            if new_date:
                                new_date = new_date[:4]
                            date_note = date_note.replace(pn, "")

                    if date_type:
                        date_type = date_type[0]

                    new_date_tile = {
                        "data": {},
                        # get the nodegroup from the auto generated tile inside the parent date tile
                        "nodegroup_id": str(new_important_date_parent.tiles[0].nodegroup_id),
                        "parenttile_id": str(new_important_date_parent.tileid),
                        "provisionaledits": None,
                        "resourceinstance_id": resid,
                        "sortorder": 0,
                        "tileid": str(uuid.uuid4()),
                    }

                    new_date_tile['data']['d7c28dca-6473-11ed-adda-09c2399aacac'] = new_date
                    new_date_tile['data']['07ebffb8-6474-11ed-adda-09c2399aacac'] = date_type
                    new_date_tile['data']['552d0452-6474-11ed-adda-09c2399aacac'] = date_note

                    new_tiles.append(new_date_tile)

                elif ng_label == "Image (InvRes)":
                    print("SKIPPING IMAGE BUT IT NEEDS TO BE HANDLED STILL")
                    # print(tile)
                elif ng_label == "Evaluation (InvRes)":
                    original_eval_tile = tile
                    eval_ct +=1
            else:
                # print("  -- (no change to make on first pass) --")
                new_tiles.append(tile)

        print("\n-- FIRST PASS COMPLETE --")

        print("\nhandle evaluation tile(s)")
        if original_eval_tile:
            print(f"original parent tileid: {original_eval_tile['tileid']}")
            original_eval_tile_children = []

            # collect the children of the original evaluation tile.
            for tile in tiles:
                if tile['parenttile_id'] == original_eval_tile['tileid']:
                    original_eval_tile_children.append(tile)

            # confirm that if there are no children, then the original eval doesn't have data either
            if not original_eval_tile_children:
                assert not any(original_eval_tile['data'].values()), \
                    "there are no children tiles but the original eval parent does contain data"
            # confirm there was only one original eval tile
            assert eval_ct <= 1, \
                "there was more than one eval tile"

            if len(original_eval_tile_children) > 0:
                # first create the new parent tile for this evaluation
                new_top_eval_tile = Tile().get_blank_tile("62c71694-3d75-11ea-b9b7-027f24e6fd6b", resourceid=resid)
                new_tiles.append(new_top_eval_tile.serialize())

                # collect some nodes that were on the original eval tile data, but will
                # be reassigned to other new tiles
                reassigned_eval_nodes = {
                    "640fdf62-3d76-11ea-b9b7-027f24e6fd6b": "Evaluation Area of Significance",
                    "37a8ce52-3d76-11ea-b9b7-027f24e6fd6b": "Evaluation Period of Significance",
                    "912ba828-3d76-11ea-b9b7-027f24e6fd6b": "HPMP"
                }
                reassigned_eval_values = {}
                for nodeid, value in original_eval_tile['data'].items():
                    if nodeid in reassigned_eval_nodes:
                        reassigned_eval_values[reassigned_eval_nodes[nodeid]] = value
                    elif nodeid == "62c71694-3d75-11ea-b9b7-027f24e6fd6b":
                        # this is an empty value for the top tile (oops)
                        pass
                    else:
                        raise Exception(f"unhandled nodeid {nodeid}")

                # assign hpmp directly to parent
                if reassigned_eval_values.get("HPMP"):
                    new_hpmp = Tile().get_blank_tile_from_nodegroup_id(
                        "912ba828-3d76-11ea-b9b7-027f24e6fd6b",
                        resourceid=resid, parenttile=new_top_eval_tile
                    )
                    new_hpmp.data["912ba828-3d76-11ea-b9b7-027f24e6fd6b"] = reassigned_eval_values.get("HPMP")
                    new_tiles.append(new_hpmp.serialize())
                else:
                    print("no HPMP in source data")
                
                # now begin remake the afrh desig from the children as necessary.
                new_afrh_desig = Tile().get_blank_tile_from_nodegroup_id(
                    "cb4e5c66-6475-11ed-adda-09c2399aacac",
                    resourceid=resid,
                    parenttile=new_top_eval_tile
                )
                # print(f"{len(original_eval_tile_children)} original eval children")
                for oec in original_eval_tile_children:

                    # this is the total score, and should be skipped because it is recalculated in
                    # the main afrh-w desig below
                    if oec['nodegroup_id'] == "db6bbf76-3d77-11ea-b9b7-027f24e6fd6b":
                        pass

                    # this this the main AFRH-W desig
                    elif oec['nodegroup_id'] == "e22938bc-3d76-11ea-b9b7-027f24e6fd6b":

                        # rel sig and rel sig date
                        new_afrh_desig.data["80eff6e2-6502-11ed-adda-09c2399aacac"] = oec['data'].pop("e22938bc-3d76-11ea-b9b7-027f24e6fd6b", None)
                        new_afrh_desig.data["1aea1ae2-80b0-11ee-b3e3-45401c237637"] = oec['data'].pop("000b7804-3d77-11ea-b9b7-027f24e6fd6b", None)
                        

                        new_afrh_desig.data["66995e60-6501-11ed-adda-09c2399aacac"] = reassigned_eval_values.get("Evaluation Area of Significance")
                        new_afrh_desig.data["422d1008-6501-11ed-adda-09c2399aacac"] = reassigned_eval_values.get("Evaluation Period of Significance")

                        # this are the score values
                        new_afrh_desig.data["d570b02e-64ff-11ed-adda-09c2399aacac"] = new_score_tile_data["Criterion A"]
                        new_afrh_desig.data["eb02262a-64ff-11ed-adda-09c2399aacac"] = new_score_tile_data["Criterion B"]
                        new_afrh_desig.data["fed01d38-64ff-11ed-adda-09c2399aacac"] = new_score_tile_data["Criterion C"]
                        new_afrh_desig.data["5cecfa08-6500-11ed-adda-09c2399aacac"] = new_score_tile_data["Criterion D"]
                        new_afrh_desig.data["fa44b02e-6501-11ed-adda-09c2399aacac"] = new_score_tile_data["Integrity"]
                        new_afrh_desig.data["0a84f232-6502-11ed-adda-09c2399aacac"] = new_score_tile_data["National Significance"]
                        
                        # recalculate the total score
                        new_afrh_desig.data["81c3dfd6-6500-11ed-adda-09c2399aacac"] = sum(new_score_tile_data.values())

                    # this is the overall AFRH W status, must go within the newly created tile
                    elif oec['nodegroup_id'] == "20b57492-3d77-11ea-b9b7-027f24e6fd6b":

                        # status and status date
                        new_afrh_desig.data["bcf5e1bc-6500-11ed-adda-09c2399aacac"] = oec['data'].pop("38f517e2-3d77-11ea-b9b7-027f24e6fd6b", None)
                        new_afrh_desig.data["f6c887b4-6500-11ed-adda-09c2399aacac"] = oec['data'].pop("498467a2-3d77-11ea-b9b7-027f24e6fd6b", None)

                    else:
                        print("UH-OH!")
                        raise Exception("UH-OH! unexpected child of original evaluation tile")

                new_tiles.append(new_afrh_desig.serialize())


        # process location content
        og_loc_tile = None
        for t in tiles:
            if t['nodegroup_id'] == "87fad7b9-46c4-11ea-b9b7-027f24e6fd6b":
                og_loc_tile = t

        if og_loc_tile:
            new_location_parent_tile = Tile().get_blank_tile_from_nodegroup_id(
                "87fad7b9-46c4-11ea-b9b7-027f24e6fd6b",
                resourceid=resid,
            )
            new_tiles.append(new_location_parent_tile.serialize())
            # print(json.dumps(new_location_parent_tile.data, indent=2))

            geom = og_loc_tile['data'].pop("87fad7bc-46c4-11ea-b9b7-027f24e6fd6b", None)
            addr = og_loc_tile['data'].pop("b806806a-46c4-11ea-b9b7-027f24e6fd6b", None)
            addr_type = og_loc_tile['data'].pop("c637b7b2-46c4-11ea-b9b7-027f24e6fd6b", None)
            loc_note = og_loc_tile['data'].pop("87fad7bd-46c4-11ea-b9b7-027f24e6fd6b", None)
            arch_zone = og_loc_tile['data'].pop("da46289a-60f1-11eb-b848-3af9d3749918", None)
            char_area = og_loc_tile['data'].pop("09b8a7a6-60f2-11eb-b848-3af9d3749918", None)
            mp_zone = og_loc_tile['data'].pop("f5d5fca2-60f1-11eb-b848-3af9d3749918", None)

            if geom:
                new_geom_tile = Tile().get_blank_tile_from_nodegroup_id(
                    "87fad7bc-46c4-11ea-b9b7-027f24e6fd6b",
                    resourceid=resid,
                    parenttile=new_location_parent_tile
                )
                new_geom_tile.data["87fad7bc-46c4-11ea-b9b7-027f24e6fd6b"] = geom
                new_tiles.append(new_geom_tile.serialize())

            if addr:
                new_addr_tile = Tile().get_blank_tile_from_nodegroup_id(
                    "906e40a6-46c4-11ea-b9b7-027f24e6fd6b",
                    resourceid=resid,
                    parenttile=new_location_parent_tile
                )
                new_addr_tile.data["b806806a-46c4-11ea-b9b7-027f24e6fd6b"] = addr
                new_addr_tile.data["c637b7b2-46c4-11ea-b9b7-027f24e6fd6b"] = addr_type
                new_tiles.append(new_addr_tile.serialize())

            if loc_note:
                new_loc_note_tile = Tile().get_blank_tile_from_nodegroup_id(
                    "87fad7bd-46c4-11ea-b9b7-027f24e6fd6b",
                    resourceid=resid,
                    parenttile=new_location_parent_tile
                )
                new_loc_note_tile.data["87fad7bd-46c4-11ea-b9b7-027f24e6fd6b"] = loc_note
                new_tiles.append(new_loc_note_tile.serialize())

            if any([arch_zone, char_area, mp_zone]):
                new_areas_tile = Tile().get_blank_tile_from_nodegroup_id(
                    "48aa02fc-6523-11ed-adda-09c2399aacac",
                    resourceid=resid,
                    parenttile=new_location_parent_tile
                )
                new_areas_tile.data["4eb220c0-6524-11ed-adda-09c2399aacac"] = arch_zone
                new_areas_tile.data["c7ff7f28-6523-11ed-adda-09c2399aacac"] = char_area
                new_areas_tile.data["35040328-6524-11ed-adda-09c2399aacac"] = mp_zone
                new_tiles.append(new_areas_tile.serialize())


            # after popping all these values, there are still two keys left but they
            # are empty in every resource, so they will be ignored

            if any(og_loc_tile['data'].values()):
                print(json.dumps(og_loc_tile['data'], indent=2))
                raise Exception("")

        # print("process reassigned location nodes")
        for t in new_tiles:
            for nodeid, value in t['data'].items():
                if nodeid in self.reassigned_location_nodes:
                    reassigned_location_values[self.reassigned_location_nodes[nodeid]] = value

        # print("remove reassigned eval and location nodes (should this really happen???)")
        reassigned_nodeids = list(self.reassigned_location_nodes)
        for t in new_tiles:
            for rn in reassigned_nodeids:
                if rn in t['data']:
                    del t['data'][rn]

        print(f"og tiles: {len(tiles)}, new tiles: {len(new_tiles)}")

        resource['tiles'] = new_tiles

        # print("\n VALIDATE new resource content...")
        validated = self.inspect_resource(resource)
        # print(json.dumps(validated), indent=2)
        return resource

    def inspect_graph_file(self, json_path):

        data = None
        with open(json_path, "r") as o:
            data = json.load(o)

        graph_list = data.get("graph")
        if graph_list is None:
            print("no graphs in file")
            exit()

        for graph in graph_list:
            self.inspect_graph(graph)

    def inspect_graph(self, graph):

        print("-"*80)
        print(f"GRAPH NAME: {graph['name']}")

        c_nodes = [i for i in graph['nodes'] if i['datatype'] == "concept"]
        cl_nodes = [i for i in graph['nodes'] if i['datatype'] == "concept-list"]

        cc_nodes = c_nodes + cl_nodes
        cc_nodes.sort(key=lambda item: item.get("name"))
        errors = []
        for n in cc_nodes:
            if self.verbosity > 1:
                print(f"{n['name']} ({n['datatype']})")
            config = self.get_node_config(n)
            if config is None:
                continue

            collection, status = self.check_collection(config)
            if status != "valid":
                errors.append((n['name'], status, collection))

        if self.verbosity > 0:
            print(f"-- {len(errors)} COLLECTION ERRORS --")
            for i in errors:
                print(i)

    def get_node_config(self, node):

        config = node.get('config')
        if config is None:
            if self.verbosity > 1:
                print("  ERROR: null config on node")
        return config

    def check_collection(self, config):
        collection = config.get('rdmCollection')
        status = "valid"
        if collection is None:
            if self.verbosity > 1:
                print("  ERROR: no collection set")
            status = "null"
        else:
            c = Concept.objects.filter(pk=collection)
            if not c.exists():
                status = "invalid"
                if self.verbosity > 1:
                    print(f"  ERROR: {collection} is not a valid collection.")
        return (collection, status)

    def inspect_collections_file(self, file_path):

        g = Graph()
        g.parse(str(file_path))

        # first thing is checking whether every collection has a prefLabel
        collection_labels = {}
        for s, o, p in g:
            if "#Collection" in str(p):
                collection_labels[s] = None
        # print(collection_labels)
        for s, o, p in g:
            if "#prefLabel" in str(o):
                collection_labels[s] = p
        for k, v in collection_labels.items():
            if v is None:
                print(k)