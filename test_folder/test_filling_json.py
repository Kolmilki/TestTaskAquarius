import os
import json
import pytest
from test_main import inflation
from program.main import get_absolute_path
from program.filling_json import choosing_mode
from program.filling_json import forming_json_file
from contextlib import nullcontext as does_not_raise


pathOS = get_absolute_path()


@pytest.mark.parametrize(
    "config, setting, mode, path, expectation",
    [
        ("config.txt", 3, "dir", f"{pathOS}fileDirectoryDE", does_not_raise()),
        (
            "config.txt",
            2,
            "files",
            [f"{pathOS}c.txt", f"{pathOS}b.txt", f"{pathOS}a.txt"],
            does_not_raise(),
        ),
        (
            "config.txt",
            3,
            "jpg",
            f"{pathOS}fileDirectoryDE",
            pytest.raises(AssertionError),
        ),
        (
            "config.tft",
            3,
            "files",
            f"{pathOS}fileDirectoryDE",
            pytest.raises(AssertionError),
        ),
    ],
)
def test_forming_json_file(inflation, config, setting, mode, path, expectation):
    forming_json_file(config, setting, mode, path)
    with open(f"{pathOS}data.json", encoding="UTF-8") as json_file:
        config_data = json.load(json_file)
        assert os.path.exists(f"{pathOS}/data.json")
        with expectation:
            assert config_data.get("configFile").endswith((".txt", ".csv"))
            assert config_data.get("configurationData").get("mode") in ["dir", "files"]
