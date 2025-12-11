from collections import defaultdict
adj = defaultdict(list)
with open("input.txt", "r") as f:
    for line in f:
        line = line.rstrip('\n').split(": ")
        adj[line[0]].extend(line[1].split(" "))

def run(start, end):
    paths = {}
    def dfs(node):
        if node in paths:
            return paths[node]
        if node == end:
            return 1
        ans = 0    
        for neighbour in adj[node]:
            ans += dfs(neighbour)
        paths[node] = ans
        return ans
    dfs(start)
    return paths[start]

def part1():
    return run("you", "out")
print(part1())

def part2():
    return (run("svr", "fft") * run("fft", "dac") * run("dac", "out") + 
            run("svr", "dac") * run("dac", "fft") * run("fft", "out"))
print(part2())
