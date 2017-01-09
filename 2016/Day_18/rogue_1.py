def is_trap(left: bool, center: bool, right: bool) -> bool:
    if (left and center and not right) or (not left and center and right):
        return True
    elif (left and not center and not right) or (not left and not center and right):
        return True
    else:
        return False


def print_room(room):
    for row_num in range(len(room)):
        print("".join(["^" if t else "." for t in room[row_num]]))


if __name__ == "__main__":
    # room = [[False, False, True, True, False]]
    with open("day18_input.txt") as fin:
        start_row = [True if c == "^" else False for c in fin.readline().strip()]
    room = [start_row]
    max_rows = 40

    for row_num in range(max_rows - len(room)):
        prev_row = room[-1]
        new_row = []
        for i in range(len(prev_row)):
            left = prev_row[i-1] if i-1 >= 0 else False
            center = prev_row[i]
            right = prev_row[i+1] if i+1 < len(prev_row) else False
            new_row.append(is_trap(left, center, right))
        room.append(new_row)
    print_room(room)
    print("Safe tiles = {0}".format(sum([not trap for row in room for trap in row])))
