import subprocess
import json
from pathlib import Path
import yaml

def scan_labels(org, repo):
    print("Scanning labels of GitHub repository '%s/%s'..." % (org, repo))

    json_filename = org + '-' + repo + '-labels.json'

    json_data = ''
    if Path(json_filename).exists():
      with open(json_filename, 'r') as file:
        json_data = file.read()
    else:
      json_data = subprocess.check_output(['curl', '-s', '-H "Accept: application/vnd.github.symmetra-preview+json"',
            'https://api.github.com/repos/' + org + '/' + repo + '/labels']).decode('utf-8')
      with open(json_filename, 'w') as file:
        file.write(json_data)

    labels = json.loads(json_data)

    for label in labels:
        print(label['name'])
        print("  " + label['description'])
        print("  " + label['color'])

    return labels

def write_yaml(labels, filename):
    category = []
    for label in labels:
        category.append({
          'id': label['id'],
          'name': label['name'],
          'description': label['description'],
          'color': label['color'],
    })
    yaml_data = {'general': category}
    with open(filename, 'w') as file:
        file.write(yaml.dump(yaml_data, default_flow_style=False))
