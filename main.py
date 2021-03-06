import argparse
import importlib
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('day', type=int, help='day to run')
parser.add_argument('--year', type=int, default=2020,
                    help='Advent of Code year')
parser.add_argument('--test', action="store_true", help='run doctests for day')
parser.add_argument('--time', action="store_true", help='show time elapsed')
parser.add_argument('--profile', action="store_true", help='run cProfile')


def run_day(year, day):
    input_file = "aoc%s/inputs/%s.txt" % (year, day)
    with open(input_file) as f:
        script = importlib.import_module('aoc%s.day%s' % (year, day))
        script.main(f)


if __name__ == "__main__":
    args = parser.parse_args()
    start = datetime.now()
    if args.profile:
        import cProfile
        cProfile.run('run_day(args.year, args.day)')
    elif args.test:
        import doctest
        import unittest
        mod = importlib.import_module('aoc%s.day%s' % (args.year, args.day))
        tests = unittest.TestSuite()
        tests.addTests(doctest.DocTestSuite(mod))
        runner = unittest.TextTestRunner()
        runner.run(tests)
    else:
        run_day(args.year, args.day)

    if args.time:
        print("Ran in %.3fs" % (datetime.now() - start).total_seconds())
