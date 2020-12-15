import json
from typing import List

class Context:
    def __init__(self, obj_names: List[str], attr_names: List[str], connections: List[List[int]]):
        self.obj_names = obj_names
        self.attr_names = attr_names
        self.connections = connections
    
    def to_raw(self):
        def single_connection_mapper(connection: List[int]):
            return {
                "Count": len(connection),
                "Inds": connection
            }

        data = list(map(single_connection_mapper, self.connections))
        return [
            {
                "ObjNames": self.obj_names,
                "Params": { "AttrNames": self.attr_names }
            },
            {
                "Count": len(self.connections),
                "Data": data
            }
        ]

    def to_file(self, filename: str = 'mycontext.json'):
        with open(filename, "w") as outfile:  
            json.dump(self.to_raw(), outfile, indent = 4)
