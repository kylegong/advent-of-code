def tree_at(grid, x, y):
    row = grid[y]
    return row[x % len(row)] == "#"


def part1(grid):
    return count_trees(grid, 3, 1)


def count_trees(grid, dx, dy):
    x, y = 0, 0
    trees = 0
    while True:
        x += dx
        y += dy
        if y > len(grid)-1:
            return trees
        if tree_at(grid, x, y):
            trees += 1


def part2(grid):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees = [count_trees(grid, dx, dy) for dx, dy in slopes]
    return product(trees)


def product(lst):
    import functools
    return functools.reduce(lambda x, y: x*y, lst)


def main(f):
    grid = [[p for p in line.strip()] for line in f]
    print(part1(grid))
    print(part2(grid))
