import argparse
import importlib
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('day', type=int, help='day to run')
parser.add_argument('--year', type=int, default=2020,
                    help='Advent of Code year')
parser.add_argument('--time', type=bool, action=argparse.BooleanOptionalAction,
                    help='show time elapsed')
parser.add_argument('--profile', type=bool, action=argparse.BooleanOptionalAction,
                    help='run cProfile')


def run_day(day, year):
    input_file = "aoc%s/inputs/%s.txt" % (year, day)
    with open(input_file) as f:
        script = importlib.import_module('aoc%s.day%s' % (year, day))
        script.main(f)


if __name__ == "__main__":
    args = parser.parse_args()
    start = datetime.now()
    if args.profile:
        import cProfile
        cProfile.run('run_day(args.day, args.year)')
    run_day(args.day, args.year)

    if args.time:
        print("Ran in %.3fs" % (datetime.now() - start).total_seconds())
