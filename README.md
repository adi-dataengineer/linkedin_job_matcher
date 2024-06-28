# linkedin_job_matcher
Provides list of jobs that best match the resume

## Project Instructions
- Create an free trial account in 'scrapingdog'
- Extract the API_KEY from scrapingdog and store as env variable
- Execute the commands in a new virtual env,Python version 3.10 
  - 'pip install poetry'
  - 'poetry install'
- Ensure to place your resume(pdf) under src/data_files/raw_zone
- Update the project variables as per your requirements config_files/config
  - Variable : geoid, Job search location
  - Variable : job_title
  - Variable : resume_pdf_path, file name of your resume
  - Variable : jobs_to_match, count of jobs you want to match against your resume
- Execute the app.py python file
- Matched jobs as per your resume will be placed under 

# Project Structure
linkedin_job_matcher/
├── config_files/
│   ├── config.py
│   └── raw_json_extract_fields.yml
├── src/
│   ├── data_files/
│   │   └── data_product_zone/
│   │   └── raw_zone/
│   │   └── transformed_zone/
│   ├── data_processor/
│   │   └── generate_transformed_data.py
│   ├── helper_scripts/
│   │   └── helpers.py
│   ├── job_matcher/
│   │   └── resume_match.py
│   └── job_scrapper/
│       └── job_id_scrapper.py
├── app.py
├── noxfile.py
├── PROJECT_DETAILS.md
└── pyproject.toml

## project config files
- config_files/config.py: Python file for configuration settings and variables used across the project.
- config_files/raw_json_extract_fields.yml: YAML files with the fields extracted from scrapped JSON response.
- pyproject.toml: Configuration file for the project and packages used.
- noxfile.py: Configuration for sessions used to lint and trigger tests
- app.py: Main application script, executes and finally places the matched jobs in src/data_files/data_product_zone.
- PROJECT_DETAILS.md: Contains documentation of tools and methods used.

## src/
Main source directory for project code.

### data_files/
Directory for storing datwew4ssa files.

#### data_processor/
Contains scripts for processing data.
- generate_transformed_data.py: Script to generate transformed data.

#### helper_scripts/
Contains utility scripts.
- helpers.py: Utility helper functions.

#### job_matcher/
Contains scripts related to job matching.
- resume_match.py: Script to match resumes with jobs.

#### job_scrapper/
Contains job scraping scripts.
- job_id_scrapper.py: Script to scrape job IDs.
