# Path: day3/day3.py


def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()

    return content


lists = [
    ["4", "6", "7", ".", ".", "1", "1", "4", ".", "."],
    [".", ".", ".", "*", ".", ".", ".", ".", ".", "."],
    [".", ".", "3", "5", ".", ".", "6", "3", "3", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
    ["6", "1", "7", "*", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "+", ".", "5", "8", "."],
    [".", ".", "5", "9", "2", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "7", "5", "5", "."],
    [".", ".", ".", "$", ".", "*", ".", ".", ".", "."],
    [".", "6", "6", "4", ".", "5", "9", "8", ".", "."],
]

lists1 = [
    ["467..114.."],
    ["...*......"],
    ["..35..633."],
    ["......#..."],
    ["617*......"],
    [".....+.58."],
    ["..592....."],
    ["......755."],
    ["...$.*...."],
    [".664.598.."],
]


def part1(content: str) -> int:
    schematic = [[line] for line in content.splitlines()]
    for line in schematic:
        print(get_nr_in_line(line))


def get_nr_in_line(line: str) -> list:
    idx = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            start = i   
            while line[i].isdigit():
                i += 1
            end = i
            idx.append((start, end))
        i += 1
    return idx


def check_adjacent(schematic: list, x: int, y: int) -> int:
    ...


def main():
    filename = "day3/input.txt"
    content = get_content(filename)
    print(f"Part 1: sum of numbers: {part1(content)}")


if __name__ == "__main__":
    main()
