import os

def directories():
    for directory in ['code', 'lib', 'test']:
        os.mkdir(directory)
        open(os.path.join(directory, '.gitignore'), 'w').write('')

def readme():
    fp = open('readme.md', 'w')
    for section in ['Overview', 'References', 'Goals', 'Assignment', 'Extra Credit', 'Glossary']:
        fp.write('\n## %s\n' % section)
    fp.close()
