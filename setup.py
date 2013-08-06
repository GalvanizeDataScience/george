import setuptools # so we can `./setup.py develop`

setuptools.setup(
    name='george',
    version='0.0.1',
    packages=setuptools.find_packages(),

    author='Thomas Levine',
    maintainer='Thomas Levine',
    maintainer_email='occurrence@thomaslevine.com',
    description='Helpers for Zipfian Academy curriculum development',
    license='MIT License',
    keywords='datascience education cli',

    url='http://ufs.cc/',
    download_url='https://github.com/zipfian/george',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],

    include_package_data=True,
    zip_safe=False,
)
