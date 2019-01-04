variable "github_token" {}

provider "github" {
  organization = "cornelius"
  token = "${var.github_token}"
}

resource "github_issue_label" "1166740325" {
  repository  = "gittest"
  name        = "another label"
  description = ""
  color       = "EE7912"
}

resource "github_issue_label" "1097075204" {
  repository  = "gittest"
  name        = "bug"
  description = "Something isn't working"
  color       = "d73a4a"
}

resource "github_issue_label" "1167038964" {
  repository  = "gittest"
  name        = "common issue"
  description = "Label used across repositories"
  color       = "333333"
}

resource "github_issue_label" "1167042235" {
  repository  = "gittest"
  name        = "common-issue"
  description = "Label used across repositories"
  color       = "333333"
}

resource "github_issue_label" "1166858855" {
  repository  = "gittest"
  name        = "duplicate"
  description = "Already exists"
  color       = "1fd3d7"
}

resource "github_issue_label" "1097075206" {
  repository  = "gittest"
  name        = "enhancement"
  description = "New feature or request"
  color       = "a2eeef"
}

resource "github_issue_label" "1097075208" {
  repository  = "gittest"
  name        = "good first issue"
  description = "Good for newcomers"
  color       = "7057ff"
}

resource "github_issue_label" "1166736935" {
  repository  = "gittest"
  name        = "hello world"
  description = ""
  color       = "ba1840"
}

resource "github_issue_label" "1097075207" {
  repository  = "gittest"
  name        = "help wanted"
  description = "Extra attention is needed"
  color       = "008672"
}

resource "github_issue_label" "1167043459" {
  repository  = "gittest"
  name        = "label for all"
  description = "Label used across repositories"
  color       = "333333"
}

resource "github_issue_label" "1097075210" {
  repository  = "gittest"
  name        = "question"
  description = "Further information is requested"
  color       = "d876e3"
}

resource "github_issue_label" "1097075205" {
  repository  = "gittest"
  name        = "seen before"
  description = "Already exists"
  color       = "1fd3d7"
}

resource "github_issue_label" "1167036615" {
  repository  = "gittest"
  name        = "shared label"
  description = "Label used across repositories"
  color       = "111111"
}

resource "github_issue_label" "1166739985" {
  repository  = "gittest"
  name        = "some label"
  description = "Some description"
  color       = "EE7912"
}

resource "github_issue_label" "1097075211" {
  repository  = "gittest"
  name        = "wontfix"
  description = "This will not be worked on"
  color       = "ffffff"
}
