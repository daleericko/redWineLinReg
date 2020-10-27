# Linear Regression Model in Python 
# Red Wine Quality dataset from Kaggle https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009

import pandas as pd
import seaborn as sns
from pyprojroot import here
from datetime import datetime

# Setup file paths 
todaysDate = datetime.today().strftime('%Y-%m-%d')

dataRawPath = here('data-raw')
dataOutputPath = here('data-output')

# read in the raw data 
redWineRaw = pd.read_csv(str(dataRawPath) + '/winequality-red.csv')

print(redWineRaw.head())