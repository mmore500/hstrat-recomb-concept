from Bio import Phylo as BioPhylo


def callibrate_branch_lengths_to_tip_origin_times(
    tree: BioPhylo.BaseTree,
    node_depths: typing.Dict,
) -> BioPhylo.BaseTree:

    # Get all clades in reverse order (from inner to outer)
    clades = list(reversed(list(tree.find_clades())))

    # Iterate over the clades
    for clade in clades:
        # Perform operations on each clade
        if clade.is_terminal():
            clade.origin_time = node_depths[int(clade.name)]
        else:
            clade.origin_time = np.mean(
                [c.origin_time - c.branch_length for c in clade.clades]
            )

    tree.root.branch_length = tree.root.origin_time

    return tree
