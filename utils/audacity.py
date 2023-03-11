import os
from bs4 import BeautifulSoup


# Audacity parsing functions
def find_aup_file(path):
    aup_files = [f for f in os.listdir(path) if f.endswith('.aup')]
    return aup_files[0] # Assume only one file per directory

def parse_audacity_project(path_to_aup_file):
    
    with open(path_to_aup_file, 'r') as f:
        aup = BeautifulSoup(f, features="lxml-xml")
    
    root_path = os.path.split(path_to_aup_file)[:-1]
    root_path = os.path.join(*root_path)

    project = aup.find('project')
    proj_name = project.get('projname')
    data_path = os.path.join(root_path, proj_name)

    proj_imports = project.find_all('import')
    proj_files = []
    for item in proj_imports:
        filename, offset= item.get('filename'), float(item.get('offset'))
        entry = {
            'filename': filename,
            'offset': offset
        }
        proj_files.append(entry)

    
    output = {
        'project_name' : proj_name,
        'root_path': root_path,
        'data_path': data_path,
        'files': proj_files
    }

    return output

def get_audacity_object(directory):
    project = parse_audacity_project(
        os.path.join(directory, find_aup_file(directory))
    )
    return project