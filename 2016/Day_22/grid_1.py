from collections import namedtuple
import re

Node = namedtuple("Node", "size used avail usep")
node_pattern = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)")

if __name__ == "__main__":
    with open("day22_input.txt") as fin:
        # grab the df output, but skip the first two lines
        df = fin.readlines()[2:]

    node_map = {}
    # read data into node map
    for node_line in df:
        # parts: filesystem size used avail use%
        parts = node_line.split()
        m = node_pattern.match(parts[0])
        if not m:
            print("Invalid node name: {0}".format(parts[0]))
            continue
        x = int(m.group(1))
        y = int(m.group(2))
        size = int(parts[1].rstrip("T"))
        used = int(parts[2].rstrip("T"))
        avail = int(parts[3].rstrip("T"))
        usep = int(parts[4].rstrip("%"))
        node_map[(x,y)] = Node(size, used, avail, usep)

    # Determine viable pairs
    viable_count = 0
    for A in node_map.keys():
        for B in node_map.keys():
            A_used = node_map[A].used
            B_avail = node_map[B].avail
            if A != B and 0 < A_used <= B_avail:
                viable_count += 1
    print("{0} viable pairs".format(viable_count))
