from typing import List


class Array:

    def find_k_diff_pairs(self, nums: List[int], k: int) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        result = 0
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        for num in dictionary:
            if k > 0 and num + k in dictionary:
                result += 1
            elif k == 0 and dictionary[num] > 1:
                result += 1
        return result

    def find_k_diff_pairs_(self, nums: List[int], k: int) -> int:
        """
        Approach: Two Pointers
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        nums.sort()
        n = len(nums)
        result = 0
        left, right = 0, 1

        while left < n and right < n:

            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                result += 1
                left += 1
                while left < n and nums[left - 1] == nums[left]:
                    left += 1
        return result


if __name__ == "__main__":
    array = Array()
    print(array.find_k_diff_pairs([5, 7, 4, 2], 2))
    print(array.find_k_diff_pairs([1, 1, 1, 1], 0))
    print(array.find_k_diff_pairs([1, 2, 3, 4, 5], 9))

    print(array.find_k_diff_pairs_([5, 7, 4, 2], 2))
    print(array.find_k_diff_pairs_([1, 1, 1, 1], 0))
    print(array.find_k_diff_pairs_([1, 2, 3, 4, 5], 9))