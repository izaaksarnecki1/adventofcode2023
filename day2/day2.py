def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()

    return content


def count_bags(content: str) -> int:
    bags = content.split("\n")
    counter = 0
    games = []
    for line in bags:
        reqs = {"red": 12, "green": 13, "blue": 14}
        line = line.split(": ")
        game = int(line[0].split(" ")[1])
        counter += game
        line[1] = line[1].split("; ")
        for bag in line[1]:
            bag = bag.split(", ")
            for cube in bag:
                cube = cube.split(" ")
                reqs[cube[1]] -= int(cube[0])
            checker = False
            for vals in reqs.values():
                if vals < 0:
                    counter -= game
                    games.append((game, line[1]))
                    checker = True
                    break
            if checker:
                break
            for cube in bag:
                cube = cube.split(" ")
                reqs[cube[1]] += int(cube[0])   
        
    print(games)
    return counter


def main():
    filename = "day2/day2.txt"
    content = get_content(filename)
    print(count_bags(content))


if __name__ == "__main__":
    main()
