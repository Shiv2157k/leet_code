import heapq


class String:

    def re_organize(self, S: str) -> str:
        """
        Approach: Heap
        Time Complexity: O(N log A)
        N - length of string
        A - size of alphabet
        Space Complexity: O(A)
        :param S:
        :return:
        """

        reorganized_string = ""
        hq = [(-S.count(ch), ch) for ch in set(S)]

        heapq.heapify(hq)
        while len(hq) > 1:
            freq_1, char_1 = heapq.heappop(hq)
            freq_2, char_2 = heapq.heappop(hq)

            reorganized_string += char_1
            reorganized_string += char_2

            if abs(freq_1) > 1:
                heapq.heappush(hq, (freq_1 + 1, char_1))
            if abs(freq_2) > 1:
                heapq.heappush(hq, (freq_2 + 1, char_2))
        while hq:
            freq, char = heapq.heappop(hq)
            return "" if abs(freq) > 1 else reorganized_string + char

        return reorganized_string


if __name__ == "__main__":
    string = String()
    print(string.re_organize("aab"))
    print(string.re_organize("aaabbbbb"))