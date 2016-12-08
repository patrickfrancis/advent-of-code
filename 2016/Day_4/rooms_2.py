from collections import Counter
from operator import itemgetter
import re
import string


def is_real(name: str, checksum: str) -> bool:
    if len(checksum) != 5:
        return False
    letter_count = Counter([c for c in name if c != "-"])
    # first sort letter alphabetically
    temp_sort = sorted(letter_count.most_common(), key=itemgetter(0))
    # next sort by count. Ties will stay in alphabetical order
    most_common = sorted(temp_sort, key=itemgetter(1), reverse=True)
    #print(most_common)
    for i in range(5):
        if checksum[i] != most_common[i][0]:
            return False
    return True


def get_parts(full_string: str) -> (str, int, str):
    """

    :param full_string:
    :return: A tuple of the name, id, and checksum
    """
    m = re.match("([a-z\-]+)-(\d+)\[([a-z]+)\]", full_string)
    return m.group(1), int(m.group(2)), m.group(3)


def shift_letter(letter: str, amount: int) -> str:
    if letter == "-":
        return " "
    index = string.ascii_lowercase.index(letter)
    return string.ascii_lowercase[(index + amount) % 26]


def decrypt(name: str, sector_id: int) -> str:
    new_letters = [shift_letter(letter, sector_id) for letter in name]
    return "".join(new_letters)


if __name__ == "__main__":
    #print(is_real("aaaaa-bbb-z-y-x", "abxyz"))
    with open("day4_input.txt") as fin:
        for line in fin:
            name, sector_id, checksum = get_parts(line.strip())
            if is_real(name, checksum):
                print("{0}: {1}".format(decrypt(name, sector_id), sector_id))
