## Introduction
Abalones are sea snails that live in kelp forest in ocean water. They are very nutritious and expensive delicacy for their unique taste. Thus, they are in high demand, especially in Asia. This has created a multibillion dollar export industry.

There is a positive correlation between the economic value and age of abalone, meaning that as the abalone is older it is more expensive. This makes determining the age of abalone very important to those involved in this business.

<p align="center">
    <img src="images\abalone.jpg" width="320"/><br>
    <b>Figure 1.</b> Sharktopus, 2011, <i>Living abalone showing epipodium and tentacles, in display tank at Ty Warner Sea Center on Stearns Wharf, Santa Barbara, California.</i>, image, Wikimedia Commons, viewed 21 July 2020, <a href="https://commons.wikimedia.org/wiki/File:LivingAbalone.JPG">URL</a>.
</p>

## Problem statement

### Goal
The goal of the project is to predicit the age of abalone from physical measurements.

### Motivation
The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope, which is a boring and time-consuming task. The motivation of the project is to use physical measurements of abalone that are easier to obtain, and use them to predict the age with machine learning models.

### Methodology
The dataset comes from an original study: Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994) "The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait", Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288).

The dataset contains the following features:

| Feature | Data Type | Measurement Unit | Description |
| --- | --- | --- | --- |
| **Sex** | categorical | -- | M (male), F (female), and I (infant) |
| **Length** | continuous | mm | Longest shell measurement |
| **Diameter** | continuous | mm | perpendicular to length |
| **Height** | continuous | mm | with meat in shell |
| **Whole weight** | continuous | grams | whole abalone |
| **Shucked weight** | continuous | grams | weight of meat |
| **Viscera weight** | continuous | grams | gut weight (after bleeding) |
| **Shell weight** | continuous | grams | after being dried |
| **Rings** | discrete | -- | +1.5 gives the age in years |

The number of rings is the target value. If it is treated as a continuous value, the problem can be treated as a supervised learning regression problem.

As a starting point, $k$-nearest neighbours model is chosen as a baseline because it gives a reasonable performance without a lot of adjustments.

From there, the following subset of more advanced models from the `scikit-learn` library are learned to solve the problem with their default hyper-parameters:
- Ridge Regression;
- Support Vector Regression;
- Stochastic Gradient Descent;
- Gaussian Process Regression;
- Decision Trees;
- Random Forests;
- Gradient Boosting for regression.

Next, with grid search, the hyper-parameters are tuned in an attempt to imporve the performance of the models.

Finally, voting regression is used as an ensemble learning model that fits the five best performing models with their hyper-parameters tuned.

## Experimental Evaluation

### Methodology
$R^{2}$ score is the metrics used for evaluation of the performance of the models, as a percentage of variation between the value of the target and the predicted value of the target.

First, the mean cross-validated $R^{2}$ score from the models with the default hyper-parameters is computed. Then, the best mean cross-validated $R^{2}$ score from the tuned models is computed, and those values are compared.

Next, the five best performing regressors with tuned hyper-parameters are used for the ensemble learning model.

Finally, the performance of the models is evaluated on the test dataset: the baseline, the models with tuned hyper-parameters, and the voting regressor.

### Results
The table below summarizes the mean cross-validated $R^{2}$ score from the training of the regressors.

| Model	| Mean cross-validated $R^{2}$ score | Improved mean cross-validated $R^{2}$ score | Improvement |
| --- | --- | --- | --- |
| SVR | 0.5448 | 0.5449 | 0.0184 |
| GaussianProcessRegressor | -230.8753 | 0.5307 | -100.2299 |
| Ridge | 0.5365 | 0.5301 | -1.1929 |
| RandomForestRegressor | 0.5246 | 0.5252 | 0.1144 |
| SGDRegressor | 0.5192 | 0.5243 | 0.9823 |
| GradientBoostingRegressor | 0.5332 | 0.5243 | -1.6692 |
| DecisionTreeRegressor | 0.1123 | 0.4277 | 280.8549 |

The table below summarizes the mean cross-validated $R^{2}$ score of the models with tuned hyper-parameters and the voting regression model compared to the baseline, on the train dataset.

| Model | $R^{2}$ Score |
| --- | --- |
| VotingRegressor | 0.5574 |
| SVR | 0.5449 |
| GaussianProcessRegressor | 0.5307 |
| Ridge | 0.5301 |
| RandomForestRegressor | 0.5252 |
| SGDRegressor | 0.5243 |
| GradientBoostingRegressor | 0.5243 |
| KNeighborsRegressor - Baseline | 0.4604 |
| DecisionTreeRegressor | 0.4277 |

The table below summarizes the mean cross-validated $R^{2}$ score of the models with tuned hyper-parameters and the voting regression model compared to the baseline, on the test dataset to assess how well the models generalize to previously unseen data.

| Model | $R^{2}$ Score |
| --- | --- |
| VotingRegressor | 0.5288 |
| SVR | 0.5259 |
| RandomForestRegressor | 0.5104 |
| KNeighborsRegressor - Baseline | 0.5055 |
| GaussianProcessRegressor | 0.4893 |
| Ridge | 0.4892 |
| GradientBoostingRegressor | 0.4875 |
| SGDRegressor | 0.4754 |
| DecisionTreeRegressor | 0.4086 |

### Discussion
According to the analysis of the evaluation metrics on the test data set, the model VotingRegressor, that fits the base regressors: SVR, GaussianProcessRegressor, Ridge, RandomForestRegressor, and SGDRegressor, has the best $R^{2}$ score of 0.5288. Thus, this is the chosen model for the solution of the problem of predicting the age of abalone from physical measurements.

## Related Work
The problem of predicting the age of abalone has been attacked in other work ([here](https://mpra.ub.uni-muenchen.de/91210/), and [here](https://ieeexplore.ieee.org/abstract/document/8970983)).

## Future Work
It is evident from the summary of the performance of the final models that the highest $R^{2}$ Score is mere 0.5288, i.e., 52.88% variation between the age of abalone and the predicted age of abalone, which suggests that the problem should be attacked with more advanced tecniques. Possible solutions that might result in better performance are:
- Decreasing the value of the skewness because the features are skewed.
- Applying more sophisticated algorithms like gradient boosting with the `XGBoost` library, neural networks, and deep learning.
- Re-stating the problem as classification because the age is a discrete numerical feature. 

## Conclusion
Determining the age of abalone is an important task because it affects the revenue of the industry. The traditional approach is time-consuming, and different approaches are needed to speed up the process. This project aims to address that by determining the age of abalone from physical measurments with machine learning algorithms. The problem was treated as regression, and several regressors from the scikit-learn library were learned. The performance was evaluated with the $R^{2}$ score. The models however, so far are not good enough to be deployed. Namely, the best performing model is voting regression, that fits the base estimators: SVR, GaussianProcessRegressor, Ridge, RandomForestRegressor, and SGDRegressor, and has $R^{2}$ score of 0.5288, which suggests that more work is needed.

## Bibliography
- Poaching for Abalone, Africa’s ‘White Gold,’ Reaches Fever Pitch (2017) Animals. Available at: https://www.nationalgeographic.com/animals/article/wildlife-watch-abalone-poaching-south-africa (Accessed: 21 July 2020).
- Hossain, M. and Chowdhury, N.M. (no date) ‘Econometric Ways to Estimate the Age and Price of Abalone’, p. 19.
- Abalone. (1995). UCI Machine Learning Repository.
- Exploratory Data Analysis - Calculations (2020) Building Intelligence Together. Available at: https://koopingshung.com/blog/exploratory-data-analysis-non-visual/ (Accessed: 21 July 2020).
- Exploratory Data Analysis - Using Visualization (2020) Building Intelligence Together. Available at: https://koopingshung.com/blog/exploratory-data-analysis-using-visualization/ (Accessed: 21 July 2020).
- Müller, A. and Guido, S., 2016. Introduction to machine learning with Python. O'Reilly Media, Inc., p.44, 299.
- M. F. Misman et al., "Prediction of Abalone Age Using Regression-Based Neural Network," 2019 1st International Conference on Artificial Intelligence and Data Sciences (AiDAS), 2019, pp. 23-28, doi: 10.1109/AiDAS47888.2019.8970983.

