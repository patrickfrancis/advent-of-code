import re


class Bot:
    def __init__(self, id_num: int):
        self.id = id_num
        self.chip1 = None
        self.chip2 = None
        self.low_dest = None
        self.high_dest = None

    def add_chip(self, chip_val: int):
        if not self.chip1:
            self.chip1 = chip_val
        elif not self.chip2:
            self.chip2 = chip_val
        else:
            print("ERROR: Bot {0} too many chips!".format(self.id))
            return
        self.process_chips()
        return

    def process_chips(self):
        if not (self.chip1 and self.chip2):
            return
        print("Bot {0} comparing {1} and {2}".format(self.id, self.chip1, self.chip2))
        # compare chips
        low = None
        high = None
        if self.chip1 <= self.chip2:
            low = self.chip1
            high = self.chip2
        else:
            low = self.chip2
            high = self.chip1
        # send to destinations
        self.low_dest.add_chip(low)
        self.high_dest.add_chip(high)
        self.chip1 = None
        self.chip2 = None
        return


class Output:
    def __init__(self, id_num: int):
        self.id = id_num
        self.bin = []

    def add_chip(self, chip_val: int):
        self.bin.append(chip_val)


bot_map = {}
output_map = {}
bot_pattern = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")
value_pattern = re.compile(r"value (\d+) goes to bot (\d+)")


def get_bot(num: int) -> Bot:
    if num not in bot_map:
        bot_map[num] = Bot(num)
    return bot_map[num]


def get_output(num: int) -> Output:
    if num not in output_map:
        output_map[num] = Output(num)
    return output_map[num]


if __name__ == "__main__":
    # instructions = ["value 5 goes to bot 2",
    #                 "bot 2 gives low to bot 1 and high to bot 0",
    #                 "value 3 goes to bot 1",
    #                 "bot 1 gives low to output 1 and high to bot 0",
    #                 "bot 0 gives low to output 2 and high to output 0",
    #                 "value 2 goes to bot 2"]
    with open("day10_input.txt") as fin:
        instructions = [line.strip() for line in fin.readlines()]

    # first process bot rules
    for inst in instructions:
        m = bot_pattern.match(inst)
        if m:
            bot_id = int(m.group(1))
            l_type = m.group(2)
            l_id = int(m.group(3))
            h_type = m.group(4)
            h_id = int(m.group(5))
            bot = get_bot(bot_id)
            if l_type == "bot":
                bot.low_dest = get_bot(l_id)
            else:
                bot.low_dest = get_output(l_id)
            if h_type == "bot":
                bot.high_dest = get_bot(h_id)
            else:
                bot.high_dest = get_output(h_id)
    # next process value rules
    for inst in instructions:
        m = value_pattern.match(inst)
        if m:
            val = int(m.group(1))
            b_id = int(m.group(2))
            get_bot(b_id).add_chip(val)

    print("Output:")
    for obin in output_map.values():
        print("{0}: {1}".format(obin.id, obin.bin))
