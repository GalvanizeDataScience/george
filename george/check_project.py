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

def suite():
    _suite = TestSuite()
    add_test(_suite, test_has_data_submodule)
    add_test(_suite, test_has_gitignore)
    return _suite

def main():
    TextTestRunner(verbosity=2).run(suite())
