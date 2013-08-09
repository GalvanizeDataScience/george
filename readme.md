George
=======
George is a set of utilities for Zipfian Academy curriculum development.

## Organization
George expects a particular structure.

* Each project is a directory that contains
  * `readme.md`
  * a git submodule called `data`.
  * a few sprint directories

* Each sprint is a directory that contains
  * Exercise code stubs in `code`
  * Corresponding tests in `test`, written to be run by
      nose (Python), Urchin (shell) or testthat (R).
  * `slides.md` containing an outline of the lecture,
      intended to be compiled with reveal.js
  * `readme.md` containing these sections
    * A
    * B
    * C
    * ...

## Installing
Install george so you can structure and check sprints

    pip install .

Install hub so you can easily make repositories on GitHub.

    gem install hub

## Running
Enter the sprint's directory.

    cd nytimes

Start a git repository.

    git init
    touch readme.md
    git add readme.md
    git commit . -m initialize

Put it on GitHub

    hub create -p zipfian/nytimes # -p for private
    git push -u origin master

Make the data submodule

    git submodule add git@github.com:zipfian/nytimes-data.git data

Scaffold a sprint.

    mkdir using-json-apis
    cd using-json-apis
    george init-sprint

As you're working on the sprint, check that a sprint contains all of its components.

    george check-sprint

And check that the project is complete.

    cd ..
    george check-project

## Development

### Fancy installation
You can install `george` with `./setup.py develop` so that you'll always be using
the latest version of the george python library, but that doesn't set up the `bin/george`
file in `/usr/bin` to be updated when you edit it.

### Running George's tests
Let's talk about three layers of tests.

1. Each sprint contains tests that students use to see how far they've gone in their work.
    These are written in python (nose), shell (urchin) or R (testthat).
2. George checks that the first layer of tests exists and that the tests correspond to the code stubs.
    These are written in python's standard unittest library.
3. There are tests of the george program to make sure that the second layer of tests work as intended.
    These are written in nose.

Run unit tests of the george program (test layer three) like so.

    nosetests

We don't have a good system for integration tests on the command-line interface.
