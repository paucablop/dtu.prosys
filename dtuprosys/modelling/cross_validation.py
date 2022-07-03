from mbpls.mbpls import MBPLS
from sklearn.model_selection import validation_curve, LeaveOneOut
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import pandas as pd

def cross_validation(
    X: pd.DataFrame, y: pd.DataFrame, n_folds: int = 5, n_components: int = 2
) -> None:
    """
    Performs cross-validation on the data.
    @param X: dataframe of features
    @param y: dataframe of target
    @param n_folds: number of folds
    @param n_components: number of components
    """

    # Initialize model
    model = MBPLS(n_components=n_components)

    # Initialize cross-validation parameters
    cv = LeaveOneOut()
    param_name = "n_components"
    param_range = range(1, 10)
    scoring = "neg_root_mean_squared_error"

    # Perform cross-validation
    test_scores, validation_scores = validation_curve(
        model, X, y, cv = cv, param_name=param_name, param_range=param_range, scoring=scoring
    )

    # Plot results
    plt.figure(figsize=(10, 3))
    plt.title("Cross-validation")
    plt.xlabel(param_name)
    plt.ylabel("root mean squared error")
    plt.plot(param_range, -test_scores.mean(axis=1), 'o-', label="Test error", color="red")
    plt.plot(param_range, -validation_scores.mean(axis=1), 'o-', label="Validation error", color="blue")
    plt.legend()
    plt.show()

    return None
