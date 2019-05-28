from labels import Labels

def write_terraform_config(labels, filename):
    print("Writing Terraform config...")

    with open(filename, "w") as file:
        if labels.remote_state_org:
            file.write("terraform {\n")
            file.write("  backend \"remote\" {\n")
            file.write("    hostname = \"app.terraform.io\"\n")
            file.write("    organization = \"%s\"\n" % labels.remote_state_org)
            file.write("\n")
            file.write("    workspaces {\n")
            file.write("      name = \"%s\"\n" % labels.remote_state_workspace)
            file.write("    }\n")
            file.write("  }\n")
            file.write("}\n\n")
        file.write("variable \"github_token\" {}\n")
        file.write("\n")
        file.write("provider \"github\" {\n")
        file.write("  organization = \"%s\"\n" % labels.org)
        file.write("  token = \"${var.github_token}\"\n")
        file.write("}\n")
        for repo in labels.repos():
            print("  Repo '%s/%s'" % (labels.org, repo.repo))
            for category in repo.all_categories():
                print("    Category '%s'" % category)
                for label in repo.labels_for_category(category):
                    print("      Label '%s'" % label["name"])
                    label_id = id_for_label(labels.org, repo, label)
                    file.write("\n")
                    file.write("resource \"github_issue_label\" \"%s\" {\n" % label_id)
                    file.write("  repository  = \"%s\"\n" % repo.repo)
                    file.write("  name        = \"%s\"\n" % label["name"])
                    file.write("  description = \"%s\"\n" % label["description"])
                    file.write("  color       = \"%s\"\n" % label["color"])
                    file.write("}\n")

def id_for_label(org, repo, label):
    return org + "_" + repo.repo + "_" + label["id"]
