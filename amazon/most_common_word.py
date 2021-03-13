from typing import List
from collections import defaultdict


class Word:

    def most_common(self, paragraph: str, banned: List[str]):
        """
        Approach: Single Cycle
        Time Complexity: O(N + M)
        Space Complexity: O(N + M)
        :param paragraph:
        :param banned:
        :return:
        """
        word_count = defaultdict(int)
        banned = set(banned)
        max_count = 0
        ans = ""
        word_buffer = []

        for idx, char in enumerate(paragraph):
            if char.isalnum():
                word_buffer.append(char.lower())
                # skip until you buffer a full word
                # or until you reach end of the paragraph
                if idx != len(paragraph) - 1:
                    continue
            # if there is a word in a word buffer
            # check if it is in banned list
            # if note add it to the word count dictionary
            # with number of occurrences.
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
            # reset the word buffer
            word_buffer = []
        return ans


if __name__ == "__main__":
    word = Word()
    print(word.most_common("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))