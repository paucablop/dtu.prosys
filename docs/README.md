# Python Documentation

## Classes

**[RangeCut](RangeCut.md)**: Cuts a range from a dataframe. 

**[Derivative](Derivative.md)**: Calculates the derivative of a each row in a dataframe. 


## Functions

### test_range_cut







### test_derivate







### test_train_loadings







### test_fermentation_loadings







### load_train_data


Loads the train data. 




### load_fermentation_data


Loads the fermentation data. 




### plot_predictions


Plots predictions and reference. 
#### Parameters
name | description | default
--- | --- | ---
predictions: | predictions | 
reference: | reference | 
predictions |  | 
reference |  | 





### plot_spectra


Plots spectra. 
#### Parameters
name | description | default
--- | --- | ---
spectra: | list of lists of spectra | 
title: | title of plot | 
xlabel: | x-axis label | 
ylabel: | y-axis label | 
spectra |  | 
title |  | 
xlabel |  | 
ylabel |  | 





### plot_fermentation


Plots predictions and reference. 
#### Parameters
name | description | default
--- | --- | ---
prediction | load the predictions. | 
fermentation_hplc | load the reference hplc measurements. | 





### cross_validation


Performs cross-validation on the data. 
#### Parameters
name | description | default
--- | --- | ---
X: | dataframe of features | 
y: | dataframe of target | 
n_folds: | number of folds | 
n_components: | number of components | 
X |  | 
y |  | 
n_folds |  | 5
n_components |  | 2




