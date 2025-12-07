grid = []
start = None
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n')
        row = [char != '.' for char in line]
        if not grid:
            start = line.find('S')
        grid.append(row)

def part1():
    splits = 0
    beams = set([start])
    for row in range(len(grid) - 1):
        next_beams = set()
        for beam in beams:
            if grid[row+1][beam]:
                splits += 1
                if beam - 1 >= 0:
                    next_beams.add(beam - 1)
                if beam + 1 < len(grid[0]):
                    next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        beams = next_beams
    return splits
print(part1())

def part2():
    visited = {}
    def num_timelines(row, col):
        if row == len(grid) - 1:
            return 1
        if (row, col) not in visited:
            if grid[row+1][col]:
                ans = 0
                if col-1 >= 0:
                    ans += num_timelines(row+1, col-1)
                if col+1 < len(grid[0]):
                    ans += num_timelines(row+1, col+1)
                visited[(row, col)] = ans
            else:
                visited[(row, col)] = num_timelines(row+1, col)
        return visited[(row, col)]
    return num_timelines(0, start)
print(part2())

