grid = []
with open("input.txt", "r") as f:
    for line in f:
        row = []
        line = line.rstrip('\n')
        row = [char == '@' for char in line]
        grid.append(row)

rows = len(grid)
cols = len(grid[0])
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def takeable(r, c):
    if not grid[r][c]:
        return False
    count = sum(1 for x,y in dirs 
                    if 0 <= r+x < rows and 0 <= c+y < cols and grid[r+x][c+y])
    return count < 4

def part1():
    return sum(1 for r in range(rows) for c in range(cols) if takeable(r, c))
print(part1())

def part2():
    total = 0
    removed = True
    while removed: 
        removed = False
        for r in range(rows):
            for c in range(cols):
                if takeable(r, c):
                    grid[r][c] = False
                    total += 1
                    removed = True
    return total
print(part2())
