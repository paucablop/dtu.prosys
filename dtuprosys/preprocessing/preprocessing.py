from scipy.signal import savgol_filter

import pandas as pd


class RangeCut:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        return x.iloc[:, self.start : self.end]


class Derivative:
    def __init__(
        self, derivative_order: int, window_length: int = 15, polynomial_order: int = 1
    ):
        self.derivative_order = derivative_order
        self.window_length = window_length
        self.polynomial_order = polynomial_order

    def apply_to(self, x: pd.DataFrame) -> pd.DataFrame:
        return savgol_filter(
            x, self.window_length, self.polynomial_order, deriv=self.derivative_order
        )
