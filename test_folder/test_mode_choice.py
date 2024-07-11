import os
import pytest
from test_main import inflation
from program.mode_choice import dir_works
from program.mode_choice import file_works
from program.main import get_absolute_path


@pytest.mark.parametrize(
    "path, first_index, second_index, expectation",
    [
        ([f"{get_absolute_path()}fileDirectoryFGH"], 1, 3.5, pytest.raises(TypeError)),
        ([f"{get_absolute_path()}fileDirectoryFGH"], "n", 1, pytest.raises(TypeError)),
        ([f"{get_absolute_path()}fileDirectoryDE"], 1, "1", pytest.raises(TypeError)),
        ([f"{get_absolute_path()}fileDE"], 1, 1, pytest.raises(FileNotFoundError)),
    ],
)
def test_if_dir_raises_exception(
    inflation, path, first_index, second_index, expectation
):
    assert os.path.exists(f"{get_absolute_path()}data.json")
    with expectation:
        dir_works(path, first_index, second_index)


@pytest.mark.parametrize(
    "path, first_index, second_index, expectation",
    [
        (
            [
                f"{get_absolute_path()}c.txt",
                f"{get_absolute_path()}b.txt",
                f"{get_absolute_path()}a.txt",
            ],
            1,
            3.5,
            pytest.raises(TypeError),
        ),
        (
            [
                f"{get_absolute_path()}fileDirectoryFGH/h.txt",
                f"{get_absolute_path()}fileDirectoryFGH/f.txt",
            ],
            "n",
            1,
            pytest.raises(TypeError),
        ),
        (
            [
                f"{get_absolute_path()}fileDirectoryFGH/g.txt",
                f"{get_absolute_path()}a.txt",
            ],
            1,
            "1",
            pytest.raises(TypeError),
        ),
        (
            [
                f"{get_absolute_path()}fileDirectory/g.txt",
                f"{get_absolute_path()}a.txt",
            ],
            1,
            "1",
            pytest.raises(FileNotFoundError),
        ),
    ],
)
def test_how_file_mode_works(inflation, path, first_index, second_index, expectation):
    assert os.path.exists(f"{get_absolute_path()}data.json")
    with expectation:
        file_works(path, first_index, second_index)
