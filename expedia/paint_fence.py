class Fence:

    def number_of_ways_to_paint(self, n: int, k: int) -> int:
        """
        Approach: DP - Bottom Up (Constant Space)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :param k:
        :return:
        """

        if n == 1:
            return k

        two_posts_back = k
        one_post_back = k * k

        for i in range(3, n + 1):
            curr = (k - 1) * (one_post_back + two_posts_back)
            two_posts_back = one_post_back
            one_post_back = curr
        return one_post_back

    def number_of_ways_to_paint_(self, n: int, k: int) -> int:
        """
        Approach: DP - Bottom Up
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param k:
        :return:
        """

        if n == 1:
            return k
        if n == 2:
            return k * k

        dp = [0] * (n + 1)
        dp[1], dp[2] = k, k*k

        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[-1]

    def number_of_ways_to_paint__(self, n: int, k: int) -> int:
        """
        Approach: DP - Top Down
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param k:
        :return:
        """

        def total_ways(i: int) -> int:

            if i == 1:
                return k
            if i == 2:
                return k * k

            if i in memo:
                return memo[i]

            memo[i] = (k - 1) * (total_ways(i - 1) + total_ways(i - 2))

            return memo[i]

        memo = dict()
        return total_ways(n)


if __name__ == "__main__":
    fence = Fence()
    print(fence.number_of_ways_to_paint(3, 2))
    print(fence.number_of_ways_to_paint_(3, 2))
    print(fence.number_of_ways_to_paint__(3, 2))