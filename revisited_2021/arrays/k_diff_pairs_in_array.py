from typing import List


class Array:

    def k_diff_pairs(self, nums: List[int], k: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        left, right, result = 0, 1, 0
        nums.sort()
        n = len(nums)
        while left < n and right < n:
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                result += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1
        return result

    def k_diff_pairs_(self, nums: List[int], k: int) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        from collections import Counter
        counter = Counter(nums)
        result = 0
        for key in counter:
            if k > 0 and key + k in counter:
                result += 1
            elif k == 0 and counter[key] > 1:
                result += 1
        return result


if __name__ == "__main__":
    array = Array()
    print(array.k_diff_pairs([1, 2, 3, 1, 5], 2))
    print(array.k_diff_pairs([1, 2, 3, 4], 1))
    print(array.k_diff_pairs([1, 1, 1, 1], 0))
    print(array.k_diff_pairs_([1, 2, 3, 1, 5], 2))
    print(array.k_diff_pairs_([1, 2, 3, 4], 1))
    print(array.k_diff_pairs_([1, 1, 1, 1], 0))