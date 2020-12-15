from typing import List

def lattice_from_json(json: list):
    info = json[0]
    bottoms = info["Bottom"]
    top = info["Top"]
    
    def parse_nodes(node_raw):
        return node_raw["Nodes"]
    nodes = parse_nodes(json[1])

    # S = source, D = destination object list
    arcs = json[2]["Arcs"]

class Lattice:
    pass