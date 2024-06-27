import json
import pandas as pd
import duckdb
import yaml


def combine_linkedin_jobs(linkedin_jobs_json, linkedin_jobs_overview_json,output_file_name):
    # Read JSON files into pandas DataFrames
    df1 = pd.read_json(linkedin_jobs_json)
    df2 = pd.read_json(linkedin_jobs_overview_json)

    df_linked_in_jobs = df1.apply(lambda x: pd.Series({
        'job_position': x['job_position'],
        'job_link': x['job_link'],
        'job_id': x['job_id'],
        'company_name': x['company_name'],
        'company_profile': x['company_profile'],
        'job_location': x['job_location'],
        'job_posting_date': x['job_posting_date']
    }), axis=1)

    df_linked_in_jobs_overview = df2.apply(lambda x: pd.Series({
        'job_position': x[0]['job_position'],
        'company_name': x[0]['company_name'],
        'company_linkedin_id': x[0]['company_linkedin_id'],
        'base_pay': x[0]['base_pay'],
        'job_description': x[0]['job_description'],
        'Seniority_level': x[0]['Seniority_level'],
        'Employment_type': x[0]['Employment_type'],
        'Job_function': x[0]['Job_function'],
        'Industries': x[0]['Industries'],
        'recruiter_name': x[0]['recruiter_details'][0]['recruiter_name'],
        'recruiter_profile_url': x[0]['recruiter_details'][0]['recruiter_profile_url']
    }), axis=1)

    # Merge df based on job_position and company_name
    combined_df = pd.merge(df_linked_in_jobs, df_linked_in_jobs_overview,
                           on=['job_position', 'company_name'],
                           how='left')

    combined_df.to_csv(f'{output_file_name}.csv')
    combined_df.to_json(f'{output_file_name}.json', orient='records')

    return combined_df


if __name__ == '__main__':
    combine_linkedin_jobs(linkedin_jobs_json='../data_files/raw/linkedin_jobs_101165590.json',
                          linkedin_jobs_overview_json='../data_files/raw/linkedin_jobs_overview_101165590.json',
                          output_file_name='../data_files/transformed/combined_linkedin_jobs')
