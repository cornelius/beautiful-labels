from graphql import Query

def test_empty_query():
    q = Query()
    assert q.json() == {"query": "query {\n}\n"}

def test_full_query():
    q = Query()
    with q.field("repository", 'owner: "cornelius", name: "gittest"'):
        with q.field("issues", "first: 5"):
            with q.field("nodes"):
                q.field("number")
                q.field("title")
                with q.field("labels", "first: 20"):
                    with q.field("nodes"):
                        q.field("name")
            with q.field("pageInfo"):
                q.field("hasNextPage")
                q.field("endCursor")

    print(q.out)

    expected_json = { "query": """query {
  repository(owner: "cornelius", name: "gittest") {
    issues(first: 5) {
      nodes {
        number
        title
        labels(first: 20) {
          nodes {
            name
          }
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
}
"""}

    assert q.json() == expected_json
