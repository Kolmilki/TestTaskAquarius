from test_task import file_creation
import os


def test_is_there_any_files():
    file_creation()
    assert os.path.exists('a.txt')
    assert os.path.exists('b.txt')
    assert os.path.exists('c.txt')
