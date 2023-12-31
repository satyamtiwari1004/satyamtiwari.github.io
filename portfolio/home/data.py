import yaml
from yaml.loader import SafeLoader

def experience_data():
    with open('data/experience.yml', 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
    print(yaml_data)
    return yaml_data

def other_projects_data():
    with open('data/other-projects.yml', 'r') as f:
        yaml_data = list(yaml.full_load_all(f))
    print(yaml_data)
    return yaml_data
def skills_data():
    with open('data/skills.yml', 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
    print(yaml_data)
    return yaml_data
