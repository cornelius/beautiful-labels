import yaml
from terraform import write_terraform_config

def test_write_terraform_config(tmp_path):
    with open('test_data/labels.yaml') as file:
        labels = yaml.load(file)
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config("someorg", "somerepo", labels, str(actual_file))
    with open('test_data/labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()

def test_write_structured_terraform_config(tmp_path):
    with open('test_data/structured-labels.yaml') as file:
        labels = yaml.load(file)
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config("someorg", "somerepo", labels, str(actual_file))
    with open('test_data/structured-labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
