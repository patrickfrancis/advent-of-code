def is_possible(sides: list) -> bool:
    longest = max(sides)
    return sum(sides) > 2*longest


if __name__ == "__main__":
    col1 = []
    col2 = []
    col3 = []
    count_possible = 0
    with open("day3_input.txt") as fin:
        for line in fin:
            sides = [int(part.strip()) for part in line.split()]
            col1.append(sides[0])
            col2.append(sides[1])
            col3.append(sides[2])
    all_sides = col1 + col2 + col3
    for i in range(0, len(all_sides), 3):
        if is_possible(all_sides[i:(i+3)]):
            count_possible += 1
    print("Possible triangles: {0}".format(count_possible))
