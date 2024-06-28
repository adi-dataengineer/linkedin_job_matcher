import fitz  # PyMuPDF
import pandas as pd
import pdfplumber
from sentence_transformers import SentenceTransformer

from src.helper_scripts.helpers import df_to_vectors, load_csv, query_resume, store_vectors


def extract_resume_info(pdf_path):
    resume_info = {
        "Profile": "",
        "Portfolio": "",
        "Technical Skills": "",
        "Education": "",
        "Work Experience": "",
        "Tables": [],
    }

    # Extract text and basic structure
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    # Extract tables
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                resume_info["Tables"].append(pd.DataFrame(table[1:], columns=table[0]))

    # Split text by sections
    sections = ["Profile", "Portfolio", "Technical Skills", "Education", "Work Experience"]
    section_texts = {section: "" for section in sections}

    current_section = None
    for line in text.split("\n"):
        stripped_line = line.strip()
        if stripped_line in sections:
            current_section = stripped_line
        elif current_section:
            section_texts[current_section] += stripped_line + " "

    for section in sections:
        resume_info[section] = section_texts[section].strip()

    print("RAW Resume data extracted...")
    return resume_info


def prepare_resume_text(resume_info):
    """
    Extracts and concatenates relevant content from the resume information
    for comparison with job descriptions.

    Args:
    resume_info (dict): The extracted resume information containing sections
                        and tables.

    Returns:
    str: The concatenated resume text.
    """
    # Extract relevant sections
    profile = resume_info.get("Profile", "")
    technical_skills = resume_info.get("Technical Skills", "")
    education = resume_info.get("Education", "")
    work_experience = resume_info.get("Work Experience", "")

    # Concatenate the relevant sections into a single string
    resume_text = "\n".join([profile, technical_skills, education, work_experience])

    # Optionally, you can add additional processing or filtering here if needed
    print("RAW Resume data cleansed...")

    return resume_text.strip()


def assess_resume_match(csv_path, vector_col_name, resume_text, top_k=5):
    # Load the CSV file
    df = load_csv(csv_path)

    # Load pre-trained model for vector conversion
    model = SentenceTransformer("all-MiniLM-L6-v2")  # example model

    # Convert job descriptions to vectors
    job_vectors = df_to_vectors(df, vector_col_name, model)

    # Store vectors in FAISS
    index = store_vectors(job_vectors)

    # Convert resume text to vector
    resume_vector = model.encode([resume_text])

    # Query the database with the resume vector
    matching_indices = query_resume(index, resume_vector, top_k)

    # Retrieve matching job postings
    matching_jobs = df.iloc[matching_indices[0]]

    print("Jobs match process complete!")

    return matching_jobs


if __name__ == "__main__":
    from config_files.config import data_product_zone, job_desc_col, jobs_to_match, resume_pdf_path, transformed_zone

    scrapped_jobs_csv_path = f"../../{transformed_zone}/combined_linkedin_jobs.csv"
    pdf_path = f"../../{resume_pdf_path}"
    matching_jobs_output_file = f"../../{data_product_zone}/matched_jobs.csv"

    raw_resume_data = extract_resume_info(pdf_path)
    resume_text = prepare_resume_text(raw_resume_data)
    matching_jobs = assess_resume_match(scrapped_jobs_csv_path, job_desc_col, resume_text, jobs_to_match)

    # Extract output as CSV
    matching_jobs.to_csv(matching_jobs_output_file)
