from math import factorial


class Robot:

    def get_unique_paths__(self, m: int, n: int) -> int:
        """
        Approach: Built in factorial function
        Time Complexity: O((M + N)(log(M + N)log log(M + N))^2)
        Space Complexity: O(1)
        Formulae: Binomial Coefficients
        Combination:
        C(h, h + v) = C(v, h + v) = (h + v)! / h! v!
        h = m - 1, v = n - 1
        C(h, h + v) = (m + n - 2)! / (m - 1)!(n - 1)!
        :param m:
        :param n:
        :return:
        """
        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)

    def get_unique_paths_(self, m: int, n: int) -> int:
        """
        Approach: Recursion
        Time Complexity:
        Space Complexity:
        :param m:
        :param n:
        :return:
        """
        if m == 1 or n == 1:
            return 1
        return self.get_unique_paths_(m - 1, n) + self.get_unique_paths_(m, n - 1)

    def get_unique_paths(self, m: int, n: int) -> int:
        """
        Approach: DP
        Time Complexity: O(N * M)
        Space Complexity: O(N * M)
        :param m:
        :param n:
        :return:
        """
        paths = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                paths[col][row] = paths[col - 1][row] + paths[col][row - 1]
        return paths[-1][-1]


if __name__ == "__main__":
    robot = Robot()
    print(robot.get_unique_paths(3, 7))
    print(robot.get_unique_paths__(3, 7))
    print(robot.get_unique_paths_(3, 7))