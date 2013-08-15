import os
import shutil
import nose.tools as n

from _sandbox import setup, teardown
from george import check_sprint

def test_check_has_directory():
    n.assert_raises(AssertionError, lambda: check_sprint.check_has_directory('code'))
    os.mkdir('code')
    check_sprint.check_has_directory('code')

def test_check_has_file():
    n.assert_raises(AssertionError, lambda: check_sprint.check_has_file('readme.md'))
    open('readme.md', 'w').write('foo')
    check_sprint.check_has_file('readme.md')

def test_check_readme_has_section():
    n.assert_raises(AssertionError, lambda: check_sprint.check_readme_has_section('Foo'))

    open('readme.md', 'w').write('Foo')
    n.assert_raises(AssertionError, lambda: check_sprint.check_readme_has_section('Foo'))

    open('readme.md', 'w').write('Title\n======\n## Foo')
    check_sprint.check_readme_has_section('Foo')

def test_test_python_init():
    setup()
    os.mkdir('code')
    os.mkdir('test')
    check_sprint.test_python_init()

    open(os.path.join('code', 'foo.py'), 'w').write('foo')
    n.assert_raises(AssertionError, check_sprint.test_python_init)
    os.remove(os.path.join('code', 'foo.py'))

    open(os.path.join('code', '__init__.py'), 'w').write('foo')
    check_sprint.test_python_init()

def test_test_has_a_test():
    setup()
    n.assert_raises(AssertionError, check_sprint.test_has_a_test)
    os.mkdir('test')
    open(os.path.join('test', 'foo'), 'w').write('')
    check_sprint.test_has_a_test()

def test_test_python_files_correspond():
    setup()
    check_sprint.test_python_files_correspond()

    os.mkdir('code')
    os.mkdir('test')
    open(os.path.join('code', 'foo.py'), 'w').write('')
    open(os.path.join('code', '__init__.py'), 'w').write('')
    n.assert_raises(AssertionError, check_sprint.test_python_files_correspond)

    open(os.path.join('test', 'test_foo.py'), 'w').write('')
    check_sprint.test_python_files_correspond()

def test_test_shell_files_correspond():
    setup()
    check_sprint.test_shell_files_correspond()

    os.mkdir('code')
    os.mkdir('test')
    open(os.path.join('code', 'foo.sh'), 'w').write('')
    n.assert_raises(AssertionError, check_sprint.test_shell_files_correspond)

    open(os.path.join('test', 'foo.sh'), 'w').write('')
    check_sprint.test_shell_files_correspond()

def test_test_makefile():
    setup()
    n.assert_raises(AssertionError, check_sprint.test_has_makefile)
    open('Makefile', 'w').write('')
    n.assert_raises(AssertionError, check_sprint.test_has_makefile)
    open('Makefile', 'w').write('.PHONY: test\ntest:\n  urchin test')
    check_sprint.test_has_makefile()
