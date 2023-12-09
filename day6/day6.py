def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()
    return content


def prepare1(content: str) -> list:
    content = [line.split() for line in content.splitlines()]
    td = list(zip(content[0], content[1]))
    del td[0]
    for i, t in enumerate(td):
        td[i] = (int(t[0]), int(t[1]))
    return td


def sol1(content: list) -> int:
    prod = 1
    for race in content:
        time, distance = race
        counter = 0
        for t in range(time):
            covered = t * (time - t)
            if covered > distance:
                counter += 1
        prod *= counter

    return prod


def prepare2(content: str) -> list:
    content = [
        [el.replace(" ", "") for el in line.split(":")] for line in content.splitlines()
    ]
    return [int(content[0][1]), int(content[1][1])]


def sol2(content: list) -> int:
    time, distance = content
    counter = 0
    for t in range(time):
        covered = t * (time - t)
        if covered > distance:
            counter += 1
    return counter


def main():
    content = get_content("day6/input.txt")
    content1 = prepare1(content)
    print("Part 1: ", sol1(content1))
    content2 = prepare2(content)
    print("Part 2: ", sol2(content2))


if __name__ == "__main__":
    main()
