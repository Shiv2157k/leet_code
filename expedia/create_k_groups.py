

class People:

    def into_k_groups(self, n: int, g: int) -> int:
        """
        Approach: DP
        Time Complexity:
        Space Complexity:
        Link:
        https://math.stackexchange.com/questions/1908701/integer-partition-of-n-into-k-parts-recurrence
        :param n:
        :param g:
        :return:
        """

        if n < g:
            return 0

        dp = [[0] * (g + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][1] = 1

        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(2, g + 1):
                dp[i][j] = dp[i - 1][j - 1]
                if i >= 2 * j:
                    dp[i][j] += dp[i - j][j]
        print (dp)
        return dp[-1][-1]


if __name__ == "__main__":

    people = People()
    print(people.into_k_groups(8, 3))
    print(people.into_k_groups(7, 4))
    print(people.into_k_groups(7, 2))

    print(people.into_k_groups(5, 3))