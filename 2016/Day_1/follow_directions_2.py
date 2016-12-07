import re


class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0 # 0 = N, 1 = E, 2 = S, 3 = W
        self.visited_locations = {(0, 0)}

    def follow_directions(self, moves: list):
        for move in moves:
            repeat_loc = self.do_move(move)
            if repeat_loc:
                return repeat_loc

    def do_move(self, move: str):
        m = re.match("([R|L])(\d+)", move)
        if m:
            turn_dir = m.group(1)
            distance = int(m.group(2))
            # process turn
            if turn_dir == "R":
                self.direction = (self.direction + 1) % 4
            elif turn_dir == "L":
                self.direction -= 1
                if self.direction < 0:
                    self.direction = 3
            # process travel
            for i in range(distance):
                self.move_single_block()
                if (self.x, self.y) in self.visited_locations:
                    return (self.x, self.y)
                else:
                    self.visited_locations.add((self.x, self.y))
            # no intersection found
            return None

    def move_single_block(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 3:
            self.x -= 1


def read_moves(filename):
    with open(filename) as input_file:
        moves_string = input_file.readline()
    return [move.strip() for move in moves_string.split(",")]


if __name__ == "__main__":
    t = Turtle()
    moves = read_moves("day1_input.txt")
    #moves = ["R5", "L5", "R5", "R3"]
    #moves = ["R8", "R4", "R4", "R8"]
    result = t.follow_directions(moves)
    print("result = {0}".format(result))
    print("x = {0}, y = {1}".format(t.x, t.y))
    if result:
        total = abs(result[0]) + abs(result[1])
    else:
        total = abs(t.x) + abs(t.y)
    print("total = {0}".format(total))

