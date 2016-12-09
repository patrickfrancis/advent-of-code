import re

abba_pattern = re.compile(r'([a-z])((?!\1)[a-z])\2\1')


def supports_tls(address: str) -> bool:
    #print(address)
    global abba_pattern
    parts = re.findall("[a-z]+|\[[a-z]+\]", address)
    good_abba = False
    bad_abba = False
    for part in parts:
        if re.search(abba_pattern, part):
            if part.startswith("["):
                bad_abba = True
            else:
                good_abba = True
    return good_abba and not bad_abba


if __name__ == "__main__":
    tls_count = 0
    with open("day7_input.txt") as fin:
        for line in fin:
            if supports_tls(line.strip()):
                tls_count += 1
    print("tls count: {0}".format(tls_count))
