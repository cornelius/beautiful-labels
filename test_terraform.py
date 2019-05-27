from terraform import write_terraform_config
from labels import Labels

def assert_write_config(tmp_path, name):
    labels = Labels()
    labels.load('test_data/%s.yaml' % name)
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config(labels, str(actual_file))
    with open('test_data/%s.tf' % name) as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()

def test_write_config(tmp_path):
    for name in ["labels", "structured-labels", "remote-state-labels"]:
        assert_write_config(tmp_path, name)

def test_write_terraform_config(tmp_path):
    labels = Labels()
    labels.load('test_data/labels.yaml')
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config(labels, str(actual_file))
    with open('test_data/labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()

def test_write_structured_terraform_config(tmp_path):
    labels = Labels()
    labels.load('test_data/structured-labels.yaml')
    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    write_terraform_config(labels, str(actual_file))
    with open('test_data/structured-labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
