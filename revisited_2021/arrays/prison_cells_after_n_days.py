from typing import List


class Prison:

    # To Do - Using Bit Map

    def next_day(self, cells: List[int]) -> List[int]:
        """

        :param cells:
        :return:
        """
        cycle = [0]
        for i in range(1, len(cells) - 1):
            cycle.append(int(cells[i - 1] == cells[i + 1]))
        cycle.append(0)
        return cycle

    def cells_after_n_days(self, cells: List[int], n: int) -> List[int]:
        """
        Approach: Hash Table
        Time Complexity: O(k * min(N, 2^k))
        Space Complexity: O(K * 2^K)
        :param cells:
        :param n:
        :return:
        """
        seen = {}
        fast_forwarded = False

        while n:
            if not fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    n %= seen[state_key] - n
                    fast_forwarded = True
                else:
                    seen[state_key] = n
            if n > 0:
                n -= 1
                next_day_cells = self.next_day(cells)
                cells = next_day_cells
        return cells


if __name__ == "__main__":
    prison = Prison()
    print(prison.cells_after_n_days([0, 1, 0, 1], 6))
