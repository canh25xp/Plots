import math
import matplotlib.pyplot as plt
from pathlib import Path

CWD = Path(__file__).resolve().parents[0]
ROOT = CWD.parents[0]


def get_fig_size(fig_width_cm, fig_height_cm=None):
    """Convert dimensions in centimeters to inches.
    If no height is given, it is computed using the golden ratio.
    """
    if not fig_height_cm:
        golden_ratio = (1 + math.sqrt(5)) / 2
        fig_height_cm = fig_width_cm / golden_ratio

    size_cm = (fig_width_cm, fig_height_cm)
    return map(lambda x: x / 2.54, size_cm)


"""
The following functions can be used by scripts to get the sizes of
the various elements of the figures.
https://matplotlib.org/stable/users/explain/customizing.html
"""


def label_size():
    """Size of axis labels"""
    return 10


def font_size():
    """Size of all texts shown in plots"""
    return 10


def ticks_size():
    """Size of axes' ticks"""
    return 8


def axis_lw():
    """Line width of the axes"""
    return 0.6


def plot_lw():
    """Line width of the plotted curves"""
    return 1.5


def figure_setup():
    """
    Set all the sizes to the correct values and use
    tex fonts for all texts.
    """
    params = {
        "text.usetex": True,
        "figure.dpi": 200,
        "font.size": font_size(),
        "font.serif": [],
        "font.sans-serif": [],
        "font.monospace": [],
        "axes.labelsize": label_size(),
        "axes.titlesize": font_size(),
        "axes.linewidth": axis_lw(),
        "text.fontsize": font_size(),
        "legend.fontsize": font_size(),
        "xtick.labelsize": ticks_size(),
        "ytick.labelsize": ticks_size(),
        "font.family": "serif",
    }
    plt.rcParams.update(params)


def remove_creation_date(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if 'CreationDate' not in line:
                file.write(line)


def Save_fig(fig, file_name, fmt=None, dpi=300, tight=True, creation_date = False):
    """
    Save a Matplotlib figure as EPS/PNG/PDF to the given path and trim it.
    """

    save_folder = ROOT / "Figures"
    save_folder.mkdir(parents=True, exist_ok=True)

    if not fmt:
        fmt = file_name.strip().split(".")[-1]

    if fmt not in ["eps", "png", "pdf"]:
        raise ValueError("unsupported format: %s" % (fmt,))

    extension = ".%s" % (fmt,)
    if not file_name.endswith(extension):
        file_name += extension

    # save figure
    if tight:
        fig.savefig(save_folder / file_name, bbox_inches="tight", dpi=dpi)
    else:
        fig.savefig(save_folder / file_name, dpi=dpi)

    if not creation_date:
        remove_creation_date(save_folder / file_name)
