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
