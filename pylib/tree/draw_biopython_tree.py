from Bio import Phylo as BioPhylo
from matplotlib.axes import Axes as mpl_Axes
from matplotlib.figure import Figure as mpl_Figure


def draw_biopython_tree(
    tree: BioPhylo.BaseTree,
    fig_size: tuple = (10, 10),
    line_width: float = 4.0,
) -> mpl_Figure:
    from Bio import Phylo
    from matplotlib import pyplot as plt

    from .color_biopython_tree import color_biopython_tree as color_tree
    from .sort_biopython_tree import sort_biopython_tree as sort_tree

    biopy_tree = tree
    fig = plt.figure(figsize=fig_size)
    sort_tree(biopy_tree.root)
    color_tree(biopy_tree.root)
    plt.rcParams["lines.linewidth"] = line_width

    axes: mpl_Axes = fig.add_subplot(1, 1, 1)
    Phylo.draw(
        biopy_tree,
        label_func=lambda node: "" if not node.is_terminal() else node.name,
        axes=axes,
    )

    return fig
