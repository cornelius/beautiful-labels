import yaml

class Labels:
    def __init__(self, org, repo):
        self.org = org
        self.repo = repo
        self.categories = {}
        self.category_names = []

    def add_label(self, category, label_id, name, description, color):
        if not category in self.categories:
            self.categories[category] = []
            self.category_names.append(category)
        self.categories[category].append({"id": label_id, "name": name, "description": description, "color": color})

    def all_categories(self):
        return self.category_names

    def labels_for_category(self, category):
        return self.categories[category]

    def save(self, filename):
        yaml_data = {'org': self.org, 'repo': self.repo, 'categories': []}
        for category in self.all_categories():
            category_data = {'name': category, 'labels': []}
            for label in self.labels_for_category(category):
                category_data['labels'].append({
                    'id': label['id'],
                    'name': label['name'],
                    'description': label['description'],
                    'color': label['color'],
                })
            yaml_data['categories'].append(category_data)
        with open(filename, 'w') as file:
            file.write(yaml.dump(yaml_data, default_flow_style=False))

    def load(self, filename):
        with open(filename) as file:
            yaml_data = yaml.full_load(file)
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
