# Problem statement
Abalones are sea snails that live in kelp forest in ocean water. They are very nutritious and expensive delicacy for their unique taste. Thus, they are in high demand, especially in Asia. This has created a multibillion dollar export industry.

There is a positive correlation between the economic value and age of abalone, meaning that as the abalone is older it is more expensive. This makes determining the age of abalone very important to those involved in this business.

The goal of the project is to predicit the age of abalone from physical measurements with machine learning.

# Methodology
Various models were built, and their performance was evaluated with R^2 score, and root mean square error (RMSE). The winning model is Random Forests from the `sklearn` library. The evaluation scores on the test data set are: R^2 = 0.570045, and RMSE = 2.000499.
