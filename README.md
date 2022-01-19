# Abalone Age Prediction

## Motivation
Determining the age of abalone is an important task because it affects the revenue of the industry. The traditional approach is time-consuming, and different approaches are needed to speed up the process. The motivation for this project is to address that by determining the age of abalone from physical measurments with machine learning models.

## Methodology
This is a regression type of problem in which a subset of learning algoritms were trained from `scikit-learn` and regression algorithm from `XGBoost`. As a single number evaluation metric R^2 is used, and after fine-tuning the models, the most optimal model is Support Vector Regressor where R^2=0.655027.
