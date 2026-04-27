import pandas as pd
from datetime import datetime

print("Starting ingestion...")
df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")
df['ingestion_timestamp'] = datetime.now()
df['source_file'] = 'nyc_taxi_apo'
df = df.dropna()
df = df.drop_duplicates()
print(f"Total records loaded: {len(df)}")
print(f"Coumns: {list(df.columns)}")
print(df.head())
df.to_csv("raw_taxi_data.csv", index=False)
print('Raw data saved to raw_taxi_data.csv')