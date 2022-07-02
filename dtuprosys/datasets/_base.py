import pandas as pd

def load_train_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads the train data.
    @return: tuple with spectra and hplc data.
    """
    train_spectra = pd.read_csv('./dtuprosys/datasets/data/train_spectra.csv')
    train_hplc = pd.read_csv('./dtuprosys/datasets/data/train_hplc.csv')

    return train_spectra, train_hplc


def load_fermentation_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Loads the fermentation data.
    @return: tuple with spectra and hplc data.
    """
    fermentation_spectra = pd.read_csv('./dtuprosys/datasets/data/fermentation_spectra.csv')
    fermentation_hplc = pd.read_csv('./dtuprosys/datasets/data/fermentation_hplc.csv')

    return fermentation_spectra, fermentation_hplc
