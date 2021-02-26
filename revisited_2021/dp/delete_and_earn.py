from typing import List


class Array:

    def delete_and_earn(self, nums: List[int]) -> int:
        """
        Approach: DP
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :return:
        """
        # from collections import Counter
        # counter = Counter(nums)
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        prev = None
        seen = current = 0
        for num in sorted(counter):
            if num - 1 != prev:
                seen, current = max(seen, current), num * counter[num] + max(seen, current)
            else:
                seen, current = max(seen, current), num * counter[num] + seen
            prev = num
        return max(seen, current)


if __name__ == "__main__":
    array = Array()
    print(array.delete_and_earn([2, 3, 3, 3, 4]))