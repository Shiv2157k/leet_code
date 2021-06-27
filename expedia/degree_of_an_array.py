from typing import List


class Array:

    def degree(self, nums: List[int]) -> int:
        """
        Approach: Linear Scan + Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        count, left, right = {}, {}, {}

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1

        max_count = max(count.values())
        ans = len(nums)

        for num in count:
            if count[num] == max_count:
                ans = min(ans, right[num] - left[num] + 1)
        return ans


if __name__ == "__main__":
    array = Array()
    print(array.degree([1, 2, 2, 3, 1]))
    print(array.degree([1, 2, 3, 4, 5, 1, 7, 9, 1, 2, 5, 3]))
