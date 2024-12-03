from jenkinsapi import jenkins

# Jenkins server credentials
JENKINS_URL = 'http://51.20.143.126:8080/'
USERNAME = 'myakovkin'
API_TOKEN = 'Ahv*w35316'
JOB_NAME = 'GitHubPipelineJob'

# # Connect to Jenkins
# server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=API_TOKEN)

# # Job name
# job_name = 'GitHubPipelineJob'

# # GitHub repository details
# github_repo_url = 'https://github.com/CaCuCkA/test-docker.git'
# branch_name = 'main' 

# with open('pipeline_config.xml', 'r') as file:
#     pipeline_config = file.read()

# pipeline_config = pipeline_config.replace('{{github_repo_url}}', github_repo_url)
# pipeline_config = pipeline_config.replace('{{branch_name}}', branch_name)

# try:
#     server.create_job(job_name, pipeline_config)
#     print(f"Job '{job_name}' created successfully!")
# except jenkins.JenkinsException as e:
#     print(f"Failed to create job: {e}")


# server = jenkins.Jenkins(JENKINS_URL, username=USERNAME, password=API_TOKEN)

# # Get the current job configuration
# current_config = server.get_job_config(JOB_NAME)
# print("Current Job Config:")
# print(current_config)

# # Modify the configuration (add changes)

# # Update the job with the new configuration
# server.reconfig_job(JOB_NAME, new_config)

# current_config = server.get_job_config(JOB_NAME)
# print("Current Job Config:")
# print(current_config)

# print(f"Job '{JOB_NAME}' updated successfully.")

import requests

# Define your Jenkins credentials and URL
# job_url = f"{JENKINS_URL}/job/{JOB_NAME}/config.xml"
# response = requests.get(job_url, auth=(USERNAME, API_TOKEN))

CRUMB_URL = f"{JENKINS_URL}/crumbIssuer/api/json"
crumb_response = requests.get(CRUMB_URL, auth=(USERNAME, API_TOKEN))


if crumb_response.status_code == 200:
    crumb_data = crumb_response.json()
    crumb_header = {crumb_data['crumbRequestField']: crumb_data['crumb']}
    print("Crumb retrieved successfully.")
    print(crumb_header)
else:
    print(f"Failed to retrieve crumb. Status Code: {crumb_response.status_code}")
    exit(1)
# if response.status_code == 200:
#     current_config = response.text
#     print("Current Job Config:")
#     print(current_config)
# else:
#     print(f"Failed to retrieve job configuration. Status Code: {response.status_code}")
#     exit(1)

# new_config = current_config.replace("<scriptPath>Jenkinsfile</scriptPath>",
#                                     "<scriptPath>docker_build.jenkins</scriptPath>")


# headers = {"Content-Type": "application/xml"}
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# headers.update(crumb_header)
# update_response = requests.post(job_url, data=new_config, auth=(USERNAME, API_TOKEN), headers=headers)

# if update_response.status_code == 200:
#     print(f"Job '{JOB_NAME}' updated successfully.")
# else:
#     print(f"Failed to update job. Status Code: {update_response.status_code}")