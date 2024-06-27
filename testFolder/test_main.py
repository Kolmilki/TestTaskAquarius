import sys
sys.path.insert(0, '/home/kolmilki/project/TestTaskAquarius/program')
from main import getting_input


positive_answer = ['yes', 'Yes', 'y', 'Y']

def test_is_input_correct():
    answer = answer in positive_answer
    assert answer
