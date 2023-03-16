import pandas as pd
from ydata_profiling import ProfileReport

train = pd.read_csv('../Abalone-Age-Prediction/data/train.csv')
profile = ProfileReport(train, title="Profiling Report")
profile.to_file("Profiling_Report.html")