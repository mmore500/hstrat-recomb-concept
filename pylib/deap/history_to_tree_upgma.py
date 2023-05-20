import typing

from Bio import Phylo as BioPhylo
from deap.tools.support import History as deap_History

from ..dag.dag_to_tree_upgma import dag_to_tree_upgma
from ..dag.prune_dag import prune_dag
from .history_to_dag import history_to_dag


def history_to_tree_upgma(
    history: deap_History, extant_nodes: typing.List
) -> BioPhylo.BaseTree:
    dag = prune_dag(history_to_dag(history), extant_nodes)
    return dag_to_tree_upgma(dag)
