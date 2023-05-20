from Bio import Phylo as BioPhylo


def sort_biopython_tree(tree: BioPhylo.BaseTree) -> None:
    """Recursively sort clades in-place in the tree based on their terminal elements' names"""
    tree.clades.sort(
        key=lambda x: x.name
        if len(x.clades) == 0
        else min(y.name for y in x.get_terminals())
    )

    for clade in tree.clades:
        sort_biopython_tree(clade)
