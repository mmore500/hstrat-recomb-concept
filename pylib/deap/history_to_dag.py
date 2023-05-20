import typing

from deap.tools.support import History as deap_History
import networkx as nx


def history_to_dag(history: deap_History) -> nx.DiGraph:
    graph = nx.DiGraph(history.genealogy_tree)
    graph = graph.reverse()  # Make the graph top-down

    return graph
