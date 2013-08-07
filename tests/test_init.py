import os
import nose.tools as n

from _helpers import setup, teardown
from george import init

def test_directories():
    'The appropriate directories should be created.'
    init.directories()
    for directory in ['code', 'lib', 'test']:
        yield n.assert_true, os.path.isdir(directory)
        yield n.assert_true, os.path.isfile(os.path.join(directory, '.gitignore'))

def test_readme():
    'A readme should be created with the appropriate sections.'
    init.readme()
    yield n.assert_true, os.path.isfile('readme.md')
    readme = open('readme.md').read()
    for section in ['Overview', 'References', 'Goals', 'Assignment', 'Extra Credit', 'Glossary']:
        yield n.assert_in, '\n## %s' % section, readme
