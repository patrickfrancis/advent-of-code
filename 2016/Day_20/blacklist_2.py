


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
    print(blacklist)

    min_possible = 0
    total_allowed = 0
    for entry in blacklist:
        if min_possible < entry[0]:
            # add gap of allowed IPs
            total_allowed += entry[0] - min_possible
            min_possible = entry[1] + 1
        elif min_possible < entry[1]:
            min_possible = entry[1] + 1
        else:
            # min_possible is already larger than upper value. Do nothing
            pass
    max_ip = 4294967295
    if min_possible < max_ip:
        total_allowed += max_ip - min_possible
    print("Total unblocked IPs: {0}".format(total_allowed))

