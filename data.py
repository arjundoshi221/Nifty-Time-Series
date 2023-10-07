import pandas as pd
import numpy as np

crudeoil = pd.read_excel(r'C:\Users\harsh\Downloads\data\crudeoil.xlsx')
DJI = pd.read_excel(r'C:\Users\harsh\Downloads\data\DJI.xlsx')
gold = pd.read_excel(r'C:\Users\harsh\Downloads\data\gold.xlsx')
nifty_50 = pd.read_csv(r'C:\Users\harsh\Downloads\data\NIFTY50.csv')
fedrate = pd.read_csv(r'C:\Users\harsh\Downloads\data\fedrate.csv')

crudeoil = crudeoil[['Date','Adj Close**']]
DJI = DJI[['Date','Adj Close**']]
gold = gold[['Date','Adj Close**']]
nifty_50 = nifty_50[['Date','Adj Close']]

crudeoil['Date'] = pd.to_datetime(crudeoil['Date'], format='%b %d, %Y')
DJI['Date'] = pd.to_datetime(DJI['Date'], format='%b %d, %Y')
gold['Date'] = pd.to_datetime(gold['Date'], format='%b %d, %Y')
nifty_50['Date'] = pd.to_datetime(nifty_50['Date'], format='%d-%m-%Y')

crudeoil.rename(columns={'Adj Close**': 'crudeoil_adjusted_close'}, inplace=True)
DJI.rename(columns={'Adj Close**': 'DJI_adjusted_close'}, inplace=True)
gold.rename(columns={'Adj Close**': 'gold_adjusted_close'}, inplace=True)
nifty_50.rename(columns={'Adj Close': 'nifty_50_adjusted_close'}, inplace=True)


merged_df = nifty_50.merge(crudeoil, on='Date', how='left')
merged_df = merged_df.merge(DJI, on='Date', how='left')
merged_df = merged_df.merge(gold, on='Date', how='left')

# Sort the dataframe by the "Date" column
merged_df = merged_df.sort_values(by='Date', ascending=True)

# Set the "Date" column as the index
merged_df = merged_df.set_index('Date')
merged_df = merged_df.asfreq('b') # Business days data
merged_df.to_csv('data.csv')