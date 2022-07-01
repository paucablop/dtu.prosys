import matplotlib.pyplot as plt

def plot_spectra(spectra, labels, title, xlabel, ylabel, save_path):
    """
    Plots spectra.
    spectra: list of lists of spectra
    labels: list of labels
    title: title of plot
    xlabel: x-axis label
    ylabel: y-axis label
    save_path: path to save plot

    """
    plt.figure(figsize=(10, 10))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for i in range(len(spectra)):
        plt.plot(spectra[i], label=labels[i])
    plt.legend()
    plt.savefig(save_path)
    plt.close()
    return None
