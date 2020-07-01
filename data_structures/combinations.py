from typing import List


class Combination:

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Back Tracking (Recursion)
        Time Complexity: O(k * c`k ,n)
        Space Complexity: O(C`k ,n)
        :param n:
        :param k:
        :return:
        """
        def back_track(left=1, curr= []):
            # base case
            if len(curr) == k:
                output.append(curr[:])
            for i in range(left, n + 1):
                curr.append(i)
                back_track(i + 1, curr)
                curr.pop()
        output = []
        back_track()
        return output

    def combine_(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Lexicographic (binary) sorted combinations
        Faster than recursion.
        Time Complexity: O(k * c`k ,n)
        Space Complexity: O(C`k ,n)
        :param n:
        :param k:
        :return:
        """
        nums = list(range(1, k + 1)) + [n + 1]
        left, output = 0, []

        while left < k:
            output.append(nums[:k])
            left = 0
            while left < k and nums[left + 1] == nums[left] + 1:
                nums[left] = left + 1
                left += 1
            nums[left] += 1
        return output


if __name__ == "__main__":
    combination = Combination()
    print(combination.combine(4, 2))
    print(combination.combine_(4, 2))
    print(combination.combine(4, 3))
    print(combination.combine_(4, 3))
