from labels import Labels

def write_terraform_config(labels, filename):
    print("Writing Terraform config...")

    with open(filename, "w") as file:
        file.write("variable \"github_token\" {}\n")
        file.write("\n")
        file.write("provider \"github\" {\n")
        file.write("  organization = \"%s\"\n" % labels.org)
        file.write("  token = \"${var.github_token}\"\n")
        file.write("}\n")
        for category in labels.all_categories():
            print("  Category '%s'" % category)
            for label in labels.labels_for_category(category):
                label_id = label["id"]
                file.write("\n")
                file.write("resource \"github_issue_label\" \"%s\" {\n" % label_id)
                file.write("  repository  = \"%s\"\n" % labels.repo)
                file.write("  name        = \"%s\"\n" % label["name"])
                file.write("  description = \"%s\"\n" % label["description"])
                file.write("  color       = \"%s\"\n" % label["color"])
                file.write("}\n")
