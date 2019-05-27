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

resource "github_issue_label" "someorg_somerepo_frontend" {
  repository  = "somerepo"
  name        = "frontend"
  description = "Frontend"
  color       = "dddddd"
}

resource "github_issue_label" "someorg_somerepo_backend" {
  repository  = "somerepo"
  name        = "backend"
  description = "Backend and database"
  color       = "123456"
}
