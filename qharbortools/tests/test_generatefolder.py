import sys

import pandas as pd
import pytest
import ruamel.yaml


@pytest.fixture
def mock_folder_structure(tmp_path):
    # Create a mock folder structure
    root_folder = tmp_path / "root_folder"
    root_folder.mkdir()

    # Create a mock info file
    info_file = tmp_path / "info.xlsx"
    data = {
        "UserInitials": ["hvx124", "bla"],
        "UserName": ["Rasmus", "Bla Bla"],
        "SubjectID": ["B00101A", "B00102A"],
        "Team": ["Fab", "Fab"],
        "Component": ["Component1", "Component2"],
        "SubjectName": ["Subject1", "Subject2"],
        "Equipment": ["Equipment1", "Equipment2"],
        "Step": ["Step1", "Step2"],
        "SubStep": ["SubStep1", "SubStep2"],
        "ProtocolName": ["Protocol1", "Protocol2"],
        "ChipNickname": ["Chip1", "Chip2"],
        "ProjectName": ["Project1", "Project2"],
        "Station": ["Station1", "Station2"],
        "Folder": ["subfolder1", "subfolder2"],
    }

    df = pd.DataFrame(data)
    df.to_excel(info_file, index=False)

    return root_folder, info_file


@pytest.mark.skipif(
    sys.platform == "linux",
    reason="Test is not compatible with Linux one of the used libraries is not compatible with Linux",
)
def test_folderfromxl(mock_folder_structure):
    root_folder, info_file = mock_folder_structure
    from qharbortools.generatefolder import folderfromxl  # noqa: PLC0415

    # Call the function to test
    folderfromxl(root_folder, info_file)
    assert True

    # Check if the folders were created
    for ii in [1, 2]:
        folder_name = f"subfolder{ii}"
        assert (root_folder / f"B0010{ii}A" / folder_name).exists()

        # Check if the _QH_dataset_info.yaml file exists
        qh_file_path = (
            root_folder / f"B0010{ii}A" / folder_name / "_QH_dataset_info.yaml"
        )
        assert qh_file_path.exists()
        yaml = ruamel.yaml.YAML()
        with open(qh_file_path) as f:
            data = yaml.load(f)
            assert data["attributes"]["SubjectID"] == f"B0010{ii}A"
