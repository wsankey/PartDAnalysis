import pandas as pd
import numpy as np

df = pd.read_csv("test.csv", nrows=1000000)
print df.head(10)
def opiods(series):
    if series["generic_name"]=="FENTANYL":
        return 1
    else:
        return 0

df['opioid_var'] = df.apply(opiods, axis=1)
newdf = df[df.opioid_var==1]

#print DataFrame.dtypes
#grouped = file_a.groupby('npi')['bene_count'].agg(lambda col: col.idxmax())[:100]
print newdf.head(10)
#print grouped.head()
