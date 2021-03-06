import subprocess
from subprocess import CalledProcessError, PIPE
from shutil import copyfile
import pytest
import yaml
from pathlib import Path
import os

def run_cmd(arg_line):
    cmd = ["./beautiful-labels"] + arg_line.split(" ")
    print(cmd)
    subprocess.check_output(cmd, stderr=PIPE)

def test_unknown_command():
    with pytest.raises(CalledProcessError):
        run_cmd("xxx someorg somerepo somedir")

def test_write_config(tmp_path):
    config_file = Path("test_data", "structured-labels.yaml")
    output_file = tmp_path / "config.tf"
    expected_file = Path("test_data", "config.tf")

    run_cmd("write-config %s -o %s" % (str(config_file), str(output_file)))

    with open('test_data/structured-labels.tf') as expected_file:
        with output_file.open() as actual_file:
            assert actual_file.read() == expected_file.read()

def test_scan(tmp_path):
    json_file = tmp_path / "labels.json"
    config_file = tmp_path / "labels.yaml"
    expected_file = Path("test_data", "labels.yaml")

    copyfile("test_data/labels.json", json_file)

    run_cmd("scan someorg somerepo -o %s" % str(config_file))

    with config_file.open() as file:
        actual_data = yaml.full_load(file)
    with expected_file.open() as file:
        expected_data = yaml.full_load(file)
    assert actual_data == expected_data

def test_create_svg(tmp_path):
    config_file = Path("test_data", "structured-labels.yaml")
    output_file = tmp_path / "config.svg"
    expected_file = Path("test_data", "structured-labels.svg")

    run_cmd("create-svg %s somerepo -o %s --label-font-size=15" % (config_file, output_file))

    with expected_file.open() as expected:
        with output_file.open() as actual:
            assert actual.read() == expected.read()

def test_save_backup():
    config_file = Path("test_data", "multi-repo-labels.yaml")
    repo = "doesnotexist"

    os.environ["GITHUB_TOKEN"] = "xxx"
    with pytest.raises(CalledProcessError) as e:
        run_cmd("save-backup %s %s /tmp" % (config_file, repo))

    output = e.value.stderr.decode('utf-8')
    assert "Unknown repo 'doesnotexist'" in output
