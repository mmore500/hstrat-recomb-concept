import typing

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout


def draw_pedigree(
    graph: nx.DiGraph,
    extant_nodes: typing.List,
    pos: typing.Dict = None,
) -> None:
    """
    Draw the input graph.

    Args:
        graph: The input graph to draw.
        extant_nodes: List of extant nodes.
        pos: Position of nodes for layout. If None, use the graphviz_layout.
    """
    if pos is None:
        pos = graphviz_layout(graph, prog="dot")

    nx.draw(graph, pos, with_labels=True, arrows=True, node_color="lightblue")

    labels = {node: str(node) for node in extant_nodes}
    nx.draw_networkx_labels(graph, pos, labels=labels)

    print("Pedigree laid out")

    plt.show()
