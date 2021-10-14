# Problem statement
Abalones are sea snails that live in kelp forest in ocean water. They are very nutritious and expensive delicacy for their unique taste. Thus, they are in high demand, especially in Asia. This has created a multibillion dollar export industry.

There is a positive correlation between the economic value and age of abalone, meaning that as the abalone is older it is more expensive. This makes determining the age of abalone very important to those involved in this business.

The goal of the project is to predicit the age of abalone from physical measurements with machine learning.

# Methodology
Various models were built, and their performance was evaluated with R^2 score, and root mean square error (RMSE). The winning model is Random Forests from the `sklearn` library with the following parameters: `'bootstrap': True, 'ccp_alpha': 0.0, 'criterion': 'mse', 'max_depth': 12, 'max_features': 'auto', 'max_leaf_nodes': None, 'max_samples': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 722, 'n_jobs': -1, 'oob_score': False, 'random_state': 0, 'verbose': 0, 'warm_start': False`.

The evaluation scores on the test data set are: R^2 = 0.552064, and RMSE = 2.041903.

You can read the full report of the project [here](https://djosifovski.github.io/portfolio/).

# Installation
- Clone the repository to your local computer.
- Install the requirements using `pip install -r requirements.txt`.
