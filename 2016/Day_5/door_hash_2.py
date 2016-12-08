from hashlib import md5


def check_for_digit(door_id: str, index: int) -> (int, str):
    digest = md5("{0}{1}".format(door_id, index).encode('ascii')).hexdigest()
    if digest[0:5] == "00000":
        position = digest[5]
        if position.isdigit() and int(position) < 8:
            print("index: {0}, hash: {1}".format(index, digest))
            digit = digest[6]
            return int(position), digit
    return None


if __name__ == "__main__":
    password = ["_" for i in range(8)]
    digit_count = 0
    i = 0
    while digit_count < 8:
        result = check_for_digit("reyedfim", i)
        #result = check_for_digit("abc", i)
        if result:
            pos = result[0]
            d = result[1]
            if password[pos] == "_":
                password[pos] = d
                print("password: {0}".format("".join(password)))
                digit_count += 1
        # d = check_for_digit("abc", i)
        i += 1
