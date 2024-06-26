import json
import os

import requests
from dotenv import load_dotenv

from src.helper_scripts.helpers import extract_job_ids_from_json


def fetch_linkedin_jobs(api_key, job_title, geoid, page, output_file):
    """
    Fetch job listings from LinkedIn using ScrapingDog API and save the response as a JSON file.

    Args:
    - api_key (str): The API key for ScrapingDog.
    - field (str): The field or job title to search for.
    - geoid (str): The geographic location ID to search for jobs.
    - page (str): The page number to fetch results from.
    - output_file (str): The file path to save the response JSON data.

    Returns:
    - None
    """
    url = "https://api.scrapingdog.com/linkedinjobs/"
    params = {
        "api_key": api_key,
        "field": job_title,
        "geoid": geoid,
        "page": page
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {output_file}")
    else:
        print(f"Request failed with status code: {response.status_code}")


def fetch_linkedin_job_details(api_key, job_ids, output_file):
    """
    Fetch job details from LinkedIn using ScrapingDog API and save the details to a JSON file.

    Args:
    - api_key (str): The API key for ScrapingDog.
    - job_ids (list): A list of job IDs to fetch details for.
    - output_file (str): The file path to save the job details JSON data.

    Returns:
    - None
    """
    url = "https://api.scrapingdog.com/linkedinjobs"
    all_job_details = []

    for job_id in job_ids:
        params = {
            "api_key": api_key,
            "job_id": job_id
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            job_details = response.json()  # Assuming the API returns JSON data
            all_job_details.append(job_details)
        else:
            print(f"Request for job ID {job_id} failed with status code: {response.status_code}")

    # Write all job details to the output file
    with open(output_file, 'w') as f:
        json.dump(all_job_details, f, indent=4)

    print(f"Job details saved to {output_file}")


import requests
import json
from time import sleep


def fetch_linkedin_job_details(api_key, job_ids, output_file):
    """
    Fetch job details from LinkedIn using ScrapingDog API and save the details to a JSON file.

    Args:
    - api_key (str): The API key for ScrapingDog.
    - job_ids (iterator): An iterator (list or generator) of job IDs to fetch details for.
    - output_file (str): The file path to save the job details JSON data.

    Returns:
    - None
    """
    url = "https://api.scrapingdog.com/linkedinjobs"
    all_job_details = []
    batch_size = 10  # Adjust the batch size based on API limits and performance

    job_id_batches = [list(job_ids)[i:i + batch_size] for i in range(0, len(job_ids), batch_size)]

    for batch in job_id_batches:
        batch_job_details = []
        for job_id in batch:
            params = {
                "api_key": api_key,
                "job_id": job_id
            }

            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Raise HTTPError for bad responses

                job_details = response.json()  # Assuming the API returns JSON data
                batch_job_details.append(job_details)
            except requests.exceptions.RequestException as e:
                print(f"Request for job ID {job_id} failed: {e}")

            sleep(0.5)  # Add a small delay to prevent overwhelming the API (adjust as necessary)

        all_job_details.extend(batch_job_details)

    # Write all job details to the output file
    with open(output_file, 'w') as f:
        json.dump(all_job_details, f, indent=4)

    print(f"Job details saved to {output_file}")


def main(fetch_fresh_data):
    load_dotenv()
    api_key = os.getenv('api_key')
    job_title = "data engineer"
    geoid = "101165590"  # GeoID for London
    page_count = "10"
    jobs_output_file = f"linkedin_jobs_{geoid}.json"
    job_overview_output_file = f"linkedin_jobs_overview_{geoid}.json"

    if fetch_fresh_data:
        fetch_linkedin_jobs(api_key=api_key, job_title=job_title, geoid=geoid, page=page_count,
                            output_file=jobs_output_file)

    job_ids = extract_job_ids_from_json(jobs_output_file)

    if fetch_fresh_data:
        fetch_linkedin_job_details(api_key=api_key, job_ids=job_ids, output_file=job_overview_output_file)


if __name__ == '__main__':
    main(fetch_fresh_data=False)