from typing import List


class WordBreak:

    def is_a_segment(self, s: str, word_list: List[str]) -> bool:
        """
        Approach: Dynamic Programming.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :param s:
        :param word_list:
        :return:
        """
        tracker = [False] * (len(s) + 1)
        tracker[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if tracker[j] and s[j:i] in word_list:
                    tracker[i] = True
                    break
        return tracker[-1]


if __name__ == "__main__":
    word_break = WordBreak()
    print(word_break.is_a_segment("leetcode", ["leet", "code"]))
    print(word_break.is_a_segment("catsandogs", ["cat", "san", "dogs"]))
    print(word_break.is_a_segment("catsandog", ["cats", "dog", "sand", "and", "cat"]))