import matplotlib.pyplot as plt
import numpy as np


def plot_predictions(predictions: np.ndarray, reference: np.ndarray) -> None:
    """
    Plots the PLS predictions and the reference hplc measurements for the training set.
    @param predictions predicted concentrations.
    @param reference reference hplc measurements.
    """

    plt.figure(figsize=(5, 4))
    plt.title("Predictions")
    plt.xlabel("Reference")
    plt.ylabel("Prediction")
    plt.plot(reference, predictions, "o", color="blue")
    plt.plot(
        [predictions.min().min(), predictions.max().max()],
        [predictions.min().min(), predictions.max().max()],
        color="red",
    )

    return None
