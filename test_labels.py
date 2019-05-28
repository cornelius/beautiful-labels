import yaml

from labels import Labels, Repo

def test_save(tmp_path):
    labels = Labels()
    labels.org = "someorg"
    repo = Repo()
    repo.repo = "somerepo"
    repo.add_label("scanned", "another_label", "another label", "", "EE7912")
    repo.add_label("scanned", "bug", "bug", "Something isn't working", "d73a4a")
    repo.add_label("scanned", "common_issue", "common issue", "Label used across repositories", "333333")
    labels.add_repo(repo)

    actual_file = tmp_path / 'labels.yaml'
    labels.save(str(actual_file))
    with open('test_data/written-labels.yaml') as expected_file:
        with open(str(actual_file)) as actual_file:
            actual_data = actual_file.read()
            print(actual_data)
            assert actual_data == expected_file.read()

def test_equivalence_of_written_and_test_data():
    with open('test_data/written-labels.yaml') as file:
        written_data = yaml.full_load(file)
    with open('test_data/labels.yaml') as file:
        test_data = yaml.full_load(file)
    assert written_data == test_data

def test_load():
    labels = Labels()
    labels.load('test_data/labels.yaml')
    repo = labels.repo("somerepo")

    assert len(repo.labels_for_category("scanned")) == 3

    label = repo.labels_for_category("scanned")[0]
    assert label["name"] == "another label"
    assert label["description"] == ""
    assert label["color"] == "EE7912"

    label = repo.labels_for_category("scanned")[1]
    assert label["name"] == "bug"
    assert label["description"] == "Something isn't working"
    assert label["color"] == "d73a4a"

def test_structured_load():
    labels = Labels()
    labels.load('test_data/structured-labels.yaml')
    repo = labels.repo("somerepo")

    assert len(repo.labels_for_category("Type")) == 1
    assert len(repo.labels_for_category("Components")) == 2

    label = repo.labels_for_category("Components")[0]
    assert label["name"] == "frontend"
    assert label["color"] == "dddddd"

    label = repo.labels_for_category("Components")[1]
    assert label["name"] == "backend"
    assert label["color"] == "123456"

def test_multi_repo_load():
    labels = Labels()
    labels.load('test_data/multi-repo-labels.yaml')

    repos = labels.repos()
    assert len(repos) == 2

    repo0 = repos[0]
    assert repo0.all_categories() == ["Type"]
    assert len(repo0.labels_for_category("Type")) == 2
    assert repo0.labels_for_category("Type")[0]["name"] == "bug"

    repo1 = repos[1]
    assert repo1.category_names == ["Type", "Welcome"]
    assert len(repo1.labels_for_category("Type")) == 1

def test_remote_state_load():
    labels = Labels()
    labels.load('test_data/remote-state-labels.yaml')

    assert labels.remote_state_org == "someterraformorg"
    assert labels.remote_state_workspace == "someworkspace"

def test_as_text_structured():
    labels = Labels()
    labels.load('test_data/structured-labels.yaml')
    expected = '''# GitHub Labels

## Repo 'someorg/somerepo'

### Type

* bug (Something isn't working) [#d73a4a]

### Components

* frontend (Frontend) [#dddddd]
* backend (Backend and database) [#123456]
'''
    assert labels.as_text() == expected

def test_as_text_multi_repo():
    labels = Labels()
    labels.load('test_data/multi-repo-labels.yaml')
    expected = '''# GitHub Labels
Terraform remote state at someterraformorg/beautiful-labels

## Repo 'someorg/somerepo'

### Type

* bug (Something isn't working) [#d73a4a]
* feature (New feature) [#a2eeef]

## Repo 'someorg/anotherrepo'

### Type

* bug (Something isn't working) [#d73a4a]

### Welcome

* good first issue (Good for newcomers) [#7057ff]
'''
    assert labels.as_text() == expected


def test_repo():
    labels = Labels()
    labels.load('test_data/multi-repo-labels.yaml')
    assert not labels.repo("xxx")
    assert labels.repo("somerepo")
    assert labels.repo("anotherrepo")
