

if __name__ == "__main__":
    num_elves = 3012210
    elves = [1 for i in range(num_elves)]
    active_idx = 0  # index of elf whose turn it is
    remaining = num_elves  # number of elves remaining who still have presents

    while remaining > 1:
        # print("elves: {0} active: {1}".format(elves, active_idx + 1))
        if elves[active_idx] > 0:
            # find next elf who has any presents
            target_idx = (active_idx + 1) % num_elves
            while elves[target_idx] == 0:
                target_idx = (target_idx + 1) % num_elves
            # take presents
            elves[active_idx] += elves[target_idx]
            elves[target_idx] = 0
            remaining -= 1
        active_idx  = (active_idx + 1) % num_elves
    # print("final state: {0}".format(elves))
    winner = [i + 1 for i in range(len(elves)) if elves[i] > 0]
    print("Winner: {0}".format(winner))
