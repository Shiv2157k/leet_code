from typing import List


class Matrix:

    def does_exist(self, matrix: List[List[int]], target: int) -> bool:
        """
        Approach: Binary Search
        Time Complexity: O(log mn)
        Space Complexity: O(1)
        :param matrix:
        :return:
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, (m * n) - 1
        while left <= right:
            pivot_idx = left + (right - left) // 2
            pivot_elm = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_elm:
                return True
            else:
                if target > pivot_elm:
                    left = pivot_idx + 1
                else:
                    right = pivot_idx - 1
        return False


if __name__ == "__main__":
    grid = Matrix()
    print(grid.does_exist(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 3
    ))
    print(grid.does_exist(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 9
    ))