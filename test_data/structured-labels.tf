variable "github_token" {}

provider "github" {
  organization = "someorg"
  token = "${var.github_token}"
}

resource "github_issue_label" "1166740325" {
  repository  = "somerepo"
  name        = "frontend"
  description = "Frontend"
  color       = "EE7912"
}

resource "github_issue_label" "1167038964" {
  repository  = "somerepo"
  name        = "backend"
  description = "Backend and database"
  color       = "123456"
}

resource "github_issue_label" "1097075204" {
  repository  = "somerepo"
  name        = "bug"
  description = "Something isn't working"
  color       = "d73a4a"
}
