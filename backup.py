import requests
import os
from graphql import Query
import json

def get_items_with_labels(org, repo, kind, after=None):
    if not "GITHUB_TOKEN" in os.environ or not os.environ["GITHUB_TOKEN"]:
        os.sys.exit("Environment variable GITHUB_TOKEN needs to be set to a GitHub authentication token")

    q = Query()
    with q.field("repository", 'owner: "%s", name: "%s"' % (org, repo)):
        args = "first: 50"
        if after:
            args += ' after: "%s"' % after
        with q.field(kind, args):
            with q.field("nodes"):
                q.field("number")
                q.field("title")
                q.field("state")
                with q.field("labels", "first: 20"):
                    with q.field("nodes"):
                        q.field("name")
            with q.field("pageInfo"):
                q.field("hasNextPage")
                q.field("endCursor")

    headers = {"Authorization": "bearer " + os.environ["GITHUB_TOKEN"]}
    r = requests.post("https://api.github.com/graphql", headers=headers, json=q.json())

    return r.json()["data"]

def parse_response(json_response, kind):
    items = []
    for item_node in json_response["repository"][kind]["nodes"]:
        item = {
            "number": item_node["number"],
            "title": item_node["title"],
            "state": item_node["state"],
            "labels": [],
        }
        for label_node in item_node["labels"]["nodes"]:
            item["labels"].append(label_node["name"])
        items.append(item)
    return items

def save(org, repo, config):
    save_items(org, repo, config, 'issues')
    save_items(org, repo, config, 'pullRequests')

def save_items(org, repo, config, kind):
    json_response = get_items_with_labels(org, repo, kind)
    items = parse_response(json_response, kind)
    while(json_response["repository"][kind]["pageInfo"]["hasNextPage"] == True):
        cursor = json_response["repository"]["issues"]["pageInfo"]["endCursor"]
        json_response = get_items_with_labels(org, repo, kind, after=cursor)
        items += parse_response(json_response, kind)
    filename = config.backup_filename(kind)
    with open(filename, "w") as file:
        file.write(json.dumps(items, indent=2, sort_keys=True))
    print("Saved backup to '%s'" % filename)
