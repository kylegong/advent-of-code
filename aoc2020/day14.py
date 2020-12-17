def apply_mask(mask, val):
    """
    >>> apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11)
    73
    """
    b = [d for d in format(val, "036b")]
    for i, d in enumerate(mask):
        if d == "X":
            continue
        b[i] = d
    return int("".join(b), 2)

def part1(prog):
    mask = None
    mem = {}
    for line in prog:
        if 'mask' in line:
            mask = line['mask']
            continue
        mem[line['addr']] = apply_mask(mask, line['val'])
    return sum(v for k, v in mem.items())

def apply_addr_mask(mask, val):
    """
    >>> apply_addr_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", 11)
    73
    """
    b = [d for d in format(val, "036b")]
    for i, d in enumerate(mask):
        if d == "X":
            b[i] = "X"
        if d == "1":
            b[i] = "1"
    return gen_addrs("".join(b))

def gen_addrs(addr):
    """
    >>> list(gen_addrs("01X0X"))
    [8, 9, 12, 13]
    """
    i = addr.find("X")
    if i == -1:
        yield int(addr, 2)
        return
    a = list(addr)
    a[i] = "0"
    for x in gen_addrs("".join(a)):
        yield x
    b = list(addr)
    b[i] = "1"
    for x in gen_addrs("".join(b)):
        yield x


def part2(prog):
    mask = None
    mem = {}
    for line in prog:
        if 'mask' in line:
            mask = line['mask']
            continue
        for addr in apply_addr_mask(mask, line['addr']):
            mem[addr] = line['val']
    return sum(v for k, v in mem.items())

def parse(lines):
    prog = []
    for line in lines:
        if line.startswith("mask"):
            prog.append({"mask": line.split(" = ")[1]})
        else:
            line = line.replace("mem[", "").replace("]", "")
            addr, val = line.split(" = ")
            prog.append({"addr": int(addr), "val":int(val)})
    return prog


def main(f):
    lines = [line.strip() for line in f]
    prog = parse(lines)
    print(part1(prog))
    print(part2(prog))
