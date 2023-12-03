import re

def get_content(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content


def main():
    filename = "day1/day1.txt"
    file_content = get_content(filename)
    cals = get_cals1(file_content)
    counter = 0
    for line in file_content.splitlines():
        counter += (process_line(line))
    print(counter)

def get_cals1(cals: str) -> int:
    lines = cals.splitlines()
    counter = 0
    for line in lines:
        double = []
        line_list = [*line]
        for char in line_list:
            if char.isnumeric() and len(double) < 2:
                double.append(char)
                break
        for char in reversed(line_list):
            if char.isnumeric() and len(double) < 2:
                double.append(char)
                break
        if len(double) < 2:
            double.append(double[0])
        counter += int("".join(double))
    return counter


def get_cals2(cals: str) -> int:
    lines = cals.splitlines()
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in lines:
        double = []
        for i in range(len(numbers)):
            if numbers[i] in line and len(double) < 2:
                double.append(i + 1)
                break
        for i in range(len(numbers), 0, -1):
            if numbers[i] in line and len(double) < 2:
                counter += i + 1
                break


def process_line(line="1Here be dragons 7"):
    replacements = {
        "zerone": "zeroone",
        "oneight": "oneeight",
        "twone": "twoone",
        "sevenine": "sevennine",
        "eightwo": "eighttwo",
        "eighthree": "eightthree",
        "nineight": "nineeight",
    }

    number_table = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    retval = ""

    for replacement in replacements.keys():
        line = line.replace(replacement, replacements[replacement])

    for number in number_table:
        line = line.replace(number, number_table[number])

    matches = re.findall("\d+", line)
    first = matches[0][0]
    last = matches[-1][-1]

    answer = int(first + last)
    return answer


if __name__ == "__main__":
    main()
