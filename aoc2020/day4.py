
def part1(lines):
    pps = parse(lines)
    return len([pp for pp in pps if isValid1(pp)])


def part2(lines):
    pps = parse(lines)
    return len([pp for pp in pps if isValid2(pp)])


def isValid1(pp):
    for k in ["byr", "iyr",  "eyr", "hgt", "hcl", "ecl",  "pid"]:
        if k not in pp:
            return False
    return True


def isValid2(pp):
    try:
        byr = int(pp['byr'])
        if 1920 > byr or byr > 2002:
            return False
        iyr = int(pp['iyr'])
        if 2010 > iyr or iyr > 2020:
            return False
        eyr = int(pp['eyr'])
        if 2020 > eyr or eyr > 2030:
            return False
        hgt = pp['hgt']
        if 'cm' in hgt:
            hgt = int(hgt[:-2])
            if 150 > hgt or hgt > 193:
                return False
        elif 'in' in hgt:
            hgt = int(hgt[:-2])
            if 59 > hgt or hgt > 76:
                return False
        else:
            return False
        hcl = pp['hcl']
        if hcl[0] != "#":
            return False
        hcl = hcl[1:]
        for c in hcl:
            int("0x%s" % c, 16)
        ecl = pp['ecl']
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        pid = pp['pid']
        if len(pid) != 9:
            return False
        int(pid)
    except:
        return False
    return True


def parse(lines):
    pp = {}
    out = []
    for line in lines:
        if line == "":
            out.append(pp)
            pp = {}
            continue
        pairs = line.split(" ")
        for p in pairs:
            k, v = p.split(":")
            pp[k] = v
    if pp != {}:
        out.append(pp)
    return out


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
