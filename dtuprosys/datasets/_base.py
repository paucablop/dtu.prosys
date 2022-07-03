import pandas as pd


def load_train_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads the train data.
    @return train_spectra: spectra in the training data.
    @return train_hplc: hplc in the training data.
    """
    train_spectra = pd.read_csv("./datasets/data/train_spectra.csv")
    train_spectra.columns = train_spectra.columns.astype(float)
    train_hplc = pd.read_csv("./datasets/data/train_hplc.csv")

    return train_spectra, train_hplc


def load_fermentation_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads the fermentation data.
    @return fermentation_spectra: spectra measured during the fermentation.
    @return fermentation_hplc: hplc measured during the fermentation.
    """
    fermentation_spectra = pd.read_csv(
        "./datasets/data/fermentation_spectra.csv"
    )
    fermentation_spectra.columns = fermentation_spectra.columns.astype(float)
    fermentation_hplc = pd.read_csv("./datasets/data/fermentation_hplc.csv")

    return fermentation_spectra, fermentation_hplc
