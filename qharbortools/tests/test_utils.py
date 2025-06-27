import subprocess
from unittest import mock

from qharbortools.utils import (
    export_conda_environment,
    get_githash_of_current_commit,
    get_name_of_current_repo,
    git_info_to_file,
)


def test_export_conda_environment_success(tmp_path):
    file_path = tmp_path / "environment.yml"
    with mock.patch("subprocess.run") as mock_run:
        export_conda_environment(tmp_path)
        assert file_path.exists()
        mock_run.assert_called_once_with(
            ["conda", "env", "export"],
            stdout=mock.ANY,
            check=True,
            timeout=10,
        )


def test_export_conda_environment_folder_missing(tmp_path, capsys):
    missing_folder = tmp_path / "doesnotexist"
    export_conda_environment(missing_folder)
    captured = capsys.readouterr()
    assert "The specified folder path does not exist" in captured.out


def test_export_conda_environment_subprocess_error(tmp_path, capsys):
    with mock.patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(1, ["conda", "env", "export"]),
    ):
        export_conda_environment(tmp_path)
        captured = capsys.readouterr()
        assert "An error occurred while exporting the conda environment" in captured.out


def test_git_info_to_file_success(tmp_path):
    file_path = tmp_path / "git_info.txt"
    with (
        mock.patch(
            "qharbortools.utils.get_githash_of_current_commit", return_value="abc123"
        ),
        mock.patch("qharbortools.utils.get_name_of_current_repo", return_value="repo"),
    ):
        git_info_to_file(tmp_path, nameofcurrentfile="file.py")
        assert file_path.exists()
        content = file_path.read_text()
        assert "Git Hash: abc123" in content
        assert "Repository Name: repo" in content
        assert "File Name: file.py" in content


def test_git_info_to_file_no_filename(tmp_path):
    file_path = tmp_path / "git_info.txt"
    with (
        mock.patch(
            "qharbortools.utils.get_githash_of_current_commit", return_value="abc123"
        ),
        mock.patch("qharbortools.utils.get_name_of_current_repo", return_value="repo"),
    ):
        git_info_to_file(tmp_path)
        content = file_path.read_text()
        assert "File Name: Not provided" in content


def test_git_info_to_file_folder_missing(tmp_path, capsys):
    missing_folder = tmp_path / "doesnotexist"
    git_info_to_file(missing_folder)
    captured = capsys.readouterr()
    assert "does not exist" in captured.out


def test_get_githash_of_current_commit_success():
    mock_result = mock.Mock()
    mock_result.stdout = "deadbeef\n"
    with mock.patch("subprocess.run", return_value=mock_result):
        assert get_githash_of_current_commit() == "deadbeef"


def test_get_githash_of_current_commit_error(capsys):
    with mock.patch(
        "subprocess.run", side_effect=subprocess.CalledProcessError(1, "git")
    ):
        assert get_githash_of_current_commit() == ""
        captured = capsys.readouterr()
        assert "An error occurred while getting the git hash" in captured.out


def test_get_name_of_current_repo_success():
    mock_result = mock.Mock()
    mock_result.stdout = "/some/path/repo\n"
    with mock.patch("subprocess.run", return_value=mock_result):
        assert get_name_of_current_repo() == "repo"


def test_get_name_of_current_repo_error(capsys):
    with mock.patch(
        "subprocess.run", side_effect=subprocess.CalledProcessError(1, "git")
    ):
        assert get_name_of_current_repo() == ""
        captured = capsys.readouterr()
        assert "An error occurred while getting the repository name" in captured.out
