from typing import List


class Pascal:

    def get_row(self, num_row: int) -> List[int]:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param num_row:
        :return:
        """
        row = [1] * (num_row + 1)

        for i in range(1, num_row + 1):
            for j in range(1, i):
                row[i - j] += row[i - j - 1]
        return row


if __name__ == "__main__":
    pascal = Pascal()
    print(pascal.get_row(3))
    print(pascal.get_row(4))