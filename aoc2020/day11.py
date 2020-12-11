NEIGHBOR_DELTAS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


class Grid:
    def __init__(self, lines, new_seat_func):
        self.rows = [[s for s in line] for line in lines]
        self.new_seat = new_seat_func

    def num_rows(self):
        return len(self.rows)

    def num_cols(self):
        return len(self.rows[0])

    def exists(self, r, c):
        return 0 <= r < self.num_rows() and 0 <= c < self.num_cols()

    def seat(self, r, c):
        try:
            return self.rows[r][c]
        except:
            print(r, c, self.exists(r, c), self.num_rows(), self.num_cols())
            raise

    def set_seat(self, r, c, s):
        self.rows[r][c] = s

    def all_seat_pos(self):
        for r in range(self.num_rows()):
            for c in range(self.num_cols()):
                yield (r, c)

    def num_occ(self):
        return len([1 for r, c in self.all_seat_pos() if self.seat(r, c) == "#"])

    def __str__(self):
        return '\n'.join(''.join(r) for r in self.rows)

    def next_round(self):
        has_changed = False
        new_rows = []
        for r in range(self.num_rows()):
            row = []
            new_rows.append(row)
            for c in range(self.num_cols()):
                seat = self.seat(r, c)
                new_seat = self.new_seat(self, r, c)
                if seat != new_seat:
                    has_changed = True
                row.append(new_seat)
        self.rows = new_rows
        return has_changed


def new_seat_p1(grid, r, c):
    seat = grid.seat(r, c)
    if seat == ".":
        return "."
    num_neighbors = 0
    for dr, dc in NEIGHBOR_DELTAS:
        if grid.exists(r + dr, c + dc):
            if grid.seat(r+dr, c+dc) == "#":
                num_neighbors += 1
    if seat == "#" and num_neighbors >= 4:
        return "L"
    if seat == "L" and num_neighbors == 0:
        return "#"
    return seat


def part1(lines):
    grid = Grid(lines, new_seat_p1)
    while grid.next_round():
        pass
    return grid.num_occ()


def new_seat_p2(grid, r, c):
    seat = grid.seat(r, c)
    if seat == ".":
        return "."
    num_neighbors = 0
    for dr, dc in NEIGHBOR_DELTAS:
        nr = r + dr
        nc = c + dc
        if not grid.exists(nr, nc):
            continue
        neighbor = grid.seat(nr, nc)
        seen = False
        while neighbor == "." and not seen:
            nr += dr
            nc += dc
            if not grid.exists(nr, nc):
                break
            neighbor = grid.seat(nr, nc)
        if neighbor == "#":
            num_neighbors += 1
            seen = True
            continue
        if neighbor == "L":
            seen = True
            continue
    if seat == "#" and num_neighbors >= 5:
        return "L"
    if seat == "L" and num_neighbors == 0:
        return "#"
    return seat


def part2(lines):
    grid = Grid(lines, new_seat_p2)
    while grid.next_round():
        pass
    return grid.num_occ()


def main(f):
    lines = [line.strip() for line in f]
    print(part1(lines))
    print(part2(lines))
