terraform {
  backend "remote" {
    hostname = "app.terraform.io"
    organization = "someterraformorg"

    workspaces {
      name = "someworkspace"
    }
  }
}

variable "github_token" {}

provider "github" {
  organization = "someorg"
  token = "${var.github_token}"
}

resource "github_issue_label" "someorg_somerepo_another_label" {
  repository  = "somerepo"
  name        = "another label"
  description = ""
  color       = "EE7912"
}

resource "github_issue_label" "someorg_somerepo_bug" {
  repository  = "somerepo"
  name        = "bug"
  description = "Something isn't working"
  color       = "d73a4a"
}
