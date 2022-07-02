from scipy.signal import savgol_filter

import pandas as pd


class RangeCut:
    """
    Cuts a range from a dataframe.
    """
    def __init__(self, start: int, end: int):
        """
        Constructor.
        @param start: start index
        @param end: end index
        """
        self.start = start
        self.end = end

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the cut to the dataframe.
        @param x: dataframe
        @return: dataframe with cut
        """
        return x.iloc[:, self.start : self.end]


class Derivative:
    """
    Calculates the derivative of a each row in a dataframe.
    """
    def __init__(
        self, derivative_order: int, window_length: int = 15, polynomial_order: int = 1
    ):
        """
        Constructor.
        @param derivative_order: derivative order
        @param window_length: window length
        @param polynomial_order: polynomial order
        """
        self.derivative_order = derivative_order
        self.window_length = window_length
        self.polynomial_order = polynomial_order

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        """
        Applies the derivative to the dataframe.
        @param x: dataframe
        @return: dataframe with derivative
        """
        return savgol_filter(
            x, self.window_length, self.polynomial_order, deriv=self.derivative_order
        )
