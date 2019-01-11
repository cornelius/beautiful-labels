import subprocess
from shutil import copyfile
import pytest
import yaml

class CmdError(Exception):
    pass

def run_cmd(arg_line):
    cmd = ["./beautiful-labels"] + arg_line.split(" ")
    print(cmd)
    completed = subprocess.call(cmd)
    if completed != 0:
        raise CmdError("Error running cmd %s" %cmd)

def test_unknown_command():
    with pytest.raises(CmdError):
        run_cmd("xxx someorg somerepo somedir")

def test_write_config(tmp_path):
    copyfile("test_data/structured-labels.yaml", str(tmp_path / "someorg-somerepo-labels.yaml"))
    run_cmd("write-config someorg somerepo " + str(tmp_path))

    actual_file = tmp_path / 'someorg-somerepo-labels.tf'
    with open('test_data/structured-labels.tf') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()

def test_scan(tmp_path):
    copyfile("test_data/labels.json", str(tmp_path / "someorg-somerepo-labels.json"))
    run_cmd("scan someorg somerepo " + str(tmp_path))

    actual_file = tmp_path / 'someorg-somerepo-labels.yaml'
    with open(str(actual_file)) as file:
        actual_data = yaml.load(file)
    with open('test_data/labels.yaml') as file:
        expected_data = yaml.load(file)
    assert actual_data == expected_data

def test_create_svg(tmp_path):
    copyfile("test_data/structured-labels.yaml", str(tmp_path / "someorg-somerepo-labels.yaml"))
    run_cmd("create-svg someorg somerepo " + str(tmp_path) + " --label-font-size=15")

    actual_file = tmp_path / 'someorg-somerepo-labels.svg'
    with open('test_data/structured-labels.svg') as expected_file:
        with open(str(actual_file)) as actual_file:
            assert actual_file.read() == expected_file.read()
