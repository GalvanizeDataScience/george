from unittest import TestSuite, TextTestRunner
import os
import nose.tools as n
from _helpers import add_test
from copy import copy

def add_parametrized_test(suite, func, param):
    _param = copy(param)
    return add_test(suite, lambda: func(_param))

def suite():
    _suite = TestSuite()

    for func in [
        test_python_init,
        test_python_files_correspond,
        test_shell_files_correspond,
        test_has_a_test,
    ]:
        add_test(_suite, func)

    for dirname in ['code', 'lib', 'test']:
        add_parametrized_test(_suite, check_has_directory, dirname)

    for filename in ['readme.md', 'slides.md']:
        add_parametrized_test(_suite, check_has_file, filename)

    for sectionname in [
        'Overview',
        'References',
        'Goals',
        'Assignment',
        'Extra Credit',
        'Glossary',
    ]:

        add_parametrized_test(_suite, check_readme_has_section, sectionname)
        add_test(_suite, check_readme_has_main_teacher)
    return _suite

def test_python_init():
    'If there are any python files in the code directory, there should be an __init__.py'
    n.assert_true(os.path.isdir('code'))
    if filter(lambda filename: filename.endswith('.py'), os.listdir('code')):
        n.assert_true(os.path.isfile(os.path.join('code', '__init__.py')), msg = 'There should be an __init__.py')

def test_python_files_correspond():
    '.py files in ``code`` should correspond with test files in ``test``'
    if not (os.path.isdir('code') and os.path.isdir('test')):
        return

    code_files = set(filter(lambda filename: filename.endswith('.py'), os.listdir('code')))
    test_files = filter(lambda filename: filename.startswith('test_') and filename.endswith('.py'), os.listdir('test'))

    if '__init__.py' in code_files:
        code_files.remove('__init__.py')

    n.assert_set_equal(set([test_file[5:] for test_file in test_files]), code_files)

def test_shell_files_correspond():
    '.sh files in ``code`` should correspond with test directories in ``test``'
    if not (os.path.isdir('code') and os.path.isdir('test')):
        return

    code_files = filter(lambda filename: filename.endswith('.sh'), os.listdir('code'))
    test_files = filter(lambda filename: (not filename.startswith('.')) and filename.endswith('.sh'), os.listdir('test'))
    n.assert_set_equal(set(test_files), set(code_files))

@n.nottest
def test_python_test_coverage():
    pass

@n.nottest
def test_shell_test_coverage():
    pass

def check_has_directory(dirname):
    n.assert_true(os.path.isdir(dirname), msg = '%s should exist.' % dirname)

def check_has_file(filename):
    n.assert_true(os.path.isfile(filename), msg = '%s should exist.' % filename)

def check_readme_has_main_teacher():
    readme = open('readme.md').read()
    n.assert_in('\nMain teacher:', readme)

def check_readme_has_section(section):
    readme = open('readme.md').read()
    n.assert_in('\n## %s' % section, readme)

def test_has_a_test():
    if os.path.isdir('test'):
        n.assert_true(len(os.listdir('test')) > 0)
    else:
        raise AssertionError('There is no test directory.')

def test_has_makefile():
    n.assert_true(os.path.isfile('Makefile'), 'There should me a Makefile.')
    makefile = open('Makefile').read()
    n.assert_in('.PHONY', makefile)
    n.assert_in('test:', makefile)

def main():
    TextTestRunner(verbosity=2).run(suite())
