import os
import shutil
import nose.tools as n

from _sandbox import setup, teardown
from george import check_project

def test_test_has_data_submodule():
    n.assert_raises(AssertionError, check_project.test_has_data_submodule)
    open('.gitmodules', 'w').write('foo')
    os.mkdir('data')
    open(os.path.join('data', '.git'), 'w').write('bar')
    check_project.test_has_data_submodule()

def test_test_has_gitignore():
    n.assert_raises(AssertionError, check_project.test_has_gitignore)
    open('.gitignore', 'w').write('foo\n')
    n.assert_raises(AssertionError, check_project.test_has_gitignore)
    open('.gitignore', 'w').write('*.pyc')
    check_project.test_has_gitignore()
