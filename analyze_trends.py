import os
import pandas as pd
import matplotlib.pyplot as plt

# Ensure reports and figures folder exist
os.makedirs("reports/figures", exist_ok=True)

def analyze_trends(file="data/cleaned_jobs.csv"):
    df = pd.read_csv(file)

    # Top 10 cities
    top_cities = df["Location"].value_counts().head(10)
    plt.figure(figsize=(10,5))
    top_cities.plot(kind="bar")
    plt.title("Top 10 Job Locations")
    plt.ylabel("Job Count")
    plt.xlabel("City")
    plt.tight_layout()
    plt.savefig("reports/figures/top_cities.png")
    plt.show()

    # Top 10 job titles
    top_roles = df["Job Title"].value_counts().head(10)
    plt.figure(figsize=(10,5))
    top_roles.plot(kind="barh")
    plt.title("Top 10 Job Titles")
    plt.tight_layout()
    plt.savefig("reports/figures/top_roles.png")
    plt.show()
