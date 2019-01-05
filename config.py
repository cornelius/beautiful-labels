from pathlib import Path

class Config:
    def __init__(self, dir, org, repo):
        self.working_dir = dir
        self.org = org
        self.repo = repo

    def yaml_filename(self):
        return str(Path(self.working_dir) / (self.org + '-' + self.repo + '-labels.yaml'))

    def terraform_filename(self):
        return str(Path(self.working_dir) / (self.org + '-' + self.repo + '-labels.tf'))

    def json_filename(self):
        return str(Path(self.working_dir) / (self.org + '-' + self.repo + '-labels.json'))
