# Automated Linkedin Job Matching with Resume Parsing and Vector Databases

## Overview
This project aims to develop an automated job matching system that efficiently compares a candidate's resume against a database of job descriptions. The system extracts relevant information from a resume, converts it into vectors, and uses a vector database to find the most suitable job matches. The job data is sourced from an API, transformed, and stored in a structured format for comparison.

![proj_workflow.png](img%2Fproj_workflow.png)

## Key Skills and Tools Used

### Python Programming
- Utilized Python for data extraction, transformation, and comparison tasks.

### PDF Parsing
- **PyMuPDF (fitz)**: Extracted structured text from PDF resumes.
- **pdfplumber**: Extracted tabular data from PDF resumes.

### Natural Language Processing (NLP)
- **Sentence Transformers**: Employed pre-trained models (`all-MiniLM-L6-v2`) from the `sentence-transformers` library to convert text into dense vectors.

### Vector Databases
- **FAISS**: Implemented FAISS (Facebook AI Similarity Search) for efficient similarity search and storage of dense vectors.

### Data Handling
- **Pandas**: Managed and manipulated structured data for both resumes and job descriptions.

### Machine Learning Integration
- Developed an end-to-end pipeline to assess the compatibility of resumes with job descriptions using vector similarity.


## Project Execution Instructions
- Create an free trial account in '[scrapingdog](https://docs.scrapingdog.com/)'
- Extract the API_KEY from scrapingdog and store as env variable
- Execute the commands in a new virtual env,Python version 3.10 
  - 'pip install poetry'
  - 'poetry install'
- Ensure to place your resume(pdf) under data_files/raw_zone
- Update the project variables as per your requirements config_files/config
  - Variable : geoid, Job search location
  - Variable : job_title
  - Variable : resume_pdf_path, file name of your resume
  - Variable : jobs_to_match, count of jobs you want to match against your resume
- Execute the app.py python file
- Matched jobs as per your resume will be placed under data_files/data_product_zone

## Project Structure
```
linkedin_job_matcher/
├── config_files/
│   ├── __init__.py
│   ├── config.py
│   └── raw_json_extract_fields.yml
├── data_files/
│   └── data_product_zone/
│   └── raw_zone/
│   └── transformed_zone/
├── src/
│   ├── data_processor/
│   │   ├── __init__.py
│   │   └── generate_transformed_data.py
│   ├── helper_scripts/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── job_matcher/
│   │   ├── __init__.py
│   │   └── resume_match.py
│   └── job_scrapper/
│       ├── __init__.py
│       └── job_id_scrapper.py
├── .gitignore
├── app.py
├── noxfile.py
├── PROJECT_DETAILS.md
└── pyproject.toml
```
### project config files
- config_files/config.py: Python file for configuration settings and variables used across the project.
- config_files/raw_json_extract_fields.yml: YAML files with the fields extracted from scrapped JSON response.
- pyproject.toml: Configuration file for the project and packages used.
- noxfile.py: Configuration for sessions used to lint and trigger tests
- app.py: Main application script, executes and finally places the matched jobs in data_files/data_product_zone.

### data_files/
Directory for storing raw and processed data files.

### src/
Main source directory for project code.

#### data_processor/
Contains scripts for processing data.
- generate_transformed_data.py: Script to generate transformed data.

##### helper_scripts/
Contains utility scripts.
- helpers.py: Utility helper functions.

##### job_matcher/
Contains scripts related to job matching.
- resume_match.py: Script to match resumes with jobs.

##### job_scrapper/
Contains job scraping scripts.
- job_id_scrapper.py: Script to scrape job IDs.

### Project Workflow

1. **API Response Handling**:
    - Retrieved job data from an API, receiving two separate JSON responses.
    - Parsed and formatted these JSON responses.

2. **Data Transformation**:
    - **DuckDB**: Utilized DuckDB to transform and combine the two JSON responses into a single structured CSV file.

3. **Resume Parsing**:
    - Extracted text and tables from PDF resumes using PyMuPDF and pdfplumber.
    - Focused on key sections: Profile, Technical Skills, Education, and Work Experience.

4. **Data Vectorization**:
    - Converted job descriptions and resume sections into vectors using Sentence Transformers.

5. **Vector Storage and Search**:
    - Stored vectors in FAISS for efficient retrieval.
    - Queried the database with the resume vector to find the most similar job descriptions.

6. **Job Matching**:
    - Compared the resume against job descriptions to identify the best matches based on vector similarity.

### Results

The system successfully automates the job matching process, providing a scalable and efficient solution for candidates to find jobs that best match their skills and experiences.

### Conclusion

This project demonstrates the effective use of modern NLP techniques and vector databases to solve real-world problems. By leveraging Python and a suite of powerful libraries, we created a robust system that streamlines the job search process for candidates.
