import json
from scanner import write_yaml

def test_write_yaml(tmp_path):
    with open('test_data/labels.json') as file:
      labels = json.loads(file.read())
    actual_file = tmp_path / 'labels.yaml'
    write_yaml(labels, str(actual_file))
    with open('test_data/labels.yaml') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
