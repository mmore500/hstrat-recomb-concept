import typing

import networkx as nx


def prune_dag(graph: nx.DiGraph, extant_nodes: typing.List) -> nx.DiGraph:

    graph = graph.reverse()  # Make the graph bottom-up

    descendants = {*extant_nodes}
    for node in extant_nodes:
        descendants.update(nx.descendants(graph, node))

    # Keep only ancestors of extant_nodes
    graph = graph.subgraph(descendants)

    graph = graph.reverse()  # Make the graph top-down

    return graph
