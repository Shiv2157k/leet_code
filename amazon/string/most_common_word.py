from typing import List

from collections import defaultdict


class Paragraph:

    def get_most_common_word(self, para: str, banned: List[str]) -> str:
        """
        Approach: Single Cycle
        Time Complexity: O(N + M)
            - O(N) for traversing i/p string once & only once.
            - if we combine all string building operations all
              together, in total it would take another O(N) time.
            - In addition, we built a set out of the list of banned
              words, which would take another O(M) time.
            - O(N) + O(N) + O(M) = O(N + M)
        Space Complexity: O(N + M)
            - O(N) to build a hash map for counting frequency of each
              unique word.
            - O(M) for building word set our of banned word list.
            - over all O(N + M).
        :param para:
        :param banned:
        :return:
        """
        banned = set(banned)
        word_buffer = []
        word_count = defaultdict(int)
        most_common_word = ""
        max_count = 0

        for i, ch in enumerate(para):
            if ch.isalnum():
                word_buffer.append(ch.lower())
                if i <= len(para) - 1:
                    continue

            if word_buffer:
                word = "".join(word_buffer)
                if word not in banned:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        most_common_word = word
                # reset the buffer
                word_buffer = []
        return most_common_word


if __name__ == "__main__":
    paragraph = Paragraph()
    print(paragraph.get_most_common_word(
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        ["hit"]
    ))
    print(paragraph.get_most_common_word(
        "a.",
        []
    ))
