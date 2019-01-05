import subprocess
import json
from pathlib import Path

from labels import Labels

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

    return labels_from_json_data(json_data)

def labels_from_json_data(json_data):
    labels_json = json.loads(json_data)
    labels = Labels("", "")
    for label in labels_json:
        labels.add_label('scanned', label['id'], label['name'], label['description'], label['color'])
    return labels
