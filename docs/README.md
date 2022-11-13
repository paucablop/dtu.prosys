# Python Documentation

## Classes

**[RangeCut](RangeCut.md)**: Cuts a dataframe selecting the wavenumbers between start and end. 

**[Derivative](Derivative.md)**: Calculates the derivative of a each row in a dataframe using the Savitzky-Golay filter. 

**[DriftCorrection](DriftCorrection.md)**: Corrects the drift in a dataframe. 


## Functions

### plot_spectra


Plots spectra. 
#### Parameters
name | description | default
--- | --- | ---
spectra | dataframe containing the spectra with the wavenumbers as columns | 
title | title of plot | 
xlabel | x-axis label | 
ylabel | y-axis label | 
reference | dataframe containing the reference spectra with the wavenumbers as columns | None





### plot_predictions


Plots the PLS predictions and the reference hplc measurements for the training set. 
#### Parameters
name | description | default
--- | --- | ---
predictions | predicted concentrations. | 
reference | reference hplc measurements. | 





### plot_fermentation


Plots the predicted concentration and the reference hplc measurements. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 





### _calculate_rmse


Calculates the root mean squared error. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 





### cross_validation


Performs cross-validation on the data. By default it performs a leave-one-out cross-validation. 
#### Parameters
name | description | default
--- | --- | ---
X | spectra dataframe containing the spectra with the wavenumbers as columns. | 
y | dataframe containing the reference hplc measurements. | 
nr_components |  | 6





### load_train_data


Loads the train data. 




### load_fermentation_data


Loads the fermentation data. 




### test_train_loadings


Test the loading of the training data. 




### test_fermentation_loadings


Test the loading of the fermentation data. 




### test_range_cut


Test the range cut. 




### test_derivate


Test the derivative. 



