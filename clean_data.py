import os
import pandas as pd

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

def clean_job_data(input_file="data/linkedin_jobs.csv", output_file="data/cleaned_jobs.csv"):
    df = pd.read_csv(input_file)

    df.drop_duplicates(inplace=True)
    df.dropna(subset=["Job Title"], inplace=True)
    df["Location"] = df["Location"].str.strip()

    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")
