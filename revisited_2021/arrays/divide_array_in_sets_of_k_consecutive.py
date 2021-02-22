from typing import List


class Array:

    def is_possible_divide(self, nums: List[int], k: int) -> bool:
        """
        Approach: Greedy
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """
        if len(nums) % k != 0:
            return False
        if k == 1:
            return True
        # sort in ascending
        nums.sort()

        from collections import Counter
        counter = Counter(nums)
        for num in nums:
            occurence = counter[num]
            if occurence == 0:
                continue
            for i in range(k):
                if counter[num + i] < occurence:
                    # Reject
                    # -> either number (n + i) does not exist
                    # -> occurence of (n + i) is not enough to make
                    # consecutive sets with k
                    return False
                counter[num + i] -= occurence
        return True


if __name__ == "__main__":
    array = Array()
    print(array.is_possible_divide([1, 2, 3, 3, 4, 4, 5, 6], 4))
