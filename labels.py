import yaml

class Repo:
    def __init__(self):
        self.categories = {}
        self.category_names = []

    def all_categories(self):
        return self.category_names

    def labels_for_category(self, category):
        return self.categories[category]

    def add_label(self, category, label_id, name, description, color):
        if not category in self.categories:
            self.categories[category] = []
            self.category_names.append(category)
        self.categories[category].append({"id": label_id, "name": name, "description": description, "color": color})

    def parse(self, yaml_data):
        self.repo = yaml_data["repo"]
        for category in yaml_data["categories"]:
            category_name = category["name"]
            if "color" in category:
                category_color = category["color"]
            else:
                category_color = "ffffff"
            for label in category["labels"]:
                if "color" in label:
                    color = label["color"]
                else:
                    color = category_color
                self.add_label(category_name, label["id"], label["name"], label["description"], color)

class Labels:
    def __init__(self):
        self.categories = {}
        self.category_names = []
        self.remote_state_org = ""
        self.remote_state_workspace = "beautiful-labels"
        self.__repos = []

    def repos(self):
        return self.__repos

    def add_repo(self, repo):
        self.__repos.append(repo)

    def repo(self, name):
        for repo in self.__repos:
            if repo.repo == name:
                return repo
        return None

    def save(self, filename):
        yaml_data = {'org': self.org, 'repos': []}
        for repo in self.repos():
            repo_data = {'categories': []}
            for category in repo.all_categories():
                category_data = {'name': category, 'labels': []}
                for label in repo.labels_for_category(category):
                    category_data['labels'].append({
                        'id': label['id'],
                        'name': label['name'],
                        'description': label['description'],
                        'color': label['color'],
                    })
                repo_data['categories'].append(category_data)
            repo_data['repo'] = repo.repo
            yaml_data['repos'].append(repo_data)
        with open(filename, 'w') as file:
            file.write(yaml.dump(yaml_data, default_flow_style=False))

    def load(self, filename):
        with open(filename) as file:
            yaml_data = yaml.full_load(file)
        self.org = yaml_data["org"]
        if "remote_state" in yaml_data:
            if "org" in yaml_data["remote_state"]:
                self.remote_state_org = yaml_data["remote_state"]["org"]
            if "workspace" in yaml_data["remote_state"]:
                self.remote_state_workspace = yaml_data["remote_state"]["workspace"]
        if "repos" in yaml_data:
            for yaml_repo in yaml_data["repos"]:
                repo = Repo()
                repo.parse(yaml_repo)
                self.__repos.append(repo)
        else:
            repo = Repo()
            repo.parse(yaml_data)
            self.__repos.append(repo)

    def show(self):
        print(self.as_text(), end='')

    def as_text(self):
        out = ""
        out += "# GitHub Labels\n"
        if self.remote_state_org:
            out += "Terraform remote state at %s/%s\n" % (self.remote_state_org, self.remote_state_workspace)
        for repo in self.repos():
            out += "\n## Repo '%s/%s'\n" % (self.org, repo.repo)
            for category in repo.all_categories():
                out += "\n### %s\n\n" % category
                for label in repo.labels_for_category(category):
                    out += "* %s" % label["name"]
                    if label["description"]:
                        out += " (%s)" % label["description"]
                    out += " [#%s]\n" % label["color"]
        return out
