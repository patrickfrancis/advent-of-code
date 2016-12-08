from hashlib import md5


def check_for_digit(door_id: str, index: int) -> str:
    digest = md5("{0}{1}".format(door_id, index).encode('ascii')).hexdigest()
    if digest[0:5] == "00000":
        print("index: {0}, hash: {1}".format(index, digest))
        return digest[5]
    return ""


if __name__ == "__main__":
    password = ""
    i = 0
    while len(password) < 8:
        d = check_for_digit("reyedfim", i)
        # d = check_for_digit("abc", i)
        i += 1
        if d:
            password += d
    print("password: {0}".format(password))
