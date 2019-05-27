import datetime
import pytest

from config import backup_filename, json_filename

def test_backup_filename(mocker):
    with mocker.patch('config.now', return_value=datetime.datetime(2018, 12, 24, 18, 55, 42)):
        assert backup_filename("some/dir", "someorg", "somerepo", "issues") == "some/dir/someorg-somerepo-backup-labels-issues.20181224T185542.json"

def test_json_filename():
    assert json_filename("somefile.yaml") == "somefile.json"

    with pytest.raises(RuntimeError):
        json_filename("somefile.xyz")
