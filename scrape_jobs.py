import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

def scrape_linkedin_jobs(keyword, location, num_pages=3):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)

    jobs = []

    for page in range(num_pages):
        url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}&location={location}&start={page*25}"
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        listings = soup.find_all("div", {"class": "base-card"})

        for job in listings:
            title = job.find("h3", {"class": "base-search-card__title"})
            company = job.find("h4", {"class": "base-search-card__subtitle"})
            loc = job.find("span", {"class": "job-search-card__location"})

            jobs.append({
                "Job Title": title.text.strip() if title else None,
                "Company": company.text.strip() if company else None,
                "Location": loc.text.strip() if loc else None,
                "Keyword": keyword
            })

    driver.quit()
    df = pd.DataFrame(jobs)
    df.to_csv("data/linkedin_jobs.csv", index=False)
    print(f"✅ Scraped {len(df)} job listings saved to data/linkedin_jobs.csv")
