import importlib
import sys

if __name__ == "__main__":
    day = sys.argv[1]
    input_file = "aoc2020/inputs/%s.txt" % day
    with open(input_file) as f:
        day = importlib.import_module('aoc2020.day%s' % day)
        day.main(f)
