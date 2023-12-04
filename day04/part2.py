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
counts = [1] * len(all_actual)
for i, (winning, actual) in enumerate(zip(all_winning, all_actual)):
    num = len(winning.intersection(actual))
    for j in range(i + 1, i + 1 + num):
        counts[j] += counts[i]

print(sum(counts))