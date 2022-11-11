import matplotlib.colors as colors
import matplotlib.pyplot as plt
import pandas as pd


def plot_spectra(spectra: pd.DataFrame, title: str, xlabel: str, ylabel: str, reference: pd.DataFrame = None):
    """
    Plots spectra.
    @param spectra dataframe containing the spectra with the wavenumbers as columns
    @param title title of plot
    @param xlabel x-axis label
    @param ylabel y-axis label
    @param reference dataframe containing the reference spectra with the wavenumbers as columns
    """

    if reference is not None:
        norm = plt.Normalize(reference.min(), reference.max())
        cmap = plt.get_cmap('viridis')
        colormap = cmap(norm(reference))
        plt.figure(figsize=(10, 3))
        for i, row, in spectra.iterrows():
            plt.plot(spectra.columns, row.values, color=colormap[i])
    else:
        plt.figure(figsize=(10, 3))
        for i, row, in spectra.iterrows():
            plt.plot(spectra.columns, row.values)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    return None

