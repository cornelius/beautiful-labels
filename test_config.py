from config import Config

def test_yaml_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.yaml_filename() == "some/dir/someorg-somerepo-labels.yaml"

def test_terraform_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.terraform_filename() == "some/dir/someorg-somerepo-labels.tf"

