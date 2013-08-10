import os

def directories():
    for directory in ['code', 'lib', 'test']:
        if not os.path.isdir(directory):
            os.mkdir(directory)
            open(os.path.join(directory, '.gitignore'), 'w').write('')

def readme():
    if os.path.isfile('readme.md'):
        return

    fp = open('readme.md', 'w')
    for section in ['Overview', 'References', 'Goals', 'Assignment', 'Extra Credit', 'Glossary']:
        fp.write('\n## %s\n' % section)
    fp.close()

def gitignore():
    if not os.path.isfile('.gitignore'):
        open('.gitignore', 'w').write('*.pyc\n')

def main():
    directories()
    readme()
