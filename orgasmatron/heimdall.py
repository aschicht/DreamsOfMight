import collections

GatewayData = collections.namedtuple('GatewayData', ['controller_id', 'map_id', 'entry_point_position'])

class Heimdall:
    _bifrost = {}

    @staticmethod
    def add_gateway(entry_id, controller_id, map_id, entry_point_position):
        if not Heimdall._bifrost.get(entry_id):
            Heimdall._bifrost[entry_id] = GatewayData(controller_id, map_id, entry_point_position)

    @staticmethod
    def remove_gateway(entry_id):
        Heimdall._bifrost.pop(entry_id)

    @staticmethod
    def update_gateway(entry_id, controller_id, map_id, entry_point_position):
        if Heimdall._bifrost.get(entry_id):
            Heimdall._bifrost[entry_id] = GatewayData(controller_id, map_id, entry_point_position)

    @staticmethod
    def get_gateway(entry_id):
        return Heimdall._bifrost.get(entry_id)