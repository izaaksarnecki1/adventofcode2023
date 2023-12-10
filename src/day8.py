from math import lcm

# 509

def get_content(filename: str) -> str:
    with open(filename) as f:
        return f.read()
    
def main():
    filename = 'input/input8.txt'
    print("Part 1: ", part1(prepare1(filename)))
    print("Part 2: ", part2(prepare2(filename)))

def prepare1(filename: str) -> tuple:
    with open(filename, 'r') as content:
        content = content.read()
        content = [x.strip() for x in content.splitlines() if x != '']
        instructions = [1 if x == 'R' else 0 for x in content[0]]
        dirs = [x.split(' = ') for x in content[1:]]
        for i in range(len(dirs)):
            dirs[i][1] = dirs[i][1].strip('(').strip(')').split(', ')
        
        dirsdict = {}
        for i in range(len(dirs)):
            dirsdict[dirs[i][0]] = dirs[i][1][0], dirs[i][1][1]
        return instructions, dirsdict


def part1(ins_dirs: tuple) -> int:
    instructions, dirs = ins_dirs
    pos = 'AAA'
    counter = 0
    while pos != 'ZZZ':
        for i in instructions:
            pos = dirs[pos][i]
            counter += 1
    return counter            

def prepare2(filename: str) -> tuple:
    data = {}
    with open("input/input8.txt", "r") as input_data:
        instructions = input_data.readlines(2)[0].strip()
        for line in input_data.readlines():
            if line == "\n": 
                continue
            line = line.strip().split(" = ")
            line[1] = line[1][1:-1:].split(", ")
            data[line[0]] = {"L": line[1][0], "R": line[1][1]}
    return instructions, data 


def part2(ins_data: tuple) -> int:
    instructions, data = ins_data
    counter = 0
    current = [i for i in data.keys() if i[-1] == "A"]
    cycles = []
    for c in current:
        cycle = 0
        while c[-1] != "Z":
            cycle += 1
            for i in instructions:
                if c[-1] != "Z": c = data[c][i]
                else: break
        cycles.append(cycle*len(instructions))
    counter = lcm(*cycles)
    
    return counter


if __name__ == '__main__':
    main()
