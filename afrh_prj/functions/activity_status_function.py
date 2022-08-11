import uuid
import json
from django.core.exceptions import ObjectDoesNotExist
from arches.app.functions.base import BaseFunction
from arches.app.models import models
from arches.app.models.tile import Tile
from arches.app.datatypes.datatypes import DataTypeFactory


details = {
    'name': 'Activity Status',
    'type': 'node',
    'description': 'Triggers change in status node of management activity instance',
    'defaultconfig': {"triggering_nodegroups": []},
    'classname': 'ActivityStatusFunction',
    'component': '',
    'functionid':'96efa95a-1e2c-4562-ac1f-b415796f9f75'
}

class ActivityStatusFunction(BaseFunction): 

    def save(self, tile, request):
        activity_status_nodegroupid = "83f05a05-3c8c-11ea-b9b7-027f24e6fd6b"
        default_status_concept_value = "" # ?
        activity_status_boolean_nodeid = "13a519f2-2dbc-11eb-a471-784f435179ea"

        try:

            status_tile = Tile.objects.get(nodegroup_id=activity_status_nodegroupid, resourceinstance=tile.resourceinstance)
            # active = status_tile.data[activity_status_nodegroupid] == default_status_concept_value
            try:
                active = status_tile.data[activity_status_boolean_nodeid] # placeholder; must identify concept values in status node considered "active" -- see comment above
            except KeyError: # data loaded with older version of graph (before boolean node added)
                status_tile.data[activity_status_boolean_nodeid] = True
                active = True
            if active and not status_tile.data[activity_status_boolean_nodeid]:
                status_tile.data[activity_status_boolean_nodeid] = True
                status_tile.save()
            elif not active and status_tile.data[activity_status_boolean_nodeid]:
                status_tile.data[activity_status_boolean_nodeid] = False
                status_tile.save()

        except ObjectDoesNotExist:
            pass

        return

    
    def delete(self,tile,request):
        raise NotImplementedError

    
    def on_import(self,tile):
        raise NotImplementedError

    
    def after_function_save(self,tile,request):
        raise NotImplementedError
    
    
    def get(self):
        raise NotImplementedError
