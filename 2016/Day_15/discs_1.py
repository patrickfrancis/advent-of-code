class Disc:
    def __init__(self, num_pos: int, init_pos: int):
        self.num_pos = num_pos
        self.init_pos = init_pos

    def get_position(self, time: int) -> int:
        return (self.init_pos + time) % self.num_pos


if __name__ == "__main__":
    # discs = {1: Disc(5, 4),
    #          2: Disc(2, 1)}
    discs = {1: Disc(17, 15),
             2: Disc(3, 2),
             3: Disc(19, 4),
             4: Disc(13, 2),
             5: Disc(7, 2),
             6: Disc(5, 0)}

    start_time = 0
    success = False
    while not success:
        if start_time % 1000 == 0:
            print("start_time = {0}".format(start_time))
        positions = [discs[delta].get_position(start_time + delta) for delta in range(1, len(discs) + 1)]
        if all([pos == 0 for pos in positions]):
            success = True
            print("Success! start_time = {0}".format(start_time))
        start_time += 1
