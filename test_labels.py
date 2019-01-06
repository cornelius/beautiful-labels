import yaml

from labels import Labels

def test_save(tmp_path):
    labels = Labels("someorg", "somerepo")
    labels.add_label("scanned", 1166740325, "another label", "", "EE7912")
    labels.add_label("scanned", 1097075204, "bug", "Something isn't working", "d73a4a")
    labels.add_label("scanned", 1167038964, "common issue", "Label used across repositories", "333333")

    actual_file = tmp_path / 'labels.yaml'
    labels.save(str(actual_file))
    with open('test_data/written-labels.yaml') as expected_file:
        with open(str(actual_file)) as actual_file:
            actual_data = actual_file.read()
            print(actual_data)
            assert actual_data == expected_file.read()

def test_equivalence_of_written_and_test_data():
    with open('test_data/written-labels.yaml') as file:
        written_data = yaml.load(file)
    with open('test_data/labels.yaml') as file:
        test_data = yaml.load(file)
    assert written_data == test_data

def test_load():
    labels = Labels("someorg", "somerepo")
    labels.load('test_data/labels.yaml')

    assert len(labels.labels_for_category("scanned")) == 3

    label = labels.labels_for_category("scanned")[0]
    assert label["name"] == "another label"
    assert label["description"] == ""
    assert label["color"] == "EE7912"

    label = labels.labels_for_category("scanned")[1]
    assert label["name"] == "bug"
    assert label["description"] == "Something isn't working"
    assert label["color"] == "d73a4a"

def test_structured_load():
    labels = Labels("someorg", "somerepo")
    labels.load('test_data/structured-labels.yaml')

    assert len(labels.labels_for_category("Type")) == 1
    assert len(labels.labels_for_category("Components")) == 2

    label = labels.labels_for_category("Components")[0]
    assert label["name"] == "frontend"
    assert label["color"] == "EE7912"

    label = labels.labels_for_category("Components")[1]
    assert label["name"] == "backend"
    assert label["color"] == "123456"