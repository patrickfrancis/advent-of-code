from hashlib import md5
from collections import deque

# passcode = "ihgpwlah"
# passcode = "kglvqrro"
# passcode = "ulqzkmiv"
passcode = "pgflpeqp"
open_vals = ['b', 'c', 'd', 'e', 'f']


def get_next_states(path: str, x: int, y: int) -> list:
    next_states = []
    door_status = md5((passcode + path).encode("ascii")).hexdigest().lower()
    # move up
    if y > 0 and door_status[0] in open_vals:
        next_states.append((path + "U", x, y - 1))
    # move down
    if y < 3 and door_status[1] in open_vals:
        next_states.append((path + "D", x, y + 1))
    # move left
    if x > 0 and door_status[2] in open_vals:
        next_states.append((path + "L", x - 1, y))
    # move right
    if x < 3 and door_status[3] in open_vals:
        next_states.append((path + "R", x + 1, y))
    return next_states


if __name__ == "__main__":
    state_queue = deque([("", 0, 0)])
    success_paths = []

    while state_queue:
        (path, x, y) = state_queue.pop()
        if x == 3 and y == 3:
            # print("Success! path = {0}".format(path))
            success_paths.append(path)
        else:
            for new_state in get_next_states(path, x, y):
                state_queue.appendleft(new_state)
    print("Number of success paths: {0}".format(len(success_paths)))
    print("Length of last success path: {0}".format(len(success_paths[-1])))
