def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def scratch1(game: str) -> list:
    game = game.split(": ")
    winning_numbers = [int(x) for x in game[1].split(" | ")[0].split()]
    player_numbers = [int(x) for x in game[1].split(" | ")[1].split()]

    points = 0
    for winning in winning_numbers:
        if winning in player_numbers:
            if points == 0:
                points += 1
            else:
                points *= 2
    return points


def prepare2(games: str) -> list:
    cards = []

    for line in games.splitlines():
        winners, numbers = line.split(": ")[1].split(" | ")
        cards.append((winners.split(), numbers.split()))

    return cards


def scratch2(game: list) -> int:
    cards = [1] * len(game)

    for i, card in enumerate(game):
        for j in range(i + 1, i + 1 + len(set(card[0]) & set(card[1]))):
            cards[j] += 1 * cards[i]

    return sum(cards)


def main():
    filename = "day4/day4.txt"
    content = get_content(filename)
    # counter = 0
    # for game in content:
    #     counter += scratch1(game)
    # print(counter)
    print(scratch2(prepare2(content)))

main()
