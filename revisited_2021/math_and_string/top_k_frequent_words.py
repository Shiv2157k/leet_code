import heapq
from typing import List


class Words:

    def get_top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
        Approach: Heap
        Time Complexity: O(N log K)
        Space Complexity: O(N)
        :param words:
        :param k:
        :return:
        """
        # validation
        if not words or k <= 0:
            return []
        word_frequency = dict()
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        heap = []
        for word, freq in word_frequency.items():
            heapq.heappush(heap, (-freq, word))

        return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    w = Words()
    print(w.get_top_k_frequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    ))
    print(w.get_top_k_frequent(
        ["i", "love", "leetcode", "i", "love", "coding"], 2
    ))