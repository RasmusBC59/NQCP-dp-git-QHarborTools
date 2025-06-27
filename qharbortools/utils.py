import subprocess
from pathlib import Path


def export_conda_environment(
    folderpath: str | Path, filename: str = "environment.yml"
) -> None:
    """Exports the current conda environment to a YAML file.

    Args:
        folderpath (str | Path): _description_. The folder where the YAML file will be saved.
        filename (str, optional): _description_. Defaults to "environment.yml".
    """
    folderpath = Path(folderpath)
    if not folderpath.exists():
        print(f"The specified folder path does not exist: {folderpath}")
        return
    filepath = folderpath / filename
    with open(filepath, "w") as f:
        try:
            subprocess.run(["conda", "env", "export"], stdout=f, check=True, timeout=10)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while exporting the conda environment: {e}")
            return
        except subprocess.TimeoutExpired as e:
            print(
                f"The subprocess has timeout while exporting the conda environment: {e}"
            )
            return


def git_info_to_file(
    folderpath: str | Path,
    filename: str = "git_info.txt",
    nameofcurrentfile: str | None = None,
) -> None:
    """Writes the current git hash and repository name to a file. Optionally includes the name of the current file.

    Args:
        folderpath (str | Path): The folder where the git info file will be saved.
        filename (str, optional): Name of the file. Defaults to "git_info.txt".
        nameofcurrentfile (str | None, optional): Name of the current file, This is a manual process. Defaults to None.
    """
    folderpath = Path(folderpath)
    if not folderpath.exists():
        print(f"The specified folder path does not exist: {folderpath}")
        return
    filepath = folderpath / filename

    githash = get_githash_of_current_commit()
    repo_name = get_name_of_current_repo()

    with open(filepath, "w") as f:
        f.write(f"Git Hash: {githash}\n")
        f.write(f"Repository Name: {repo_name}\n")
        if nameofcurrentfile:
            f.write(f"File Name: {nameofcurrentfile}\n")
        else:
            f.write("File Name: Not provided\n")


def get_githash_of_current_commit() -> str:
    """Returns the git hash of the current commit.

    Returns:
        str: The git hash of the current commit, or an empty string if an error occurs.
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            check=True,
            text=True,
            timeout=10,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while getting the git hash: {e}")
        return ""


def get_name_of_current_repo() -> str:
    """
    Returns the name of the current git repository.
    If the command fails, it returns an empty string.

    Returns:
        str: The name of the current git repository, or an empty string if an error occurs.
    """

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            check=True,
            text=True,
            timeout=10,
        )
        repo_path = result.stdout.strip()
        return Path(repo_path).name
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while getting the repository name: {e}")
        return ""
