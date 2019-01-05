from terraform import write_terraform_config
from labels import Labels

def test_write_terraform_config(tmp_path):
    labels = Labels("someorg", "somerepo")
    labels.load('test_data/labels.yaml')
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config(labels, str(actual_file))
    with open('test_data/labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()

def test_write_structured_terraform_config(tmp_path):
    labels = Labels("someorg", "somerepo")
    labels.load('test_data/structured-labels.yaml')
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config(labels, str(actual_file))
    with open('test_data/structured-labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
