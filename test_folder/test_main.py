import os
from program.main import get_answer
from program.main import get_indexes
from program.main import get_configuration_setting
from program.main import get_config_file_name


def test_is_input_correct():
    assert get_answer()


def test_are_indexes_correct():
    indexes = get_indexes()
    first_index = indexes[0]
    second_index = indexes[1]
    assert first_index.is_integer()
    assert second_index.is_integer()
    assert first_index != 0 and second_index != 0


def test_is_config_number_correct():
    config_number = get_configuration_setting()
    assert config_number.is_integer()
    assert config_number != 0


def test_is_config_file_correct():
    configuration_file = get_config_file_name()
    assert os.path.exists(configuration_file)
    assert configuration_file.endswith('.txt') or configuration_file.endswith('.csv')
