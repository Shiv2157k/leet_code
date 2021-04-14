from typing import List


class Array:

    def delete_and_earn_(self, nums: List[int]) -> int:
        """
        Approach: DP (current and previous value) + Sorting
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        using = avoid = 0
        prev = None

        for k in sorted(counter):
            max_value = max(using, avoid)

            if k - 1 != prev:
                using = k * counter[k] + max(using, avoid)
                avoid = max_value
            else:
                using = k * counter[k] + avoid
                avoid = max_value
            prev = k
        return max(using, avoid)

    def delete_and_earn(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        if not nums:
            return 0

        frequency = [0] * (max(nums) + 1)

        for num in nums:
            frequency[num] += num

        # dp block
        dp = [0] * len(frequency)
        # initialize dp index 1
        dp[1] = frequency[1]

        # perform dp
        for idx in range(2, len(frequency)):
            dp[idx] = max(frequency[idx] + dp[idx - 2], dp[idx - 1])
        return dp[-1]


if __name__ == "__main__":

    array = Array()
    print(array.delete_and_earn([1, 1, 1, 3, 3, 9, 3, 4, 2]))
    print(array.delete_and_earn_([1, 1, 1, 3, 3, 9, 3, 4, 2]))
