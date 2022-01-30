import pandas as pd
from prophet import Prophet


df = pd.read_csv('./models/data1.csv')
df.head()