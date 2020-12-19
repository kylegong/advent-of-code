from shared import utils

class Grid:
    def __init__(self, init_grid, num_dimensions):
        self.active_map = {}
        for y, row in enumerate(init_grid):
            for x, state in enumerate(row):
                coords = tuple([x, y] + [0] * (num_dimensions - 2))
                if state == "#":
                    self.active_map[coords] = True
    
    def is_active(self, coords):
        return self.active_map.get(coords, False)
    
    def num_active(self):
        return len(self.active_map)

    def is_next_cycle_active(self, coords):
        active_neighbors = [n for n in utils.neighbors(*coords) if self.is_active(n)]
        if self.is_active(coords):
            return len(active_neighbors) in (2, 3)
        else:
            return len(active_neighbors) == 3
    
    def next_cycle(self):
        points = set()
        for coords in self.active_map.keys():
            points.update(utils.neighbors(*coords))
        new_active_map = {}
        for coords in points:
            if self.is_next_cycle_active(coords):
                new_active_map[coords] = True
        self.active_map = new_active_map

def part1(lines):
    grid = Grid(lines, 3)
    for n in range(6):
        grid.next_cycle()
    return grid.num_active()

def part2(lines):
    grid = Grid(lines, 4)
    for n in range(6):
        grid.next_cycle()
    return grid.num_active()


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
