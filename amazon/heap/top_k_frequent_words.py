import heapq
from typing import List


class Words:

    def get_top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
        Approach: Heap + Hash table
        Time Complexity: O(N + k log N)
        Space Complexity: O(N)
        :param words:
        :param k:
        :return:
        """
        # validation
        if not words or k <= 0:
            return []
        word_freq = dict()
        for word in words:
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1
        heap = []
        for word, freq in word_freq.items():
            heapq.heappush(heap, (-freq, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    w = Words()
    print(w.get_top_k_frequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 3
    ))