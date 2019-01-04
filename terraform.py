def write_terraform_config(org, repo, labels, filename):
    print("Writing Terraform config...")

    with open(filename, "w") as file:
        file.write("variable \"github_token\" {}\n")
        file.write("\n")
        file.write("provider \"github\" {\n")
        file.write("  organization = \"%s\"\n" % org)
        file.write("  token = \"${var.github_token}\"\n")
        file.write("}\n")
        for category in labels:
            for label in labels[category]:
                id = label["id"]
                file.write("\n")
                file.write("resource \"github_issue_label\" \"%s\" {\n" % id)
                file.write("  repository  = \"%s\"\n" % repo)
                file.write("  name        = \"%s\"\n" % label["name"])
                file.write("  description = \"%s\"\n" % label["description"])
                file.write("  color       = \"%s\"\n" % label["color"])
                file.write("}\n")
