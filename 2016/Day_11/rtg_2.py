from collections import deque
from copy import deepcopy
from itertools import combinations, chain


class LabState:
    def __init__(self):
        self.elevator = 1
        # maps floor num to set of items on that floor
        #self.generators = {1: set(), 2: {"H"}, 3: {"Li"}, 4: set()}
        #self.microchips = {1: {"H", "Li"}, 2: set(), 3: set(), 4: set()}
        #self.generators = {1: {"Po", "Th", "Pr", "Ru", "Co"}, 2: set(), 3: set(), 4: set()}
        #self.microchips = {1: {"Th", "Ru", "Co"}, 2: {"Po", "Pr"}, 3: set(), 4: set()}
        self.generators = {1: {"Po", "Th", "Pr", "Ru", "Co", "El", "Di"}, 2: set(), 3: set(), 4: set()}
        self.microchips = {1: {"Th", "Ru", "Co", "El", "Di"}, 2: {"Po", "Pr"}, 3: set(), 4: set()}
        self.moves = 0
        self._hash = None

    def __eq__(self, other):
        return self.elevator == other.elevator and \
               self.generators == other.generators and \
               self.microchips == other.microchips

    def __ne__(self, other):
        return self.elevator != other.elevator or \
               self.generators != other.generators or \
               self.microchips != other.microchips

    def __hash__(self):
        if self._hash is None:
            self._hash = self.elevator
            for (k,v) in self.generators.items():
                self._hash ^= hash((k, frozenset(v)))
            for (k, v) in self.microchips.items():
                self._hash ^= hash((k, frozenset(v)))
        return self._hash

    def is_valid(self) -> bool:
        if self.elevator < 1 or self.elevator > 4:
            return False
        for floor in [1, 2, 3, 4]:
            # if there are any generators, check if each chip on the floor has a matching generator
            if self.generators[floor]:
                chips = self.microchips[floor]
                for chip in chips:
                    if chip not in self.generators[floor]:
                        return False
        return True

    def is_solved(self) -> bool:
        # check if there's anything left on floors 1-3
        return sum([len(self.generators[floor]) + len(self.microchips[floor]) for floor in range(1, 4)]) == 0

    def get_next_states(self) -> list:
        dirs = []
        if self.elevator > 1:
            dirs.append(-1)
        if self.elevator < 4:
            dirs.append(1)

        valid_states = []
        for direction in dirs:
            for items in self._get_valid_items():
                new_state = deepcopy(self)
                new_state._hash = None
                new_state._do_move(direction, items[0], items[1])
                if new_state.is_valid():
                    valid_states.append(new_state)
        return valid_states

    def _get_valid_items(self) -> list:
        """
        Retuns valid combinations of microchips and generators that can be moved.
        :return: A list of two-tuples, each containing a list of microchips and a list of generators.
        """
        items = []
        m_choices = list(powerset2(self.microchips[self.elevator]))
        g_choices = list(powerset2(self.generators[self.elevator]))
        for ms in m_choices:
            for gs in g_choices:
                total = len(ms) + len(gs)
                if 1 <= total <= 2:
                    items.append((ms, gs))
        return items

    def _do_move(self, direction: int, chips: tuple, gens: tuple):
        old_floor = self.elevator
        new_floor = self.elevator + direction
        for chip in chips:
            self.microchips[old_floor].remove(chip)
            self.microchips[new_floor].add(chip)
        for gen in gens:
            self.generators[old_floor].remove(gen)
            self.generators[new_floor].add(gen)
        self.elevator += direction
        self.moves += 1


def powerset2(iterable):
    """
    Returns the powerset of the iterable, but only up to tuples of size 2.
    :param iterable:
    :return:
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in [0, 1, 2])


if __name__ == "__main__":
    state_queue = deque([LabState()])
    seen_states = {LabState()}
    num_moves = -1
    while state_queue:
        curr = state_queue.pop()

        if curr.moves > num_moves:
            num_moves = curr.moves
            print("{0}  queue = {1}, seen = {2}".format(num_moves, len(state_queue), len(seen_states)))

        for new_state in curr.get_next_states():
            if new_state.is_solved():
                print("Solved! Took {0} moves".format(new_state.moves))
                exit()
            else:
                if new_state not in seen_states:
                    state_queue.appendleft(new_state)
                    seen_states.add(new_state)
