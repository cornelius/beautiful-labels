terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "someterraformorg"

    workspaces {
      name = "beautiful-labels"
    }
  }
}

variable "github_token" {}

provider "github" {
  organization = "someorg"
  token = "${var.github_token}"
}

resource "github_issue_label" "someorg_somerepo_bug" {
  repository  = "somerepo"
  name        = "bug"
  description = "Something isn't working"
  color       = "d73a4a"
}

resource "github_issue_label" "someorg_somerepo_enhancement" {
  repository  = "somerepo"
  name        = "feature"
  description = "New feature"
  color       = "a2eeef"
}

resource "github_issue_label" "someorg_anotherrepo_bug" {
  repository  = "anotherrepo"
  name        = "bug"
  description = "Something isn't working"
  color       = "d73a4a"
}

resource "github_issue_label" "someorg_anotherrepo_good_first_issue" {
  repository  = "anotherrepo"
  name        = "good first issue"
  description = "Good for newcomers"
  color       = "7057ff"
}
