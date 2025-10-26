from scripts.scrape_jobs import scrape_linkedin_jobs
from scripts.clean_data import clean_job_data
from scripts.analyze_trends import analyze_trends

if __name__ == "__main__":
    print("🚀 Starting LinkedIn Job Trend Analysis...")
    scrape_linkedin_jobs("Data Scientist", "India", num_pages=2)
    clean_job_data()
    analyze_trends()
    print("✅ Project Complete.")
