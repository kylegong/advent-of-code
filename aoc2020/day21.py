import collections


def potential_allergens(lines):
    alg_ing_map = collections.defaultdict(list)
    for line in lines:
        ings, algs = line
        for alg in algs:
            alg_ing_map[alg].append(set(ings))
    alg_map = {alg: set.intersection(*ing_lists)
               for alg, ing_lists in alg_ing_map.items()}
    return alg_map


def all_ingredients(lines):
    all_ings = set()
    for line in lines:
        all_ings.update(line[0])
    return all_ings


def part1(lines):
    potentials = potential_allergens(lines)
    all_ings = all_ingredients(lines)
    safe = all_ings - set.union(*[set(ings) for ings in potentials.values()])
    count = 0
    for line in lines:
        ings = line[0]
        for ing in ings:
            if ing in safe:
                count += 1
    return count


def part2(lines):
    potentials = potential_allergens(lines)
    while not all(len(ings) == 1 for ings in potentials.values()):
        for alg, ings in potentials.items():
            if len(ings) == 1:
                ing = list(ings)[0]
                for other_alg, ings in potentials.items():
                    if alg == other_alg:
                        continue
                    if ing in ings:
                        ings.remove(ing)
    alg_ings = [(alg, list(ings)[0]) for alg, ings in potentials.items()]
    alg_ings.sort(key=lambda x: x[0])
    return ','.join(i for _, i in alg_ings)


def parse(line):
    sp = line.split(" (contains ")
    ingredients = sp[0].split(' ')
    allergens = []
    if len(line) > 1:
        allergens = sp[1].rstrip(")").split(", ")
    return ingredients, allergens


def main(f):
    lines = [parse(line.strip()) for line in f]
    print(part1(lines))
    print(part2(lines))
