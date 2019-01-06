from pathlib import Path

class Config:
    def __init__(self, dir, org, repo):
        self.working_dir = dir
        self.org = org
        self.repo = repo

    def filename(self, extension):
        return str(Path(self.working_dir) / (self.org + '-' + self.repo + '-labels.' + extension))

    def yaml_filename(self):
        return self.filename('yaml')

    def terraform_filename(self):
        return self.filename('tf')

    def json_filename(self):
        return self.filename('json')

    def svg_filename(self):
        return self.filename('svg')
