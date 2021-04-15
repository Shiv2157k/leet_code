from typing import List


class Array:

    def is_divisible_to_k_sets(self, nums: List[int], k: int) -> bool:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """

        # edge cases
        if len(nums) % k != 0:
            return False
        if k == 1:
            return True

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in nums:
            frequency = freq[num]
            # skip case
            if frequency == 0:
                continue
            # loop for checking consecutive
            # and frequency deduction
            for i in range(k):
                if num + i not in freq or freq[num + i] < frequency:
                    # Reject
                    # -> either (n + i) doesn't exist
                    # -> occurrence of (n + i) is not enough to make consecutive sets with k
                    return False
                # after making sets, update occurrence
                freq[num + i] -= frequency
        return True


if __name__ == "__main__":
    array = Array()

    print(array.is_divisible_to_k_sets([1, 2, 3, 3, 4, 4, 5, 6], k=4))
    print(array.is_divisible_to_k_sets([1, 2, 3, 3, 4, 4, 5, 6, 8, 9], k=4))
    print(array.is_divisible_to_k_sets([1, 1, 1, 1, 2, 3], k=3))
