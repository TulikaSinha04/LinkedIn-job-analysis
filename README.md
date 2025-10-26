# LinkedIn-job-analysis
The LinkedIn Job Trend Analysis project is designed to scrape, clean, and analyze job postings from  LinkedIn to understand hiring trends. The goal is to identify:  • Popular job titles  • Top hiring locations  • Emerging skill demands 
# Folder structure
linkedin_job_trend (folder creation)/ 
│── data (sub-folder)/                  <-- CSV files saved here 
         ── linkedin_jobs.csv   # Raw scraped job data   (csv file) (self created during running the code)
         ── cleaned_jobs.csv    # Cleaned and processed data  (csv file) (self created during running the code)
│ ── reports (sub-folder)/               <-- Analysis outputs 
       ── figures (sub-sub-folder)/ 
         ── top_cities.png  # Top 10 job locations (self created during running the code)
         ── top_roles.png   # Top 10 job titles (self created during running the code)
│   ── scripts (sub-folder)/               <-- Python scripts 
          ── __init__.py  (file) 
          ── scrape_jobs.py      # Scrapes LinkedIn job postings  (file) 
          ── clean_data.py       # Cleans scraped data  (file) 
          ── analyze_trends.py   # Performs analysis and visualization  (file) 
|   ── requirements.txt        # Python dependencies 
|   ── README.md               # Project documentation 
|   ── main.py                 # Master script to run all steps  (main file)
