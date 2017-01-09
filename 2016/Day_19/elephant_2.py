from math import floor

if __name__ == "__main__":
    num_elves = 3012210
    elves = [(i + 1, 1) for i in range(num_elves)]  # tuple of ID and num presents
    active_idx = 0  # index of elf whose turn it is

    while len(elves) > 1:
        # print("elves: {0} active_idx: {1}".format(elves, active_idx))

        # find next elf who has any presents
        target_idx = (active_idx + floor(len(elves)/2)) % len(elves)
        # take presents
        target_elf = elves[target_idx]
        active_elf = elves[active_idx]
        elves[active_idx] = (active_elf[0], active_elf[1] + target_elf[1])
        # elves.remove(target_elf)
        del elves[target_idx]
        if target_idx < active_idx:
            active_idx -= 1
        # advance to next elf
        active_idx = (active_idx + 1) % len(elves)
    print("final state: {0}".format(elves))
    # winner = [i + 1 for i in range(len(elves)) if elves[i] > 0]
    # print("Winner: {0}".format(winner))
