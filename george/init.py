import os

def directories():
    for directory in ['code', 'lib', 'test']:
        os.mkdir(directory)
        open(os.path.join(directory, '.gitignore', 'w')).write('')

def readme():
    raise NotImplementedError
