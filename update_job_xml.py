import os
import asyncio
import aiojenkins
import xml.etree.ElementTree as ET

# Jenkins details
JENKINS_URL = os.getenv('JENKINS_URL', 'http://51.20.72.170:8080')
USERNAME = os.getenv('JENKINS_USERNAME', 'myakovkin')
API_TOKEN = os.getenv('JENKINS_API_TOKEN', 'Ahv*w35316')
JOB_NAME = 'GitHubPipelineJob'
CONFIG_FILE_PATH = './pipeline_config.xml'
NEW_CONFIG_FILE = 'new.xml'

jenkins = aiojenkins.Jenkins(JENKINS_URL, USERNAME, API_TOKEN)

def modify_and_save_xml(config, new_file_path):
    root = ET.fromstring(config)

    description = root.find('description')
    if description is None:
        description = ET.SubElement(root, 'description')
    description.text = 'Pipeline from GitHub Repository'

    modified_config = ET.tostring(root, encoding='unicode', method='xml')

    with open(new_file_path, 'w+') as file:
        file.write(modified_config)

    return new_file_path

async def func():
    try:
        res = await jenkins.jobs.get_config(JOB_NAME)
        await jenkins.jobs.reconfigure(JOB_NAME, modify_and_save_xml(res, NEW_CONFIG_FILE))
    finally:
        jenkins.close()

if __name__ == '__main__':
    asyncio.run(func())