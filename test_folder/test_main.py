import os
import json
import pytest
from program.main import get_answer
from program.main import get_absolute_path
from program.main import remove_directories
from program.file_creation import create_files
from program.main import read_configuration_file
from contextlib import nullcontext as does_not_raise


@pytest.fixture()
def inflation():
    create_files()
    yield
    files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
             'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']
    for path in files:
        os.remove(f'{get_absolute_path()}{path}')
    os.removedirs(f'{get_absolute_path()}fileDirectoryDE/')
    os.removedirs(f'{get_absolute_path()}fileDirectoryFGH/')


@pytest.fixture()
def inflation_with_no_clearing():
    create_files()


@pytest.mark.parametrize(
    'answer, expectation',
    [
        ('yes', does_not_raise()),
        ('y', does_not_raise()),
        ('Y', does_not_raise()),
        ('No', pytest.raises(AssertionError)),
        ('n', pytest.raises(AssertionError)),
        ('no', pytest.raises(AssertionError)),
        ('8', pytest.raises(AssertionError)),
    ]
)
def test_is_input_correct(inflation, answer, expectation):
    with expectation:
        assert get_answer(answer)


@pytest.mark.parametrize(
    'configuration_file, configuration_setting, expectation',
    [
        ('config.txt', 1, does_not_raise()),
        ('config.txt', 2, does_not_raise()),
        ('config', 5, pytest.raises(FileNotFoundError)),
        ('config.txt', 6, pytest.raises(ValueError)),
        ('config_for_test.txt', 1, does_not_raise()),
    ]
)
def test_read_configuration_file(inflation, configuration_file, configuration_setting, expectation):
    with expectation:
        assert read_configuration_file(configuration_file, configuration_setting)


def test_remove_files(inflation_with_no_clearing):
    files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
             'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']
    remove_directories()
    for path in files:
        if os.path.exists(f'{get_absolute_path()}{path}'):
            assert False
        else:
            assert True
