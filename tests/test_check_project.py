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
    open('.gitignore', 'w').write('')
    n.assert_raises(AssertionError, check_project.test_has_gitignore)
    open('.gitignore', 'w').write('*.pyc')
    n.assert_raises(AssertionError, check_project.test_has_gitignore)
    open('.gitignore', 'w').write('*.pyc\n.urchin.log')
    check_project.test_has_gitignore()
