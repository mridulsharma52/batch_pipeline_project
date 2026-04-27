# ================================================
# Project: End-to-End Batch Data Pipeline
# Author: Mridul Sharma
# Description: Raw data ingestion layer
# ================================================



import pandas as pd
from datetime import datetime

def ingest_data():
    print("BATCH PIPELINE - INGESTION STARTED")
    print(f"Timestamp: {datetime.now()}")

    # Step 1: Load raw data
    print("\n[1/4] Loading raw data...")
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    df = pd.read_csv(url)
    print(f"Records loaded: {len(df)}")
    # Step 2: Add metadata
    print("\n[2/4] Adding metadata...")
    df['ingestion_timestamp'] = datetime.now()
    df['source_file'] = 'hw_200_external'
    df['pipeline_version'] = 'v1.0'

    # Step 3: Data quality checks
    print("\n[3/4] Running quality checks...")
    before = len(df)
    df = df.dropna()
    df = df.drop_duplicates()
    print(f"Removed: {before - len(df)} records")
   
    # Step 4: Save to raw zone
    print("\n[4/4] Saving to raw zone...")
    df.to_csv("raw_data.csv", index=False)
    print("Saved to raw_data.csv")
    print("\nINGESTION COMPLETED SUCCESSFULLY")
if __name__ == "__main__":
    ingest_data()
    exit()