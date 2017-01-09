import re


def swap_position(word: str, x: int, y: int) -> str:
    lower = min(x, y)
    upper = max(x, y)
    return "{0}{1}{2}{3}{4}".format(word[:lower], word[upper], word[lower+1:upper], word[lower], word[upper+1:])


def swap_letters(word: str, x: str, y: str) -> str:
    word = word.replace(x, "Z")
    word = word.replace(y, x)
    return word.replace("Z", y)


def rotate_left(word: str, amount: int) -> str:
    amount = amount % len(word)
    return "{0}{1}".format(word[amount:], word[:amount])


def rotate_right(word: str, amount: int) -> str:
    amount = amount % len(word)
    return "{0}{1}".format(word[-amount:], word[:-amount])


def rotate_on_position(word: str, letter: str) -> str:
    idx = word.find(letter)
    amount = 1 + idx
    if idx >= 4:
        amount += 1
    return rotate_right(word, amount)


def reverse_range(word: str, lower: int, upper: int) -> str:
    if lower > 0:
        return "{0}{1}{2}".format(word[:lower], word[upper:lower-1:-1], word[upper+1:])
    else:
        return "{0}{1}{2}".format(word[:lower], word[upper::-1], word[upper + 1:])


def move(word: str, x: int, y: int) -> str:
    letter = word[x]
    word_list = list(word)
    del word_list[x]
    word_list.insert(y, letter)
    return "".join(word_list)


if __name__ == "__main__":
    # print(swap_position("abcde", 0, 4))
    # print(swap_letters("abcde", "d", "b"))
    # print(rotate_left("abcde", 1))
    # print(rotate_right("abcde", 2))
    # print(rotate_on_position("abdec", "b"))
    # print(rotate_on_position("ecabd", "d"))
    # print(reverse_range("abcde", 0, 3))
    # print(move("bcdea", 1, 4))
    # print(move("bdeac", 3, 0))

    password = "abcdefgh"
    with open("day21_input.txt") as fin:
        moves = [i.strip() for i in fin.readlines()]

    sp_pat = re.compile(r"swap position (\d+) with position (\d+)")
    sl_pat = re.compile(r"swap letter (\w+) with letter (\w+)")
    rl_pat = re.compile(r"rotate left (\d+) steps?")
    rr_pat = re.compile(r"rotate right (\d+) steps?")
    rp_pat = re.compile(r"rotate based on position of letter (\w+)")
    rev_pat = re.compile(r"reverse positions (\d+) through (\d+)")
    mov_pat = re.compile(r"move position (\d+) to position (\d+)")

    scramble = password
    for inst in moves:
        print(scramble)
        print(inst)
        m = sp_pat.match(inst)
        if m:
            scramble = swap_position(scramble, int(m.group(1)), int(m.group(2)))
            continue
        m = sl_pat.match(inst)
        if m:
            scramble = swap_letters(scramble, m.group(1), m.group(2))
            continue
        m = rl_pat.match(inst)
        if m:
            scramble = rotate_left(scramble, int(m.group(1)))
            continue
        m = rr_pat.match(inst)
        if m:
            scramble = rotate_right(scramble, int(m.group(1)))
            continue
        m = rp_pat.match(inst)
        if m:
            scramble = rotate_on_position(scramble, m.group(1))
            continue
        m = rev_pat.match(inst)
        if m:
            scramble = reverse_range(scramble, int(m.group(1)), int(m.group(2)))
            continue
        m = mov_pat.match(inst)
        if m:
            scramble = move(scramble, int(m.group(1)), int(m.group(2)))
            continue
    print("scrambled password: {0}".format(scramble))
