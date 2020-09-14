from typing import List


class WordBreak:

    def is_sequence(self, string: str, word_list: List[str]) -> bool:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n^3)
        Space Complexity: O(n)
        :param string:
        :param word_list:
        :return:
        """
        tracker = [False] * (len(string) + 1)
        tracker[0] = True

        for end in range(1, len(string) + 1):
            for start in range(end):
                if tracker[start] and string[start: end] in word_list:
                    tracker[end] = True
                    break
        return tracker[-1]


if __name__ == "__main__":
    word_break = WordBreak()
    print(word_break.is_sequence("leetcode", ["leet", "code"]))
    print(word_break.is_sequence("catsandog", ["cats", "dog", "sand", "and", "cat"]))

