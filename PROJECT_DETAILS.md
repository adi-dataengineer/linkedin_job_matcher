# Automated Job Matching with Resume Parsing and Vector Databases

## Overview

This project aims to develop an automated job matching system that efficiently compares a candidate's resume against a database of job descriptions. The system extracts relevant information from a resume, converts it into vectors, and uses a vector database to find the most suitable job matches. The job data is sourced from an API, transformed, and stored in a structured format for comparison.

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
- **DuckDB**: Used DuckDB for efficient transformation of API JSON responses into a single CSV file.

### Machine Learning Integration
- Developed an end-to-end pipeline to assess the compatibility of resumes with job descriptions using vector similarity.

## Project Workflow

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

## Results

The system successfully automates the job matching process, providing a scalable and efficient solution for candidates to find jobs that best match their skills and experiences.

## Conclusion

This project demonstrates the effective use of modern NLP techniques and vector databases to solve real-world problems. By leveraging Python and a suite of powerful libraries, we created a robust system that streamlines the job search process for candidates.
