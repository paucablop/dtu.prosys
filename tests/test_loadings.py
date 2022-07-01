from dtuprosys.datasets import load_train_data, load_fermentation_data

def test_train_loadings():
  # Arrange

  # Act
  spectra, reference = load_train_data()

  # Assert
  assert spectra.shape == (21, 1047)
  assert reference.shape == (21, 3)


def test_fermentation_loadings():
  # Arrange

  # Act
  spectra, reference = load_fermentation_data()

  # Assert
  assert spectra.shape == (1629, 1047)
  assert reference.shape == (34, 6)
