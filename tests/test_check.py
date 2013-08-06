import os
import shutil
import nose.tools as n
import uuid

from george import check

ROOT = os.getcwd()



def setup():
    # Make a temporary directory
    tmp = os.path.join('/', 'tmp', 'george-' + unicode(uuid.uuid1()))
    os.mkdir(tmp)
    os.chdir(tmp)

def teardown():
    tmp = os.getcwd()
    os.chdir(ROOT)

def test_test_has_data_submodule():
    n.assert_raises(AssertionError, check.test_has_data_submodule)
    open('.gitmodules', 'w').write('foo')
    os.mkdir('data')
    open(os.path.join('data', '.git'), 'w').write('bar')
    check.test_has_data_submodule()
