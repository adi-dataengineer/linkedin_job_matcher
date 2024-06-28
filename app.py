from src.data_processor.generate_transformed_data import combine_linkedin_jobs
from src.job_matcher.resume_match import assess_resume_match, extract_resume_info, prepare_resume_text
from src.job_scrapper.job_id_scrapper import fetch_job_jsons

if __name__ == "__main__":
    from config_files.config import (
        fetch_fresh_data,
        geoid,
        job_desc_col,
        job_title,
        jobs_to_match,
        matching_jobs_output_file,
        page_scrape_cnt,
        raw_zone,
        resume_pdf_path,
        scrapped_jobs_csv_path,
        transformed_zone,
    )

    fetch_job_jsons(
        fetch_fresh_data=fetch_fresh_data,
        job_title=job_title,
        geoid=geoid,
        page_count=page_scrape_cnt,
        jobs_output_file_path=f"{raw_zone}",
    )
    combine_linkedin_jobs(
        linkedin_jobs_json=f"{raw_zone}/linkedin_jobs_{geoid}.json",
        linkedin_jobs_overview_json=f"{raw_zone}/linkedin_jobs_overview_{geoid}.json",
        output_file_name=f"{transformed_zone}/combined_linkedin_jobs",
    )
    raw_resume_data = extract_resume_info(f"{resume_pdf_path}")
    resume_text = prepare_resume_text(raw_resume_data)
    matching_jobs = assess_resume_match(f"{scrapped_jobs_csv_path}", job_desc_col, resume_text, jobs_to_match)

    # Extract output as CSV
    matching_jobs.to_csv(f"{matching_jobs_output_file}")
    print(f"All process completed - Output stored in {matching_jobs_output_file}")
