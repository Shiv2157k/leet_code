class String:

    def __init__(self):
        self.memo = {}

    def helper(self, index, string: str):

        # base cases
        # when we reach the end
        if len(string) == index:
            return 1

        if string[index] == "0":
            return 0

        if index == len(string) - 1:
            return 1

        # check if it is in memo
        if index in self.memo:
            return self.memo[index]

        ways = self.helper(index + 1, string) + (self.helper(index + 2, string) if int(string[index: index + 2]) <= 26 else 0)

        self.memo[index] = ways
        return ways

    def decode_ways__(self, s: str) -> int:
        """
        Approach: Recursion + Memoization
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        if not s or s[0] == "0":
            return 0
        self.memo = {}
        return self.helper(0, s)

    def decode_ways_(self, s: str) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        if not s or s[0] == "0":
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            two_digit = int(s[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

    def decode_ways(self, s: str) -> str:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        if not s or s[0] == "0":
            return 0

        one_step_back = 1
        two_step_back = 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != "0":
                current = one_step_back
            two_digit = int(s[i - 1: i + 1])
            if 10 <= two_digit <= 26:
                current += two_step_back

            two_step_back = one_step_back
            one_step_back = current
        return one_step_back


if __name__ == "__main__":
    strings = String()
    print(strings.decode_ways__("12"))
    print(strings.decode_ways__("226"))

    print(strings.decode_ways_("12"))
    print(strings.decode_ways_("226"))

    print(strings.decode_ways("12"))
    print(strings.decode_ways("226"))