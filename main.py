import importlib
import sys
from datetime import datetime

if __name__ == "__main__":
    start = datetime.now()
    day = sys.argv[1]
    input_file = "aoc2020/inputs/%s.txt" % day
    with open(input_file) as f:
        day = importlib.import_module('aoc2020.day%s' % day)
        day.main(f)
    print("Ran in %.3fs" % (datetime.now() - start).total_seconds())
