import os
import nose.tools as n

from tests._helpers import setup, teardown
from george import init

def test_directories():
    'The appropriate directories should be created.'
    init.directories()
    for directory in ['code', 'lib', 'test']:
        yield n.assert_true, os.path.isdir(directory)
        yield n.assert_true, os.path.isfile(os.path.join(directory, '.gitignore'))
