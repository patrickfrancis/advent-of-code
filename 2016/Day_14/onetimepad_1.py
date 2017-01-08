import re
from hashlib import md5

triple_pattern = re.compile(r'([a-z0-9])\1\1')
# five_pattern   = re.compile(r'([a-z0-9])\1\1\1\1')

salt = "ngcjuoqr"
hashes = {}


def get_hash(index: int) -> str:
    if index not in hashes:
        hash_val = md5("{0}{1}".format(salt, index).encode('ascii')).hexdigest().lower()
        hashes[index] = hash_val
    return hashes[index]


def is_key(index: int) -> bool:
    m = triple_pattern.search(get_hash(index))
    if not m:
        return False
    val = m.group(1)
    #print("Index {0} has triple character: {1}".format(index, val*3))
    search_string = val*5
    for i in range(index + 1, index + 1001):
        test_hash = get_hash(i)
        if search_string in test_hash:
            #print("Matching 5-string found in index {0}".format(i))
            return True
    return False


if __name__ == "__main__":
    # print(is_key(18))
    # print(is_key(39))
    # print(is_key(92))
    # print(is_key(22728))

    key_indices = []
    curr_index = 0
    while len(key_indices) < 64:
        if is_key(curr_index):
            key_indices.append(curr_index)
        curr_index += 1
    print("64th key at index {0}".format(key_indices[63]))
