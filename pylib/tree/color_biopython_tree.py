from Bio import Phylo as BioPhylo

from ..util import val_to_color


def color_biopython_tree(tree: BioPhylo.BaseTree) -> None:
    """Recursively color tree"""
    name = (
        tree.name
        if len(tree.clades) == 0
        else min(y.name for y in tree.get_terminals())
    )
    tree.color = val_to_color(name)

    for clade in tree.clades:
        color_biopython_tree(clade)
