from scipy.signal import savgol_filter
import logging
import numpy as np
import pandas as pd


class RangeCut:
    """
    Cuts a dataframe selecting the wavenumbers between start and end.
    """

    def __init__(self, start: int, end: int):
        """
        Constructor.
        @param start start wavenumber
        @param end end wavenumber
        """
        self.start = start
        self.end = end

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the cut to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return range cut dataframe
        """
        return x.loc[:, self.start : self.end]


class Derivative:
    """
    Calculates the derivative of a each row in a dataframe using the Savitzky-Golay filter.
    """

    def __init__(
        self, derivative_order: int, window_length: int = 15, polynomial_order: int = 1
    ):
        """
        Constructor.
        @param derivative_order derivative order
        @param window_length window length
        @param polynomial_order polynomial order
        """
        if polynomial_order < derivative_order:
            self.polynomial_order = derivative_order
            logging.warning("Polynomial order must be >= derivative order, setting polynomial order to derivative order.")
        else:
            self.polynomial_order = polynomial_order
        self.derivative_order = derivative_order
        self.window_length = window_length

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the derivative to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return dataframe with derivative
        """
        derivate = pd.DataFrame(savgol_filter(
            x, self.window_length, self.polynomial_order, deriv=self.derivative_order
        ))
        derivate.columns = x.columns
        return derivate

class DriftCorrection:
    """
    Corrects the drift in a dataframe.
    """

    def __init__(self):
        """
        Constructor.
        @param window_length window length
        @param polynomial_order polynomial order
        """

    def _drift_correct(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the drift correction to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return dataframe with drift corrected spectra
        """
        y1: float = x.iloc[0]
        y2: float = x.iloc[-1]

        x1: float = 0
        x2: float = x.shape[0]

        x_range = np.linspace(x1, x2, x2)
        slope: float = (y2 - y1) / (x2 - x1)
        intercept: float = y1 - slope * x1

        return x - (slope * x_range + intercept)



    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the drift correction to the dataframe.
        @param x dataframe containing the spectra with the wavenumbers as columns.
        @return dataframe with drift corrected spectra
        """
        return x.apply(self._drift_correct, axis=1)