# Keypad
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D


def do_single_move(start: int, direction: str) -> int:
    if direction == "U":
        if start in [1, 2, 4, 5, 9]:
            return start
        elif start in [3, 13]:
            return start - 2
        else:
            return start - 4
    elif direction == "D":
        if start in [5, 9, 10, 12, 13]:
            return start
        elif start in [1, 11]:
            return start + 2
        else:
            return start + 4
    elif direction == "L":
        if start in [1, 2, 5, 10, 13]:
            return start
        else:
            return start - 1
    elif direction == "R":
        if start in [1, 4, 9, 12, 13]:
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
