import os
from test_main import inflation


files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
         'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']
path_of_creation = '/home/kolmilki/project/TestTaskAquarius/program/'


def test_is_there_any_files(inflation):
    for path in files:
        assert os.path.exists(f'{path_of_creation}{path}')
