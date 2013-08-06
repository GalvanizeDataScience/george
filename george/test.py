import nose.tools as n
import os

def test_has_data_submodule():
    n.assert_true(os.path.isdir('data'))
    n.assert_true(os.path.isfile(os.path.join('data', '.git')))
