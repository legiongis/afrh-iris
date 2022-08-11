import json
from pathlib import Path

from django.core.management.base import BaseCommand

from arches.app.models.models import Concept

class Command(BaseCommand):
    """
    inspect graph json
    """

    verbosity = 1

    def add_arguments(self, parser):

        parser.add_argument(
            "type",
            choices=["graph", "resource"],
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

    def handle(self, *args, **options):

        self.verbosity = options['verbosity']

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

    def inspect_resource_file(self, json_path):
        data = None
        with open(json_path, "r") as o:
            data = json.load(o)

        try:
            resource_list = data["business_data"]["resources"]
        except KeyError:
            print("file structure error")
            exit()

        print(f"{json_path.name} - {len(resource_list)}")
        tiles_cts = []
        for resource in resource_list:
            tiles_ct = self.inspect_resource(resource)
            tiles_cts.append(tiles_ct)
        print(tiles_cts)

    def inspect_resource(self, resource):
        return(len(resource['tiles']))

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
