import pandas as pd
import numpy as np

df = pd.read_csv("test.csv")
df = df[['npi', 'total_drug_cost', 'nppes_provider_last_org_name', 'nppes_provider_city', 'nppes_provider_state', 'generic_name']]

def opiods(series):
    if series["generic_name"]=="FENTANYL":
        return 1
    elif series["generic_name"]=="METHADONE HCL":
        return 1
    elif series["generic_name"]=="MORPHINE SULFATE":
        return 1
    elif series["generic_name"]=="OXYMORPHONE HCL":
        return 1
    else:
        return 0

df['opioid_var'] = df.apply(opiods, axis=1)
df = df.loc[(df.opioid_var==True)]

df['total_drug_cost'] = df['total_drug_cost'].fillna(0)
df['total_drug_cost'] = df['total_drug_cost'].str.strip("$")
df['total_drug_cost'] = df['total_drug_cost'].str.replace(',','')
df['total_drug_cost'] = df['total_drug_cost'].astype(float)

df['tot'] = df['total_drug_cost'].groupby(df['npi']).transform('sum')
df = df.drop_duplicates(cols='npi')
#df['total_drug_cost'] = df['total_drug_cost'].astype(int)
a =  df.sort('tot', ascending=False, axis=0)[:100]
a = a[['npi', 'tot', 'nppes_provider_last_org_name', 'nppes_provider_first_name', 'nppes_provider_city', 'nppes_provider_state']]
a.to_csv('out.csv')
#print newdf.head(10)
#print DataFrame.dtypes
#grouped = file_a.groupby('npi')['bene_count'].agg(lambda col: col.idxmax())[:100]
#print newdf.head(100)
#print grouped.head()
