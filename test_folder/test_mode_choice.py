import pytest
import os
from program.mode_choice import dir_works
from program.mode_choice import file_works
from test_main import inflation
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    'path, first_index, second_index, expectation',
    [
        (['/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryFGH'], 1, 3.5, pytest.raises(TypeError)),
        (['/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryFGH'], 'n', 1, pytest.raises(TypeError)),
        (['/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryDE'], 1, '1', pytest.raises(TypeError)),
    ]
)
def test_if_dir_raises_exception(inflation, path, first_index, second_index, expectation):
    assert os.path.exists('/home/kolmilki/project/TestTaskAquarius/program/data.json')
    with expectation:
        dir_works(path, first_index, second_index)


@pytest.mark.parametrize(
    'path, first_index, second_index, expectation',
    [
        (['/home/kolmilki/project/TestTaskAquarius/program/c.txt',
          '/home/kolmilki/project/TestTaskAquarius/program/b.txt',
          '/home/kolmilki/project/TestTaskAquarius/program/a.txt'], 1, 3.5, pytest.raises(TypeError)),
        (['/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryFGH/h.txt',
          '/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryFGH/f.txt'], 'n', 1, pytest.raises(TypeError)),
        (['/home/kolmilki/project/TestTaskAquarius/program/fileDirectoryFGH/g.txt',
          '/home/kolmilki/project/TestTaskAquarius/program/a.txt'], 1, '1', pytest.raises(TypeError)),
    ]
)
def test_how_file_mode_works(inflation, path, first_index, second_index, expectation):
    assert os.path.exists('/home/kolmilki/project/TestTaskAquarius/program/data.json')
    with expectation:
        file_works(path, first_index, second_index)
