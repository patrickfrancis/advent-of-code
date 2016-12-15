import re


marker_pattern = re.compile(r'\((\d+)x(\d+)\)')


def decompress(instring: str) -> str:
    output = []
    output_size = 0
    pos = 0
    while pos < len(instring):
        m = marker_pattern.search(instring, pos)
        if m:
            # add passed-over data prior to the marker
            output_size += len(instring[pos:m.start()])
            # add the size of the decompressed chunk
            size = int(m.group(1))
            times = int(m.group(2))
            data = instring[m.end():m.end() + size]
            sub_size = decompress(data)
            output_size += sub_size * times
            # advance past the chunk
            pos = m.end() + size
        else:
            # no markers remaining
            output_size += len(instring[pos:])
            pos = len(instring)
    return output_size


if __name__ == "__main__":
    # test_strings = ["(3x3)XYZ",
    #                 "X(8x2)(3x3)ABCY",
    #                 "(27x12)(20x12)(13x14)(7x10)(1x12)A",
    #                 "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]
    # for test in test_strings:
    #     print("input: {0}".format(test))
    #     expanded_len = decompress(test)
    #     print("decompressed length: {0}".format(expanded_len))

    with open("day9_input.txt") as fin:
        input_string = fin.read()
        expanded_len = decompress(input_string.strip())
        print(expanded_len)
