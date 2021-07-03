from typing import List
from heapq import heappop, heappush


class Words:

    def top_k_freq_words(self, words: List[str], k: int) -> List[str]:
        """
        Approach: Heap
        Time Complexity: O(log N)
        Space Complexity: O(N)
        :param words:
        :param k:
        :return:
        """

        freq_words = {}
        for word in words:
            if word not in freq_words:
                freq_words[word] = 1
            else:
                freq_words[word] += 1

        heap = []

        for word, freq in freq_words.items():
            heappush(heap, (-freq, word))

        return [heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    w = Words()
    print(w.top_k_freq_words(["i", "love", "leet", "code", "i", "love", "coding"], 2))