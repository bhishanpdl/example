import numpy as np
import pandas as pd
import scipy as sp

from scipy import stats as sps
import sys


# some constants
global epsilon
epsilon = sys.float_info.epsilon
global infty
infty = sys.float_info.max * epsilon
global lims
lims = (epsilon, 1.)


def remove_nans(df):
    """Removes nans from given dataframe.

    Parameters
    ----------
    df: pandas dataframe
        This must be an pandas dataframe.

    Returns
    -------
    out_df: pandas dataframe
        dataframe without any nans.
    """
    out_df = df.dropna(how='any')
    return out_data