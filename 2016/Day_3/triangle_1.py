def is_possible(sides: list) -> bool:
    longest = max(sides)
    return sum(sides) > 2*longest


if __name__ == "__main__":
    count_possible = 0
    with open("day3_input.txt") as fin:
        for line in fin:
            sides = [int(part.strip()) for part in line.split()]
            if is_possible(sides):
                count_possible += 1
    print("Possible triangles: {0}".format(count_possible))
