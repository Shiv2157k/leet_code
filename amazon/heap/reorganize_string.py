import heapq


class String:

    def reorganize(self, S: str) -> str:
        """
        Approach: Greedy with Heap
        Time Complexity: O(N log A)
        N - length of S
        A - is size of alphabet
        If A is fixed, complexity is O(N)
        Space Complexity: O(A)
        If A is fixed, complexity is O(1)
        :param S:
        :return:
        """

        heap = [(-S.count(ch), ch) for ch in set(S)]

        heapq.heapify(heap)
        re_organized_string = ""

        while len(heap) > 1:
            freq1, ch1 = heapq.heappop(heap)
            freq2, ch2 = heapq.heappop(heap)

            re_organized_string += ch1
            re_organized_string += ch2

            if abs(freq1) > 1:
                heapq.heappush(heap, (freq1 + 1, ch1))
            if abs(freq2) > 1:
                heapq.heappush(heap, (freq2 + 1, ch2))

        while heapq:
            freq, ch = heapq.heappop(heap)
            return "" if abs(freq) > 1 else re_organized_string + ch
        return re_organized_string


if __name__ == "__main__":
    string = String()
    print(string.reorganize(
        "aab"
    ))
    print(string.reorganize(
        "aaabb"
    ))
    print(string.reorganize(
        "aaaaabc"
    ))