import re


def decompress(instring: str) -> str:
    output = []
    pos = 0
    marker_pattern = re.compile(r'\((\d+)x(\d+)\)')
    while pos < len(instring):
        m = marker_pattern.search(instring, pos)
        if m:
            # add passed-over data prior to the marker
            output.append(instring[pos:m.start()])
            size = int(m.group(1))
            times = int(m.group(2))
            data = instring[m.end():m.end() + size]
            for i in range(times):
                output.append(data)
            pos = m.end() + size
        else:
            # no markers remaining
            output.append(instring[pos:])
            pos = len(instring)
    return "".join(output)


if __name__ == "__main__":
    # test_strings = ["ADVENT",
    #                "A(1x5)BC",
    #                "(3x3)XYZ",
    #                "A(2x2)BCD(2x2)EFG",
    #                "(6x1)(1x3)A",
    #                "X(8x2)(3x3)ABCY"]
    # for test in test_strings:
    #     print("input: {0}".format(test))
    #     expanded = decompress(test)
    #     print("output: {0}".format(expanded))
    #     print("length: {0}".format(len(expanded)))
    with open("day9_input.txt") as fin:
        input_string = fin.read()
        expanded = decompress(input_string.strip())
        print(len(expanded))
