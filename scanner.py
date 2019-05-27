import subprocess
import json
from pathlib import Path
import os
import sys

from labels import Labels
from config import json_filename

def scan_labels(output_file, org, repo):
    print("Scanning labels of GitHub repository '%s/%s'..." % (org, repo))

    json_data = ''
    cache_file = json_filename(output_file)
    if Path(cache_file).exists():
        with open(cache_file, 'r') as file:
            json_data = file.read()
    else:
        command = ['curl', '-s', '-HAccept: application/vnd.github.symmetra-preview+json']
        if os.environ['GITHUB_TOKEN']:
            command += ['-HAuthorization: token %s' % os.environ['GITHUB_TOKEN']]
        command += ['https://api.github.com/repos/' + org + '/' + repo + '/labels?per_page=100']
        json_data = subprocess.check_output(command).decode('utf-8')
        with open(cache_file, 'w') as file:
            file.write(json_data)

    return labels_from_json_data(org, repo, json_data)

def labels_from_json_data(org, repo, json_data):
    labels_json = json.loads(json_data)
    if "message" in labels_json:
        sys.exit("Error retrieving labels from GitHub: " + labels_json["message"] +
                "\nIf you are accessing a private repository you need to set a GitHub token "
                "in the environment variable GITHUB_TOKEN.")
    labels = Labels()
    labels.org = org
    labels.repo = repo
    for label in labels_json:
        labels.add_label('scanned', id_from_name(label['name']), label['name'], label['description'], label['color'])
    return labels

def id_from_name(name):
    return name.replace(" ", "_")
