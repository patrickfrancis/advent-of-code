# Keypad
# 1 2 3
# 4 5 6
# 7 8 9


def do_single_move(start: int, direction: str) -> int:
    if direction == "U":
        if start <= 3:
            return start
        else:
            return start - 3
    elif direction == "D":
        if start >= 7:
            return start
        else:
            return start + 3
    elif direction == "L":
        if start % 3 == 1:
            return start
        else:
            return start - 1
    elif direction == "R":
        if start % 3 == 0:
            return start
        else:
            return start + 1


def do_line(start: int, moves: str) -> int:
    prev = start
    result = start
    for move in moves:
        result = do_single_move(prev, move)
        prev = result
    return result


def read_bathroom_code(filename: str) -> list:
    with open(filename) as fin:
        return fin.readlines()


if __name__ == "__main__":
    #lines = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    lines = read_bathroom_code("day2_input.txt")
    prev = 5
    for line in lines:
        line = line.strip()
        result = do_line(prev, line)
        print(result)
        prev = result
