from shared.utils import group, product

def parseField(field):
    name, ranges = field.split(": ")
    ranges = [[int(n) for n in r.split("-")] for r in ranges.split(" or ")]
    return name, ranges

def parseYours(yours):
    tickets = []
    for line in yours[1:]:
        tickets.extend([int(n) for n in line.split(",")])
    return tickets

def parseNearby(nearby):
    tickets = []
    for line in nearby[1:]:
        tickets.append([int(n) for n in line.split(",")])
    return tickets

def validForFields(val, fields):
    try:
        for field in fields:
            name, ranges = field
            for low, high in ranges:
                if low <= val and val <= high:
                    return True
        return False
    except:
        print(val, fields)

def part1(fields, nearby):
    invalid = []
    for t in nearby:
        for n in t:
            if not validForFields(n, fields):
                invalid.append(n)
    return sum(invalid)

def part2(fields, yours, nearby):
    valid = [t for t in nearby if all(validForFields(n, fields) for n in t)]
    indices = range(len(valid[0]))
    field_map = {n: [n, r] for n, r in fields}
    field_poss = {i: set(name for name, _ in fields) for i in indices}
    for t in valid:
        for i, n in enumerate(t):
            for field_name in list(field_poss[i]):
                field = field_map[field_name]
                if not validForFields(n, [field]):
                    field_poss[i].remove(field_name)
    while True:
        found = False
        for i, poss in field_poss.items():
            if len(poss) == 1:
                name = list(poss)[0]
                for ri in field_poss.keys():
                    if ri != i and name in field_poss[ri]:
                        found = True
                        field_poss[ri].discard(name)
        if not found:
            break
    p = []
    for i, s in field_poss.items():
        name = list(s)[0]
        if name.startswith("departure"):
            p.append(yours[i])
    return product(p)


def main(f):
    fields, yours, nearby = group(line.strip() for line in f)
    fields = [parseField(f) for f in fields]
    yours = parseYours(yours)
    nearby = parseNearby(nearby)
    print(part1(fields, nearby))
    print(part2(fields, yours, nearby))
