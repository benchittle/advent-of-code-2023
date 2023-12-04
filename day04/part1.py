import re

num = re.compile(r"\d+")

with open("input.txt") as f:
    text = f.read().split("\n")

all_winning: list[set] = []
all_actual: list[set] = []

for line in text:
    cardnum, cards = line.split(": ")
    winning, actual = cards.split(" | ")

    winning = set(map(int, num.findall(winning)))
    actual = set(map(int, num.findall(actual)))

    all_winning.append(winning)
    all_actual.append(actual)

total = 0
for winning, actual in zip(all_winning, all_actual):
    intersection = winning.intersection(actual)
    if intersection:
        total += 2 ** (len(intersection) - 1)

print(total)