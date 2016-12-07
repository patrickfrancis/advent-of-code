import re
x = 0
y = 0
direction = 0  # 0 = N, 1 = E, 2 = S, 3 = W


def read_moves(filename):
    with open(filename) as input_file:
        moves_string = input_file.readline()
    return [move.strip() for move in moves_string.split(",")]


def do_move(move: str):
    global direction, x, y
    m = re.match("([R|L])(\d+)", move)
    if m:
        turn_dir = m.group(1)
        distance = int(m.group(2))
        # process turn
        if turn_dir == "R":
            direction = (direction + 1) % 4
        elif turn_dir == "L":
            direction -= 1
            if direction < 0:
                direction = 3
        # process travel
        if direction == 0:
            y += distance
        elif direction == 2:
            y -= distance
        elif direction == 1:
            x += distance
        elif direction == 3:
            x -= distance


if __name__ == "__main__":
    moves = read_moves("day1_input.txt")
    #moves = ["R5", "L5", "R5", "R3"]
    for move in moves:
        do_move(move)
    print("x = {0}, y = {1}".format(x, y))
    total = abs(x) + abs(y)
    print("total = {0}".format(total))
