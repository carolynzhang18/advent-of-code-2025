tiles = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n').split(",")
        tiles.append([int(line[0]), int(line[1])])

def part1():
    ans = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            ans = max(ans, (abs(tiles[j][0] - tiles[i][0]) + 1) * (abs(tiles[j][1] - tiles[i][1]) + 1))
    return ans
print(part1())

def part2():
    # shoutout desmos
    up = [94872,50262]
    down = [94872,48511]
    ans = 0

    up_tiles = []
    down_tiles = []
    for x,y in tiles:
        if x <= 50000:
            if 50262 <= y <= 68129:
                up_tiles.append([x,y])
            elif 32369 <= y <= 48511:
                down_tiles.append([x,y])
    up_tiles.sort(key=lambda tile: [tile[1], tile[0]])
    
    max_x = 0
    for x, y in up_tiles:
        if x >= max_x:
            ans = max(ans, (up[0] - x + 1) * (y - up[1] + 1))
            max_x = x
    down_tiles.sort(key=lambda tile: [-tile[1], tile[0]])
    max_x = 0
    for x, y in down_tiles:
        if x >= max_x:
            ans = max(ans, (down[0] - x + 1) * (down[1] - y + 1))
            max_x = x
    return ans
print(part2())

