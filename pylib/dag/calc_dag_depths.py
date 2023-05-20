import typing

import networkx as nx


def calc_dag_depths(graph: nx.DiGraph) -> typing.Dict[typing.Any, int]:
    depths: typing.Dict[
        typing.Any, int
    ] = {}  # Dictionary to store node depths
    nodes = list(nx.topological_sort(graph))  # Perform topological sorting

    for node in nodes:
        predecessors = [*graph.predecessors(node)]
        if len(predecessors) == 0:
            # If node has no predecessors, set depth to 0
            depths[node] = 0
        else:
            # Assign depth based on the maximum depth of predecessors
            max_depth = max(
                depths[predecessor] for predecessor in predecessors
            )
            depths[node] = max_depth + 1

    return depths
