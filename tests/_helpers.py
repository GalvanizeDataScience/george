import os
import uuid
ROOT = os.getcwd()

def setup():
    # Make a temporary directory
    tmp = os.path.join('/', 'tmp', 'george-' + unicode(uuid.uuid1()))
    os.mkdir(tmp)
    os.chdir(tmp)

def teardown():
    tmp = os.getcwd()
    os.chdir(ROOT)

