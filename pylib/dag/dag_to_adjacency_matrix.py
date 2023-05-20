import itertools as it

from Bio.Phylo.TreeConstruction import (
    DistanceMatrix as BioPhylo_DistanceMatrix,
)
import networkx as nx
import numpy as np

from ..util import to_tril
from .calc_dag_depths import calc_dag_depths


def dag_to_adjacency_matrix(dag: nx.DiGraph) -> BioPhylo_DistanceMatrix:

    extant_nodes = [node for node in dag if dag.out_degree(node) == 0]

    num_nodes = len(extant_nodes)
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    # Populate the distance matrix with the lowest common ancestor distances
    lcas = [
        *nx.all_pairs_lowest_common_ancestor(
            dag, pairs=it.combinations(extant_nodes, 2)
        )
    ]

    dag_depths = calc_dag_depths(dag)

    idx = {x: i for i, x in enumerate(extant_nodes)}
    for pair, lca in lcas:
        node1, node2 = pair
        adjacency_matrix[idx[node1]][idx[node2]] = (
            dag_depths[node1] + dag_depths[node2] - dag_depths[lca] * 2
        )
        adjacency_matrix[idx[node2]][idx[node1]] = adjacency_matrix[
            idx[node1]
        ][idx[node2]]

    # Create a Biopython distance matrix object
    return BioPhylo_DistanceMatrix(
        [*map(str, extant_nodes)], matrix=to_tril(adjacency_matrix)
    )
