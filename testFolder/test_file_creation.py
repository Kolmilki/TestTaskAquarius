import os
import sys
sys.path.insert(0, '/home/kolmilki/project/TestTaskAquarius/program')
from file_creation import create_files


files = ['a.txt', 'b.txt', 'c.txt', 'fileDirectoryDE/d.txt', 'fileDirectoryDE/e.txt', 'fileDirectoryFGH/f.txt',
         'fileDirectoryFGH/g.txt', 'fileDirectoryFGH/h.txt']


def test_is_there_any_files():
    create_files()
    for path in files:
        assert os.path.exists(path)
        os.remove(path)
    os.removedirs('fileDirectoryDE/')
    os.removedirs('fileDirectoryFGH/')
