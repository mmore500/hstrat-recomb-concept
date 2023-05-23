from Bio import Phylo as BioPhylo
from Bio.Phylo.TreeConstruction import (
    DistanceTreeConstructor as BioPhylo_DistanceTreeConstructor,
)
import networkx as nx
import numpy as np

from ..tree.callibrate_branch_lengths_to_tip_origin_times import (
    callibrate_branch_lengths_to_tip_origin_times,
)
from .calc_dag_depths import calc_dag_depths
from .dag_to_adjacency_matrix import dag_to_adjacency_matrix


def _setup_origin_times(
    dag: nx.DiGraph, tree: BioPhylo.BaseTree
) -> BioPhylo.BaseTree:
    depths = calc_dag_depths(dag)
    return callibrate_branch_lengths_to_tip_origin_times(tree, depths)


def dag_to_tree_upgma(
    dag: nx.DiGraph,
    correct_origin_times: bool = True,
) -> BioPhylo.BaseTree.Tree:
    biopython_adjacency_matrix = dag_to_adjacency_matrix(dag)

    tree = BioPhylo_DistanceTreeConstructor().upgma(biopython_adjacency_matrix)

    if correct_origin_times:
        tree = _setup_origin_times(dag, tree)

    return tree
