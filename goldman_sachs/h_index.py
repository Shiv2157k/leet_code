from typing import List


class Array:

    def find_h_index(self, citations: List[int]) -> int:
        """
        Approach: Sorting + Binary Search
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param citations:
        :return:
        """

        if not citations:
            return 0

        citations.sort()
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if citations[pivot] == n - pivot:
                return n - pivot
            elif citations[pivot] > n - pivot:
                right = pivot - 1
            else:
                left = pivot + 1
        return n - left

    def h_index_optimized(self, citations: List[int]) -> int:
        """
        Approach: Counter
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param citations:
        :return:
        """
        if not citations:
            return 0
        n = len(citations)
        papers = [0] * (n + 1)

        # cutting off higher than n values
        # storing the citation frequency
        for citation in citations:
            papers[min(n, citation)] += 1

        k = n
        citation_sum = papers[n]

        while k > citation_sum:
            k -= 1
            citation_sum += papers[k]
        return k


if __name__ == "__main__":
    array = Array()
    print(array.find_h_index([3, 0, 6, 1, 5]))
    print(array.find_h_index([1, 3, 1]))

    print(array.h_index_optimized([3, 0, 6, 1, 5]))
    print(array.h_index_optimized([1, 3, 1]))