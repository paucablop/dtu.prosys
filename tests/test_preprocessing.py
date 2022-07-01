from dtuprosys.datasets import load_train_data
from dtuprosys.preprocessing import RangeCut, Derivative

import pandas as pd

def test_range_cut():
  # Arrange
  start = 0
  end = 100
  range_cut = RangeCut(start, end)
  spectra = load_train_data()[0]

  # Act
  spectra_cut = range_cut(spectra)

  # Assert
  assert spectra_cut.shape == (21, 100)

def test_derivate():
  # Arrange
  derivative_order = 1
  window_length = 15
  polynomial_order = 1
  derivative = Derivative(derivative_order, window_length, polynomial_order)
  spectra = load_train_data()[0]

  # Act
  spectra_derivative = derivative(spectra)

  # Assert
  assert spectra_derivative.shape == spectra.shape
