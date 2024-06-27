import json


def extract_job_ids_from_json(file_path):
    """
    Extracts job IDs from a JSON file and returns an iterator object.

    Args:
    - file_path (str): The path to the JSON file containing job listings.

    Returns:
    - List: A List object containing the job IDs.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    job_ids = [job['job_id'] for job in data]
    return job_ids


if __name__ == '__main__':
    file_path = "../data_files/raw/linkedin_jobs_101165590.json"
    job_ids_iterator = extract_job_ids_from_json(file_path)

    for job_id in job_ids_iterator:
        print(job_id)
