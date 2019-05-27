import datetime

from config import Config

def test_yaml_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.yaml_filename() == "some/dir/someorg-somerepo-labels.yaml"

def test_terraform_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.terraform_filename() == "some/dir/someorg-somerepo-labels.tf"

def test_json_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.json_filename() == "some/dir/someorg-somerepo-labels.json"

def test_svg_filename():
    config = Config("some/dir", "someorg", "somerepo")
    assert config.svg_filename() == "some/dir/someorg-somerepo-labels.svg"

def test_backup_filename(mocker):
    config = Config("some/dir", "someorg", "somerepo")
    with mocker.patch('config.now', return_value=datetime.datetime(2018, 12, 24, 18, 55, 42)):
        assert config.backup_filename("issues") == "some/dir/someorg-somerepo-backup-labels-issues.20181224T185542.json"
