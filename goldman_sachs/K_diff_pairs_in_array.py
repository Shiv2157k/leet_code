from typing import List


class Array:

    def k_diff_pairs(self, nums: List[int], K: int) -> int:
        """
        Approach: Sorting + Two Pointer
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        total_pairs = 0
        left, right = 0, 1
        nums.sort()
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < K:
                right += 1
            elif nums[right] - nums[left] > K:
                left += 1
            else:
                total_pairs += 1
                left += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
        return total_pairs

    def k_diff_pairs_(self, nums: List[int], K) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """

        freq = {}
        total_pairs = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            # case 1:
            if K > 0 and num + K in freq:
                total_pairs += 1
            # case 2:
            elif K == 0 and freq[num] > 1:
                total_pairs += 1
        return total_pairs


if __name__ == "__main__":

    array = Array()
    print(array.k_diff_pairs_([3, 1, 4, 1, 5], 2))
    print(array.k_diff_pairs([3, 1, 4, 1, 5], 2))