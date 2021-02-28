from typing import List


class Array:

    def maximum_sum(self, arr: List[int]) -> int:
        """
        Approach: DP (contant space)
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param arr:
        :return:
        """
        left = right = max_sum = float("-inf")
        for a in arr:
            left, right = max(a, left + a), max(left, right + a)
            max_sum = max(max_sum, right, left)
        return max_sum

    def maximum_sum_(self, arr: List[int]) -> int:
        """
        Approach: DP
        Formulae:
        ---------
        dp(i,0) = max(arr(i), dp(i - 1, 0) + arr(i))
        dp(i, 1) = max(dp(i - 1, 0), dp(i - 1, 1) + arr(i))
        Time Complexity: O()
        Space Complexity: O()
        :param arr:
        :return:
        """
        n = len(arr)
        dp = [[float("-inf")] * 2 for _ in range(n)]
        res = float("-inf")
        for i, a in enumerate(arr):
            dp[i][0] = max(a, dp[i - 1][0] + a)
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + a)
            res = max(res, *dp[i])
        return res

    def maximum_sum__(self, arr: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(3N)
        Space Complexity: O(N)
        :param arr:
        :return:
        """
        if max(arr) < 0:
            return max(arr)
        n = len(arr)
        left_sum = [0] * n
        curr_sum = float("-inf")
        for i in range(n):
            curr_sum = max(arr[i], curr_sum + arr[i])
            left_sum[i] = curr_sum

        right_sum = [0] * n
        curr_sum = best_sum = float("-inf")
        for i in range(n - 1, -1, -1):
            curr_sum = max(arr[i], curr_sum + arr[i])
            best_sum = max(best_sum, curr_sum)
            right_sum[i] = curr_sum

        for i in range(1, n - 1):
            best_sum = max(best_sum, left_sum[i - 1] + right_sum[i + 1])
        return best_sum


if __name__ == "__main__":
    array = Array()
    print(array.maximum_sum__([11, -10, -11, 8, 7, -6, 9, 4, 11, 6, 5, 0]))
    print(array.maximum_sum_([11, -10, -11, 8, 7, -6, 9, 4, 11, 6, 5, 0]))
    print(array.maximum_sum([11, -10, -11, 8, 7, -6, 9, 4, 11, 6, 5, 0]))