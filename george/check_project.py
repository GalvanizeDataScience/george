import nose.tools as n
import os
from unittest import TestSuite, TextTestRunner

from _helpers import add_test

def test_has_data_submodule():
    'The sprint should have a submodule called "data".'
    n.assert_true(os.path.isdir('data'))
    n.assert_true(os.path.isfile(os.path.join('data', '.git')))

def test_has_gitignore():
    n.assert_true(os.path.isfile('.gitignore'))
    gitignore = open('.gitignore').read()
    for pattern in ['*.pyc', '.urchin.log']:
        n.assert_in(pattern, gitignore)

def test_has_license():
    n.assert_true(os.path.isfile('LICENSE'))
    license = open('LICENSE').read()
    n.assert_in('BSD', license)

def suite():
    _suite = TestSuite()
    add_test(_suite, test_has_data_submodule)
    add_test(_suite, test_has_gitignore)
    return _suite

def main():
    TextTestRunner(verbosity=2).run(suite())
