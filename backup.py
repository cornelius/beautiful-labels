import requests
import os
from graphql import Query
import json

def get_issues_with_labels(org, repo, after=None):
    if not "GITHUB_TOKEN" in os.environ or not os.environ["GITHUB_TOKEN"]:
        os.sys.exit("Environment variable GITHUB_TOKEN needs to be set to a GitHub authentication token")

    q = Query()
    with q.field("repository", 'owner: "%s", name: "%s"' % (org, repo)):
        args = "first: 50"
        if after:
            args += ' after: "%s"' % after
        with q.field("issues", args):
            with q.field("nodes"):
                q.field("number")
                q.field("title")
                with q.field("labels", "first: 20"):
                    with q.field("nodes"):
                        q.field("name")
            with q.field("pageInfo"):
                q.field("hasNextPage")
                q.field("endCursor")

    headers = {"Authorization": "bearer " + os.environ["GITHUB_TOKEN"]}
    r = requests.post("https://api.github.com/graphql", headers=headers, json=q.json())

    return r.json()["data"]

def parse_response(json_response):
    issues = []
    for issue_node in json_response["repository"]["issues"]["nodes"]:
        issue = {
            "number": issue_node["number"],
            "title": issue_node["title"],
            "labels": [],
        }
        for label_node in issue_node["labels"]["nodes"]:
            issue["labels"].append(label_node["name"])
        issues.append(issue)
    return issues

def save(org, repo, filename):
    json_response = get_issues_with_labels(org, repo)
    issues = parse_response(json_response)
    while(json_response["repository"]["issues"]["pageInfo"]["hasNextPage"] == True):
        cursor = json_response["repository"]["issues"]["pageInfo"]["endCursor"]
        json_response = get_issues_with_labels(org, repo, after=cursor)
        issues += parse_response(json_response)
    print(issues)
    with open(filename, "w") as file:
        file.write(json.dumps(issues, indent=2, sort_keys=True))
