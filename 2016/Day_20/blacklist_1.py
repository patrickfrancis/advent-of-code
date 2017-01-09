


if __name__ == "__main__":
    blacklist = []
    with open("day20_input.txt") as fin:
        for line in fin:
            parts = line.strip().split("-")
            x = int(parts[0])
            y = int(parts[1])
            if x > y:
                print("Found reversed pair: {0}, {1}".format(x, y))
            blacklist.append((min(x, y), max(x, y)))
    blacklist = sorted(blacklist)
    # print(blacklist)

    min_possible = 0
    for entry in blacklist:
        if min_possible < entry[0]:
            break
        elif min_possible < entry[1]:
            min_possible = entry[1] + 1
        else:
            # min_possible is already larger than upper value. Do nothing
            pass
    print("Lowest unblocked IP: {0}".format(min_possible))

