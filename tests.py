import doctest
import importlib
import unittest
from shared import utils

YEARS = [
    2020,
]

def day_tests(tests):
    day = 0
    for year in YEARS:
        while True:
            day += 1
            try:
                mod = importlib.import_module('aoc%s.day%s' % (year, day))
                tests.addTests(doctest.DocTestSuite(mod))
            except ModuleNotFoundError:
                break
    return tests

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(utils))
    day_tests(tests)
    return tests

if __name__ == "__main__":
    unittest.main()