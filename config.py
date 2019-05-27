from pathlib import Path
import datetime

def now():
    return datetime.datetime.now()

def json_filename(output_file):
    if not output_file.endswith(".yaml"):
        raise RuntimeError("Error: Expected output file to end with '.yaml'")
    return output_file.replace(".yaml", ".json")

def backup_filename(output_directory, org, repo, kind):
    return str(Path(output_directory) / (org + '-' + repo + '-backup-labels-'
        + kind + '.' + now().strftime("%Y%m%dT%H%M%S") + ".json"))
