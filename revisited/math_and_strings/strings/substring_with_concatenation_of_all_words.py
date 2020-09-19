from typing import List
from collections import defaultdict, Counter


class SubstringConcatenation:

    def get_all_indices(self, string: str, words: List[str]) -> List[int]:
        """
        Approach: Sliding Window
        Time Complexity: O(wl * total_words * word_length)
        Space Complexity: O(N)
        :param string:
        :param words:
        :return:
        """
        # word_counter - to keep note of words and their repetitions.
        word_counter = Counter(words)
        # length of word in words
        word_length = len(words[0])
        # number of words in words list
        total_words = len(words)
        # indices: to output the valid indices
        indices = []

        for wl in range(word_length):
            left = wl
            count = 0
            word_tracker = defaultdict(int)
            for ch in range(wl, len(string) - word_length + 1, word_length):
                word = string[ch: ch + word_length]
                if word in word_counter:
                    word_tracker[word] += 1
                    count += 1
                    while word_tracker[word] > word_counter[word]:
                        word_tracker[string[left: left + word_length]] -= 1
                        left += word_length
                        count -= 1
                    if count == total_words:
                        indices.append(left)
                else:
                    left = ch + word_length
                    count = 0
                    word_tracker = defaultdict(int)
        return indices


if __name__ == "__main__":
    substring_concat = SubstringConcatenation()
    print(substring_concat.get_all_indices("barfoothefoobarman", ["foo", "bar"]))
    print(substring_concat.get_all_indices("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(substring_concat.get_all_indices("barfoofoobarthefoobarman", ["bar", "foo", "the"]))