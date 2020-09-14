

class Decode:

    def __init__(self):
        self.memo = {}

    def number_of_ways(self, string: str) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """

        if not string:
            return 0

        dp = [0 for _ in range(len(string) + 1)]
        dp[0] = 1
        dp[1] = 0 if string[0] == "0" else 1

        for i in range(2, len(dp)):
            if string[i - 1] != "0":
                dp[i] += dp[i - 1]
            two_digit = int(string[i - 2: i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        return dp[len(string)]

    def memoization(self, index: int, string: str) -> int:

        # if index is equals to length of string
        # break the recursion by returning 1
        if len(string) == index:
            return 1

        # if given string index has 0 it is not valid fr decoding
        # return 0
        if string[index] == "0":
            return 0

        if index == len(string) - 1:
            return 1

        if index in self.memo:
            return self.memo[index]
        # recursion call
        ans = self.memoization(index + 1, string) + (self.memoization(index + 2, string) if (int(string[index: index + 2]) <= 26) else 0)
        # save it for memoization
        self.memo[index] = ans
        return ans

    def get_number_of_ways(self, string: str) -> int:
        if not string:
            return 0

        return self.memoization(0, string)


if __name__ == "__main__":
    decode = Decode()
    decode_obj = Decode()
    print(decode.get_number_of_ways("326"))
    print(decode_obj.get_number_of_ways("226"))
    print(decode.number_of_ways("326"))
    print(decode_obj.number_of_ways("226"))