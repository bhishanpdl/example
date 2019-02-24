import numpy as np
import scipy as sp
from scipy import stats as sps
import scipy.optimize as op

import example

class MyClass(object):

    def __init__(self, arg1, arg2):
        """Simple description.

        Parameters
        ----------
        arg1: list or tuple, dicts
            components to use.
        arg2: boolean
            verbose or not.

        """
        self.arg1 = arg1
        self.arg2 = arg2
        self.mylen = len(arg1)


    def func1(self, arr):
        """
        Do some calculations.

        Parameters
        ----------
        arr: numpy.ndarray
            array whose sum is to be calcualated

        Returns
        -------
        mysum: float
            total sum of array
        """
        return np.sum(arr)