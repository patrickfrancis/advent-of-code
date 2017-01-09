def generate_data(a: str) -> str:
    b = ["0" if c == "1" else "1" for c in a[::-1]]
    return "{0}0{1}".format(a, "".join(b))


def _do_checksum_step(val: str) -> str:
    checksum = []
    for i in range(0, len(val), 2):
        if val[i] == val[i+1]:
            checksum.append("1")
        else:
            checksum.append("0")
    return "".join(checksum)


def do_checksum(val: str) -> str:
    checksum = _do_checksum_step(val)
    while len(checksum) % 2 == 0:
        checksum = _do_checksum_step(checksum)
    return checksum

if __name__ == "__main__":
    disk_size = 35651584
    data = "11011110011011101"

    while len(data) < disk_size:
        data = generate_data(data)
    # print("data: {0}".format(data))
    chksum = do_checksum(data[:disk_size])
    print("checksum: {0}".format(chksum))
