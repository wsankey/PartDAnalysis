import pandas as pd
#Let's read in the CSV and retain the columns we're interested in.
df = pd.read_csv("PartD_Prescriber_PUF_NPI_DRUG_Aa_AL_CY2013.csv")

df = df[['npi', 'total_drug_cost', 'nppes_provider_last_org_name', 'nppes_provider_first_name', 'nppes_provider_city', 'nppes_provider_state', 'generic_name']]
#We identify the following generics as opioids. 
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
#The opioids function is applied and the opioids retained. 
df['opioid_var'] = df.apply(opiods, axis=1)
df = df.loc[(df.opioid_var==True)]
#Our total drug cost column is messy and needs cleaning. 
df['total_drug_cost'] = df['total_drug_cost'].fillna(0)
df['total_drug_cost'] = df['total_drug_cost'].str.strip("$")
df['total_drug_cost'] = df['total_drug_cost'].str.replace(',','')
df['total_drug_cost'] = df['total_drug_cost'].astype(float)
#Group and sum by provider NPI, sort the summed column in descending order and send our dataset to a CSV file. 
df['tot'] = df['total_drug_cost'].groupby(df['npi']).transform('sum')
df = df.drop_duplicates(cols='npi')

top100 = df.sort('tot', ascending=False)[:100]
top100 = top100[['npi', 'tot', 'nppes_provider_last_org_name', 'nppes_provider_first_name', 'nppes_provider_city', 'nppes_provider_state']]
print top100.head(5)
top100.to_csv('top_prescribers_in_first_file.csv')
