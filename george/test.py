import nose.tools as n
import os

def test_has_data_submodule():
    'The sprint should have a submodule called "data".'
    n.assert_true(os.path.isdir('data'))
    n.assert_true(os.path.isfile(os.path.join('data', '.git')))

def test_python_init():
    'If there are any python files in the code directory, there should be an __init__.py'

def test_python_files_correspond():
    '.py files in ``code`` should correspond with test files in ``test``'
