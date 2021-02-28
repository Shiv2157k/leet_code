from typing import List


class Citations:

    def get_h_index(self, citations: List[int]) -> int:
        """
        Approach: Binary Search
        Time Complexity: O(log N)
        Space Complexity: O(1)
        :param citations:
        :return:
        """
        n = len(citations)
        if not n:
            return 0
        citations.sort()
        left, right = 0, len(citations) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if citations[pivot] == n - pivot:
                return n - pivot
            elif citations[pivot] > n - pivot:
                right = pivot - 1
            else:
                left = pivot + 1
        return n - left


if __name__ == "__main__":
    cit = Citations()
    print(cit.get_h_index([3, 0, 6, 1, 5]))
    print(cit.get_h_index([0]))
    print(cit.get_h_index([0, 1]))