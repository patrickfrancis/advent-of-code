registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}


def execute(inst: str, *args) -> int:
    offset = 1
    if inst == "cpy":
        do_copy(args[0], args[1])
    elif inst == "inc":
        do_inc(args[0])
    elif inst == "dec":
        do_dec(args[0])
    elif inst == "jnz":
        offset = do_jnz(args[0], args[1])
    return offset


def do_copy(src, dest):
    if src in registers:
        val = registers[src]
    else:
        val = int(src)
    registers[dest] = val


def do_inc(reg):
    registers[reg] += 1


def do_dec(reg):
    registers[reg] -= 1


def do_jnz(src, offset) -> int:
    if src in registers:
        val = registers[src]
    else:
        val = int(src)
    if val != 0:
        return int(offset)
    else:
        return 1


if __name__ == "__main__":
    with open("Day12_input.txt") as fin:
        code = [i.strip() for i in fin.readlines()]

    pp = 0
    while 0 <= pp < len(code):
        curr = code[pp].split(" ")
        #print(curr)
        offset = execute(*curr)
        pp += offset
        #print("pp = {0}, registers = {1}".format(pp, registers))
    print("register a = {0}".format(registers['a']))
