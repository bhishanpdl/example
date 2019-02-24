import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['text.usetex'] = True
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = 'Times New Roman'
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['savefig.dpi'] = 250
mpl.rcParams['savefig.format'] = 'pdf'
mpl.rcParams['savefig.bbox'] = 'tight'

from utils import infty as default_infty
from utils import epsilon as default_eps
from utils import lims as default_lims

print(default_lims)

class MyClass(object):

    def __init__(self, pi):
        """Initialization.

        Parameters
        ----------
        pi: float, optional
            value of pi

        """
        self.pi = pi

        return

    def plot(self, x,y,figname):
        """
        Plots x versus y.

        Parameters
        ----------
        x: list or numpy array
            list or ndarray to use as x axis
        y: list, optional
            yaxis values.
        figname: str
            name of figure to save.

        Notes
        -----
        x is required but y is optional.
        """

        plt.plot(x,y)
        plt.xlim(min(x), max(x))
        plt.legend(fontsize='large')
        plt.xlabel(r'$x$', fontsize=16)
        plt.ylabel(r'$y$', fontsize=16)
        plt.tight_layout()
        plt.savefig(figname, dpi=250)

        return


