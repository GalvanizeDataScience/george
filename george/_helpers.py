from unittest import TestCase

def add_test(_suite, func):
    'Wrap a test function in a test case and then add it to the test suite.'
    class FooTestCase(TestCase):
        def runTest(self):
            func()
    _suite.addTest(FooTestCase())
