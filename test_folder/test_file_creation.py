import os
from test_main import inflation
from program.main import get_absolute_path


files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
         'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']
path_of_creation = get_absolute_path()


def test_is_there_any_files(inflation):
    for path in files:
        assert os.path.exists(f'{path_of_creation}{path}')
