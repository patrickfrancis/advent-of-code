from operator import itemgetter
from collections import Counter, defaultdict


if __name__ == "__main__":
    counts = defaultdict(Counter)
    with open("day6_input.txt") as fin:
        for line in fin:
            word = line.strip()
            for index in range(len(word)):
                counts[index].update(word[index])
    letters = [pos_count.most_common()[0] for pos, pos_count in sorted(counts.items(), key=itemgetter(0))]
    print("".join([c[0] for c in letters]))
