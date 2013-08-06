George
=======
George is a set of utilities for Zipfian Academy curriculum development.

## Running
Enter the sprint's directory.

    cd random-forests-sprint

Scaffold a sprint.

    george init

Test that a sprint contains all of its components.

    george test

## Installing

    sudo python setup.py develop

## Running George's tests
These test the george program, not the various sprints.

    nosetests

## Organization
George expects a particular structure inside of sprints.

* Tests are run with nose (Python) or Urchin (shell).
* There is a submodule called `data`.
* ...
