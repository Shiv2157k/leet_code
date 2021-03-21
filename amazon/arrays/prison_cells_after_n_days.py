from typing import List


class Prison:

    def cells_after_n_days(self, cells: List[int], n: int) -> List[int]:
        """
        Approach: Simulation with Fast Forward
        Time Complexity:
        Space Complexity:
        :param cells:
        :param n:
        :return:
        """
        is_fast_forward = False
        seen = dict()

        while n:
            if not is_fast_forward:
                state_key = tuple(cells)
                if state_key in seen:
                    n %= seen[state_key] - n
                    is_fast_forward = True
                else:
                    seen[state_key] = n
            if n > 0:
                n -= 1
                next_day_cells = self.next_cycle(cells)
                cells = next_day_cells
        return cells

    def next_cycle(self, cells: List[int]) -> List[int]:
        cycle = [0] # head
        for i in range(1, len(cells) - 1):
            cycle.append(int(cells[i - 1] == cells[i + 1]))
        cycle.append(0) # tail
        return cycle


if __name__ == "__main__":
    prison = Prison()
    print(prison.cells_after_n_days(
        [0, 1, 0, 1, 1, 0, 0, 1], 7
    ))