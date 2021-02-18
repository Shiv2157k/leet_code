from typing import List, Tuple

from pprint import pprint


class CoinsOnClock:
    # work on this again

    coin_values = {"P": 1, "N": 5, "D": 10}
    clock_size = 12

    def verify(self, sequence: List[str]) -> bool:
        coins_on_clock = [None] * self.clock_size
        position = 0
        for coin in sequence:
            position = (position + self.coin_values[coin]) % self.clock_size
            if coins_on_clock[position]:
                return False
            coins_on_clock[position] = coin
        return True

    def find_all_sequence(self, sequence: List[str], pennies: int, nickles: int, dimes: int):
        if pennies < 0 or nickles < 0 or dimes < 0:
            return []
        if self.verify(sequence):
            if len(sequence) == self.clock_size:
                return [sequence]
            else:
                return(
                    self.find_all_sequence(sequence + ["P"], pennies - 1, nickles, dimes) +
                    self.find_all_sequence(sequence + ["N"], pennies, nickles - 1, dimes) +
                    self.find_all_sequence(sequence + ["D"], pennies, nickles, dimes - 1)
                )
        else:
            return []

    def value(self, start: int, sequence: List[str]):
        coins_on_clock = [None] * self.clock_size
        position = start - 1
        for coin in sequence:
            position = (position + self.coin_values[coin]) % self.clock_size
            coins_on_clock[position] = coin
        return sum(map(lambda v: self.coin_values[coins_on_clock[v]] * (v + 1), range(self.clock_size)))

    def max_value(self, solutions: List[List[str]]) -> Tuple[int, List[str]]:
        max_value = 0
        best_solutions = []
        for solution in solutions:
            for start in range(1, self.clock_size + 1):
                val = self.value(start, solution)
                if val > max_value:
                    max_value = val
                    best_solutions += [(start, solution)]
                elif val == max_value:
                    best_solutions += [(start, solution)]
        return max_value, best_solutions

    def min_value(self, solutions: List[List[str]]) -> Tuple[int, List[str]]:
        min_value = float("inf")
        best_solutions = []
        for solution in solutions:
            for start in range(1, self.clock_size + 1):
                val = self.value(start, solution)
                if val < min_value:
                    min_value = val
                    best_solutions += [(start, solution)]
                elif val == min_value:
                    best_solutions += [(start, solution)]
        return min_value, best_solutions


if __name__ == "__main__":
    clock = CoinsOnClock()
    solutions = clock.find_all_sequence([], 2, 5, 5)
    # pprint(clock.value(1, ['D', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']))
    pprint(clock.max_value(solutions))
    pprint(clock.min_value(solutions))