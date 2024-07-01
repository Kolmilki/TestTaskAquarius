import os
import pytest
from program.main import get_absolute_path
from program.main import get_answer
from program.main import check_users_input
from program.main import get_configuration_setting
from program.main import get_config_file_name
from program.file_creation import create_files
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
    'first_index, second_index, expectation',
    [
        (1, 1, does_not_raise()),
        (13, 2, does_not_raise()),
        (2, 4, does_not_raise()),
        (0, 1, pytest.raises(AssertionError)),
        ('n', 1, pytest.raises(AttributeError)),
        (1, '1', pytest.raises(AttributeError)),
        (99, '1', pytest.raises(AttributeError)),
    ]
)
def test_are_indexes_correct(first_index, second_index, expectation):
    check_users_input(first_index, second_index)
    with expectation:
        assert first_index.is_integer()
        assert second_index.is_integer()
        assert first_index != 0 and second_index != 0
        assert first_index > 0 and second_index > 0


@pytest.mark.parametrize(
    'number, expectation',
    [
        (1, does_not_raise()),
        (5, does_not_raise()),
        (0, pytest.raises(AssertionError)),
        ('n', pytest.raises(AttributeError)),
        (-1, pytest.raises(AssertionError)),
        # (99, pytest.raises(AttributeError)),
    ]
)
def test_is_config_number_correct(number, expectation):
    config_number = get_configuration_setting(number)
    with expectation:
        assert config_number.is_integer()
        assert config_number > 0
        assert config_number != 0


@pytest.mark.parametrize(
    'answer, expectation',
    [
        ('config.txt', does_not_raise()),
        ('dfdsf.csv', pytest.raises(AssertionError)),
        ('asdsa.txt', pytest.raises(AssertionError)),
        ('config', pytest.raises(AssertionError)),
    ]
)
def test_is_config_file_correct(inflation, answer, expectation):
    configuration_file = get_config_file_name(answer)
    with expectation:
        assert os.path.exists(f'{get_absolute_path()}{configuration_file}')
        assert configuration_file.endswith('.txt') or configuration_file.endswith('.csv')
