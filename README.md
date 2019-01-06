# Beautiful Labels

GitHub labels are powerful but it's a bit of an effort to manage them consistently, especially when you have many of them. `beautiful-labels` is a tool to help with that.

It takes a YAML description of the labels and then applies that to the configuration on GitHub via the API. It uses Terraform to manage the state on GitHub which gives you all the nice features of Terraform to manage infrastructure as code.

You can check in the YAML description of your labels to your git repository and then handle it as you would handle code with version history, pull requests, diffs, etc. Managing descriptions or colors becomes as simple as editing a text file.

*Please notice: This is early code so use it with care. Especially renaming labels can be a bit tricky as GitHub uses the name of the label as identifier. I would recommend to do renaming manually in the GitHub UI for now.*

## How to use `beautiful-labels`

The general workflow is as follows:

1) Scan labels from the GitHub repo do get an initial YAML description:

        beautiful-labels scan <org> <repo> <working-directory>

   You are free to use any working directory you want. One option is to put it into a `.github/labels` repo, so you can manage the data in git as part of your repository.

2) Edit YAML and adapt it to your needs. Add categories as needed. The categories are not handled by the GitHub label functionality but can help to structure labels and group them, for example by using colors.

3) Create an SVG overview of your labels:

        beautiful-labels create-svg <org> <repo> <working-directory>

   This reads the YAML file and generates an SVG with an overview of your labels. You can link that from your contribution documentation, for example.

4) Create the Terraform configuration:

        beautiful-labels write-config <org> <repo> <working-directory>

   This generates the configuration required by Terraform to operate the GitHub API. You might want to check in the configuration and possibly the Terraform state file as well depending on how you run it. If in doubt you probably don't want to check it in.

5) Run Terraform

   Install Terraform with the package manager of your system or download it from the [Terraform download page](https://www.terraform.io/downloads.html). Then run 'terraform init' to prepare Terraform and install the required GitHub provider.

   Terraform needs a GitHub token to do changes via the API. Generate one in the GitHub API and provide it to Terraform, e.g. by setting the environment variable `TF_VAR_github_token`.

   Run `terraform apply` to apply your changes to your project on GitHub. You will get an overview of what will be changed and need to confirm it. For a dry run use `terraform plan`. It tells you what it would do without doing any changes.

## Example

Here is an example of labels managed through `beautiful-labels` from the [inqlude](https://github.com/cornelius/inqlude) repository:

![SVG example](example.svg)

## License

`beautiful-labels` is licensed under the MIT license.
