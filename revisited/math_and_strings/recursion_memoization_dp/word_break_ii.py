from typing import List, Dict
from collections import defaultdict


class WordBreak:

    def get_all(self, s: str, word_dict: List[str]) -> List[List[str]]:
        """
        Approach: DFS with memoization
        Time Complexity: O(N^2 + 2^N + W)
        Space Complexity: O(2^N * N + N^2 + W)
        :param s:
        :param word_dict:
        :return:
        """
        # for eliminating duplicates
        word_set = set(word_dict)
        memo = defaultdict(list)

        def word_break_top_down(s: str):

            # base case
            if not s:
                return [[]]
            # if in the cache
            if s in memo:
                return memo[s]

            # loop through each segment of the string
            for end_idx in range(1, len(s) + 1):
                word = s[:end_idx]
                if word in word_set:
                    for sub_word in word_break_top_down(s[end_idx:]):
                        memo[s].append([word] + sub_word)
            return memo[s]

        word_break_top_down(s)
        return [" ".join(words) for words in memo[s]]


if __name__ == "__main__":
    word_break = WordBreak()
    print(word_break.get_all("catsanddog", ["cat", "cats", "dog", "and", "sand", "dogs"]))