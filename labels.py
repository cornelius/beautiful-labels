import yaml

class Labels:
    def __init__(self, org, repo):
        self.org = org
        self.repo = repo
        self.categories = {}

    def add_label(self, category, label_id, name, description, color):
        if not category in self.categories:
            self.categories[category] = []
        self.categories[category].append({"id": label_id, "name": name, "description": description, "color": color})

    def all_categories(self):
        return self.categories.keys()

    def labels_for_category(self, category):
        return self.categories[category]

    def save(self, filename):
        yaml_data = []
        for category in self.all_categories():
            category_data = {'category': category, 'labels': []}
            for label in self.labels_for_category(category):
                category_data['labels'].append({
                    'id': label['id'],
                    'name': label['name'],
                    'description': label['description'],
                    'color': label['color'],
                })
            yaml_data.append(category_data)
        with open(filename, 'w') as file:
            file.write(yaml.dump(yaml_data, default_flow_style=False))
