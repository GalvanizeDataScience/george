import os
import nose.tools as n

from _sandbox import setup, teardown
from george import init

def test_directories():
    'The appropriate directories should be created.'
    setup()
    init.directories()
    for directory in ['code', 'lib', 'test']:
        yield n.assert_true, os.path.isdir(directory)
        yield n.assert_true, os.path.isfile(os.path.join(directory, '.gitignore'))

def test_readme():
    'A readme should be created with the appropriate sections.'
    setup()
    init.readme()
    yield n.assert_true, os.path.isfile('readme.md')
    readme = open('readme.md').read()
    for section in ['Overview', 'References', 'Goals', 'Assignment', 'Extra Credit', 'Glossary']:
        yield n.assert_in, '\n## %s' % section, readme

def test_existing_dir_is_ok():
    'If some skeleton files already exist, init should quietly skip them.'
    setup()
    os.mkdir('code')
    init.directories()

def test_existing_file_is_ok():
    'If some skeleton files already exist, init should quietly skip them.'
    banana = 'I am a banana.'
    setup()
    open('readme.md', 'w').write(banana)
    init.readme()
    n.assert_equal(open('readme.md').read(), banana)
