from Bio import Phylo as BioPhylo
from matplotlib import pyplot as plt
from matplotlib.axes import Axes as mpl_Axes
from matplotlib.figure import Figure as mpl_Figure


from .color_biopython_tree import color_biopython_tree as color_tree
from .sort_biopython_tree import sort_biopython_tree as sort_tree

def draw_biopython_tree(
    tree: BioPhylo.BaseTree,
    fig_size: tuple = (6.5, 4),
    line_width: float = 4.0,
) -> mpl_Figure:

    biopy_tree = tree
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
        # Code to remove overlapping annotations
        bboxes = []
        for label in sorted(plt.gca().texts, key=lambda l: l.get_text()):
            bbox = label.get_window_extent()
            # Check if current label overlaps with the others
            overlap = any(bboxes[i].overlaps(bbox) for i in range(len(bboxes)))
            if overlap:
                label.set_visible(False)
            else:
                bboxes.append(bbox)
