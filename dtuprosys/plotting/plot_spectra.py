import matplotlib.pyplot as plt
import pandas as pd


def plot_spectra(spectra: pd.DataFrame, title: str, xlabel: str, ylabel: str):
    """
    Plots spectra.
    @param spectra dataframe containing the spectra with the wavenumbers as columns.
    @param title title of plot
    @param xlabel x-axis label
    @param ylabel y-axis label
    """

    plt.figure(figsize=(10, 3))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(spectra.columns, spectra.T)
    return None
