import collections
import math

from shared import utils


class Tile:
    def __init__(self, id, grid):
        self.id = id
        self.grid = grid

    def key(self, edge):
        return sorted((edge, edge[::-1]))[0]

    def flip(self):
        self.grid = [line[::-1] for line in self.grid]

    def rotate(self):
        self.grid = [''.join(list(i)[::-1]) for i in zip(*self.grid)]

    def strip_borders(self):
        self.grid = [row[1:-1] for row in self.grid[1:-1]]

    @property
    def top(self):
        return self.grid[0]

    @property
    def bottom(self):
        return self.grid[9][::-1]

    @property
    def left(self):
        return ''.join([line[0] for line in self.grid][::-1])

    @property
    def right(self):
        return ''.join([line[9] for line in self.grid])

    def edges(self):
        return (self.top, self.right, self.bottom, self.left)

    def is_aligned(self, edges):
        for theirs, ours in zip(edges, self.edges()):
            if theirs is None:
                continue
            if theirs != ours:
                return False
        return True

    def align(self, edges):
        for _ in range(4):
            self.rotate()
            if self.is_aligned(edges):
                return True
        self.flip()
        for _ in range(4):
            self.rotate()
            if self.is_aligned(edges):
                return True
        return False

    def keys(self):
        return tuple(self.key(e) for e in self.edges())

    def count_pattern(self, pattern):
        '''
        >>> Tile(0, ['##.', '.##', '..#']).search(['#.', '.#'])
        3
        '''
        points = []
        for y, row in enumerate(pattern):
            for x, p in enumerate(row):
                if p == '#':
                    points.append((x, y))
        marked = set()
        for gy in range(len(self.grid) - len(pattern) + 1):
            for gx in range(len(self.grid[0]) - len(pattern[0]) + 1):
                if all(self.grid[gy+py][gx+px] == "#" for px, py in points):
                    marked.update((gx+px, gy+py) for px, py in points)
        return len(marked)

    def count(self, char):
        return len([c for row in self.grid for c in row if c == char])

    def __str__(self):
        return '\n'.join(self.grid)


def part1(grids):
    tiles = []
    for grid in grids:
        id = int(grid[0].lstrip("Tile ").rstrip(":"))
        tiles.append(Tile(id, grid[1:]))
    corners = []
    import collections
    edge_map = collections.defaultdict(set)
    for tile in tiles:
        for k in tile.keys():
            edge_map[k].add(tile.id)
    for tile in tiles:
        edges_matched = 0
        for k in tile.keys():
            matches = [t for t in edge_map[k] if t != tile.id]
            if matches:
                edges_matched += 1
        if edges_matched == 2:
            corners.append(tile.id)
    return utils.product(corners)


def part2(grids):
    tiles = []
    for grid in grids:
        id = int(grid[0].lstrip("Tile ").rstrip(":"))
        tiles.append(Tile(id, grid[1:]))
    #t = [t for t in tiles if t.id == 3079][0]
    key_map = collections.defaultdict(list)
    for tile in tiles:
        for k in tile.keys():
            key_map[k].append(tile)
    matches = collections.defaultdict(dict)
    for tile in tiles:
        for k in tile.keys():
            for t in key_map[k]:
                if t.id != tile.id:
                    matches[tile.id][k] = t

    image = []
    for tile in tiles:
        if len(matches[tile.id]) == 2:
            image.append([tile])
            break
    w = int(math.sqrt(len(tiles)))
    for y in range(w):
        if y == 0:
            cur = image[y][0]
            for _ in range(4):
                if (cur.key(cur.right) in matches[cur.id]
                        and cur.key(cur.bottom) in matches[cur.id]):
                    break
                cur.rotate()
        for x in range(1, w):
            cur = image[y][x-1]
            left = cur.right[::-1]
            nxt = matches[cur.id][cur.key(cur.right)]
            nxt.align((None, None, None, left))
            image[y].append(nxt)
            if x == w-1:
                if y == w-1:
                    continue
                # left edge of next row
                # left is outside, top is bottom of image[y][0]
                above = image[y][0]
                top = above.bottom[::-1]
                nxt = matches[above.id][above.key(above.bottom)]
                nxt.align((top, None, None, None))
                image.append([nxt])
    for row in image:
        for t in row:
            t.strip_borders()
    grid = []
    for y, row in enumerate(image):
        lines = []
        for t in row:
            for i, line in enumerate(t.grid):
                if i == len(lines):
                    lines.append('')
                lines[i] += line
        grid.extend(lines)
    full = Tile(0, grid)
    nessie = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    for _ in range(4):
        full.rotate()
        pattern_count = full.count_pattern(nessie)
        if pattern_count > 0:
            return full.count("#") - pattern_count
    full.flip()
    for _ in range(4):
        pattern_count = full.count_pattern(nessie)
        if pattern_count > 0:
            return full.count("#") - pattern_count


def main(f):
    grids = utils.group([line.strip() for line in f])
    print(part1(grids))
    print(part2(grids))
