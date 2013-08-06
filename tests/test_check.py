import os
from george import check
import nose.tools as n

ROOT = os.getcwd()

def setup():
    os.chdir(ROOT)

def test_test_has_data_submodule():
    os.chdir(os.path.join('fixtures', 'test_has_data_submodule', 'pass'))
    check.test_has_data_submodule()

@n.nottest
def test_test_has_data_submodule():
    os.chdir(os.path.join('fixtures', 'test_has_data_submodule', 'fail'))
    n.assert_raises(AssertionError, check.test_has_data_submodule)
