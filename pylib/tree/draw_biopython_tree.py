import copy
import typing

from Bio import Phylo as BioPhylo
from matplotlib import pyplot as plt
from matplotlib.axes import Axes as mpl_Axes
from matplotlib.figure import Figure as mpl_Figure

from .color_biopython_tree import color_biopython_tree as color_tree
from .pare_biopython_tree import pare_biopython_tree as pare_tree
from .sort_biopython_tree import sort_biopython_tree as sort_tree


def draw_biopython_tree(
    tree: BioPhylo.BaseTree,
    fig_size: tuple = (6.5, 4),
    line_width: float = 4.0,
    drop_overlapping_labels: bool = False,
    max_leaves: typing.Optional[int] = None,
) -> mpl_Figure:

    biopy_tree = copy.deepcopy(tree)

    if max_leaves is not None:
        biopy_tree = pare_tree(biopy_tree, max_leaves)

    sort_tree(biopy_tree.root)
    color_tree(biopy_tree.root)

    with plt.rc_context({
        'lines.linewidth': line_width,
    }):
        plt.gcf().set_size_inches(*fig_size)
        BioPhylo.draw(
            biopy_tree,
            axes=plt.gca(),
            label_func=lambda node: "" if not node.is_terminal() else node.name,
            do_show=False,
        )
        if drop_overlapping_labels:
            # Code to remove overlapping annotations
            bboxes = []
            for label in plt.gca().texts:
                bbox = label.get_window_extent()
                # Check if current label overlaps with the others
                overlaps = any(bbox.overlaps(bbox_) for bbox_ in bboxes)
                if overlaps:
                    label.set_visible(False)
                else:
                    bboxes.append(bbox)
