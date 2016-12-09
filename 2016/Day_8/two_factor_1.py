import re

num_rows = 6
num_columns = 50


def print_display(array):
    for row in array:
        print("".join(row))


def rect(array, height, width):
    for i in range(height):
        for j in range(width):
            array[i][j] = "#"


def rotate_column(array, col, amount):
    old_column = [array[i][col] for i in range(num_rows)]
    for row in range(num_rows):
        array[(row + amount) % num_rows][col] = old_column[row]


def rotate_row(array, row, amount):
    old_row = array[row].copy()
    for col in range(num_columns):
        array[row][(col + amount) % num_columns] = old_row[col]


if __name__ == "__main__":
    display = [["." for x in range(num_columns)] for y in range(num_rows)]
    # print_display(display)
    # print()
    # rect(display, 3, 2)
    # print_display(display)
    # print()
    # rotate_column(display, 1, 1)
    # print_display(display)
    # print()
    # rotate_row(display, 0, 4)
    # print_display(display)
    # print()
    # rotate_column(display, 1, 1)
    # print_display(display)

    rect_pattern = re.compile(r'rect (\d+)x(\d+)')
    rot_col_pattern = re.compile(r'rotate column x=(\d+) by (\d+)')
    rot_row_pattern = re.compile(r'rotate row y=(\d+) by (\d+)')
    with open("day8_input.txt") as fin:
        for line in fin:
            # print(line.strip())
            if line.startswith("rect"):
                m = re.match(rect_pattern, line)
                rect(display, int(m.group(2)), int(m.group(1)))
            elif line.startswith("rotate column"):
                m = re.match(rot_col_pattern, line)
                rotate_column(display, int(m.group(1)), int(m.group(2)))
            elif line.startswith("rotate row"):
                m = re.match(rot_row_pattern, line)
                rotate_row(display, int(m.group(1)), int(m.group(2)))
            else:
                print("ERROR: UNKNOWN COMMAND")
    print_display(display)
    total_lit = sum([display[i][j] == "#" for i in range(num_rows) for j in range(num_columns)])
    print("Total lit pixels: {0}".format(total_lit))
