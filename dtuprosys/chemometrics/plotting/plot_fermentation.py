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

    plt.figure(figsize=(10, 3))
    plt.title("Fermentation frofile")
    plt.xlabel("Time (h)")
    plt.ylabel("Glucose concentration (g/l)")
    plt.plot(time * 1.28 / 60, prediction, color="blue")
    plt.plot(fermentation_hplc["time"], fermentation_hplc["glucose"], "o", color="red")
    return None
