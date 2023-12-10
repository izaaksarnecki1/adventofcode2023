from collections import Counter


def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read().splitlines()
    return content


def get_type(hand: str) -> int:
    counts = Counter(hand)
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in counts.values():
            return 5
        if 3 in counts.values() and 2 in counts.values():
            return 4
    if len(counts) == 3:
        if 3 in counts.values() and list(counts.values()).count(1) == 2:
            return 3
        if list(counts.values()).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1
    return 0


def get_order(cards: dict, hand: str) -> list:
    return [cards.get(card, card) for card in hand]


def sorting(cards: dict, hand: str) -> tuple:
    return get_type(hand), get_order(cards, hand)


def part1(content: str, cards: dict) -> int:
    plays = []
    for line in content:
        hand, bid = line.split()
        plays.append((hand, int(bid)))
    plays.sort(key=lambda play: sorting(cards, play[0]))
    ans = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        ans += bid * rank
    return ans


def all_combinations(cards: dict, hand: str) -> list:
    if not hand:
        return [""]

    current_card = hand[0]
    if current_card == "J":
        possible_values = "23456789TQKA"
    else:
        possible_values = current_card

    combinations = [
        first_half + second_half
        for first_half in possible_values
        for second_half in all_combinations(cards, hand[1:])
    ]

    return combinations


def get_max_type(cards: dict, hand: str) -> int:
    return max(map(get_type, all_combinations(cards, hand)))


def sorting2(cards: dict, hand: str) -> tuple:
    return get_max_type(cards, hand), get_order(cards, hand)


def part2(content: str, cards: dict) -> int:
    plays = []
    for line in content:
        hand, bid = line.split()
        plays.append((hand, int(bid)))
    plays.sort(key=lambda play: sorting2(cards, play[0]))
    ans = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        ans += bid * rank
    return ans


def main():
    filename = "day7/input.txt"
    content = get_content(filename)
    cards = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
    print(part1(content, cards))
    print(part2(content, cards))


if __name__ == "__main__":
    main()
