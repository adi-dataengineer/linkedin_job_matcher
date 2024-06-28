import os

from dotenv import load_dotenv

load_dotenv()
raw_zone = "data_files/raw_zone"
transformed_zone = "data_files/transformed_zone"
data_product_zone = "data_files/data_product_zone"
scrapped_jobs_csv_path = f"{transformed_zone}/combined_linkedin_jobs.csv"
resume_pdf_path = f'{raw_zone}/{os.getenv("RESUME_FILE_NAME")}'
job_desc_col = "job_description"
matching_jobs_output_file = f"{data_product_zone}/matched_jobs.csv"
fetch_fresh_data = False
job_title = "data engineer"
geoid = "101165590"  # GeoID for London
page_scrape_cnt = "10"
jobs_to_match = 5
