from typing import List
from collections import Counter, defaultdict


class SubstringConcatenation:

    def find_all_indices(self, s: str, words: List[str]) -> List[int]:
        """
        Approach: Sliding Window
        Time Complexity: O(wl * total_words * word_length)
        Space Complexity: O(N)
        :param s:
        :param words:
        :return:
        """

        # to keep track of word repetition
        word_counter = Counter(words)
        # total number of words given
        total_words = len(words)
        # length of each word
        word_length = len(words[0])
        indices = []

        # loop through the word length like a sliding window
        for wl in range(word_length):
            left = wl
            count = 0
            subd = defaultdict(int)

            # loop through the words in string s
            # start index, end index, step
            for idx in range(wl, len(s) - word_length + 1, word_length):
                # get a word from string
                word = s[idx: idx + word_length]
                # if this is a valid word
                if word in word_counter:
                    # add it to subd with a counter
                    subd[word] += 1
                    # increment the counter by 1
                    count += 1
                    # if the repetition in subd is more, minus the counter and slide
                    while subd[word] > word_counter[word]:
                        subd[s[left: left + word_length]] -= 1
                        # got the new start
                        left += word_length
                        # go back one step with the counter
                        count -= 1
                    # if the counter reached the total words
                    # add the start index into list
                    if count == total_words:
                        indices.append(left)
                # if it is not a valid word
                else:
                    # move on and reset the counter
                    left = idx + word_length
                    subd = defaultdict(int)
                    count = 0
        return indices


if __name__ == "__main__":
    substring = SubstringConcatenation()
    print(substring.find_all_indices("barfoothefoobarman", ["foo", "bar"]))
    print(substring.find_all_indices("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(substring.find_all_indices("barfoofoobarthefoobarman", ["bar", "foo", "the"]))

