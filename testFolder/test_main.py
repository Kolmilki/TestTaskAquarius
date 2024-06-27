import sys
import pytest
sys.path.insert(0, '/home/kolmilki/project/TestTaskAquarius/program')
from main import get_answer


def test_is_input_correct():
    with pytest.raises(FileNotFoundError):
        get_answer()

