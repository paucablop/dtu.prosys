import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_fermentation(prediction: np.ndarray, fermentation_hplc: pd.DataFrame) -> None:
    """
    Plots the predicted concentration and the reference hplc measurements.
    @param prediction load the predictions.
    @param fermentation_hplc load the reference hplc measurements.
    """

    time = np.linspace(0, len(prediction), len(prediction))
    rmse = _calculate_rmse(prediction, fermentation_hplc)
    plt.figure(figsize=(10, 3))
    plt.title("Fermentation profile, RMSE: " + str(round(rmse, 2)))
    plt.xlabel("Time (h)")
    plt.ylabel("Glucose concentration (g/l)")
    plt.plot(time * 1.28 / 60, prediction, color="blue")
    plt.plot(fermentation_hplc["time"], fermentation_hplc["glucose"], "o", color="red")
    return None

def _calculate_rmse(prediction: np.ndarray, fermentation_hplc: pd.DataFrame) -> float:
    """
    Calculates the root mean squared error.
    @param prediction load the predictions.
    @param fermentation_hplc load the reference hplc measurements.
    @return root mean squared error
    """
    spectra_time = np.linspace(0, len(prediction), len(prediction)) * 1.28 / 60
    rmse = np.sqrt(np.mean((prediction.flatten() - np.interp(spectra_time, fermentation_hplc["time"], fermentation_hplc["glucose"])) ** 2))
    return rmse