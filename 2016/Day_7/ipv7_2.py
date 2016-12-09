import re

aba_pattern = re.compile(r'(?=([a-z])((?!\1)[a-z])\1)')


def supports_ssl(address: str) -> bool:
    #print(address)
    global aba_pattern
    parts = re.findall("[a-z]+|\[[a-z]+\]", address)
    supers = set()
    hypers = set()
    # grab all the ABAs from the supernet and hypernet sections
    for part in parts:
        abas = ["{0}{1}{0}".format(aba[0], aba[1]) for aba in re.findall(aba_pattern, part)]
        if part.startswith("["):
            hypers.update(abas)
        else:
            supers.update(abas)
    # test for any ABA/BAB pairs
    for aba in supers:
        bab = "{0}{1}{0}".format(aba[1], aba[0])
        #print("aba: {0}, bab: {1}".format(aba, bab))
        if bab in hypers:
            return True
    return False


if __name__ == "__main__":
    ssl_count = 0
    with open("day7_input.txt") as fin:
        for line in fin:
            if supports_ssl(line.strip()):
                ssl_count += 1
    print("ssl count: {0}".format(ssl_count))
    # print(supports_ssl("aba[bab]xyz"))
    # print(supports_ssl("xyx[xyx]xyx"))
    # print(supports_ssl("aaa[kek]eke"))
    # print(supports_ssl("zazbz[bzb]cdb"))
