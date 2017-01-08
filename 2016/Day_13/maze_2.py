from collections import deque

maze = {}


def compute_wall(x: int, y: int) -> bool:
    fav_num = 1358
    val = x*x + 3*x + 2*x*y + y + y*y + fav_num
    num_ones = 0
    while val > 0:
        if val % 2 > 0:
            num_ones += 1
        val >>= 1
    return num_ones % 2 == 1


def is_wall(x: int, y: int) -> bool:
    if (x,y) not in maze:
        maze[(x,y)] = compute_wall(x, y)
    return maze[(x,y)]


def get_next_locs(x:int, y:int, moves: int) -> list:
    next_locs = []
    for x_dir in [-1, 1]:
        new_x = x + x_dir
        if new_x >= 0 and not is_wall(new_x, y):
            next_locs.append((new_x, y, moves + 1))
    for y_dir in [-1, 1]:
        new_y = y + y_dir
        if new_y >= 0 and not is_wall(x, new_y):
            next_locs.append((x, new_y, moves + 1))
    return next_locs


if __name__ == "__main__":
    loc_queue = deque([(1, 1, 0)])
    visited_locs = {(1, 1)}
    max_moves = 50

    while loc_queue:
        x, y, moves = loc_queue.pop()
        if moves < max_moves:
            for (nx, ny, nm) in get_next_locs(x, y, moves):
                if (nx, ny) not in visited_locs:
                    loc_queue.appendleft((nx, ny, nm))
                    visited_locs.add((nx, ny))
        else:
            print("After {0} steps visited {1} locations".format(max_moves, len(visited_locs)))
            break


    # for y in range(45):
    #     # print("{0} ".format(y), end="")
    #     for x in range(45):
    #         wall = is_wall(x, y)
    #         if wall:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()
