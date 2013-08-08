import os
import uuid
import unittest

ROOT = os.getcwd()

def setup():
    # Make a temporary directory
    tmp = os.path.join('/', 'tmp', 'george-' + unicode(uuid.uuid1()))
    os.mkdir(tmp)
    os.chdir(tmp)

def teardown():
    tmp = os.getcwd()
    os.chdir(ROOT)


class Sandbox(unittest.TestCase):
    def setUp(self):
        setup()

    def tearDown(self):
        teardown()
