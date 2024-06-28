import json

import faiss
import pandas as pd


def store_vectors(vectors):
    d = vectors.shape[1]  # dimension of the vectors
    index = faiss.IndexFlatL2(d)  # using L2 distance
    index.add(vectors)
    return index


def query_resume(index, resume_vector, top_k=5):
    D, I = index.search(resume_vector, top_k)  # search for the top_k most similar vectors
    return I


def df_to_vectors(df, column_name, model):
    descriptions = df[column_name].tolist()
    vectors = model.encode(descriptions)
    return vectors


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df


def extract_job_ids_from_json(file_path):
    """
    Extracts job IDs from a JSON file and returns an iterator object.

    Args:
    - file_path (str): The path to the JSON file containing job listings.

    Returns:
    - List: A List object containing the job IDs.
    """
    with open(file_path, "r") as f:
        data = json.load(f)

    job_ids = [job["job_id"] for job in data]
    return job_ids


if __name__ == "__main__":
    from config_files.config import geoid, raw_zone

    file_path = f"../../{raw_zone}/linkedin_jobs_{geoid}.json"
    job_ids_iterator = extract_job_ids_from_json(file_path)

    for job_id in job_ids_iterator:
        print(job_id)
