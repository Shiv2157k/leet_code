from typing import List


class Dictionary:

    def longest_word(self, s: str, d: List[str]) -> str:
        """
        Approach: Without Sorting
        Time Complexity: O(N * X)
        Space Complexity: O(X)
        :param s:
        :param d:
        :return:
        """
        result = ""

        for word in d:
            # skip conditions
            result_len, word_len = len(result), len(word)
            if word_len < result_len or (word_len == result_len and result < word):
                continue

            # logic to find longest word
            pos = -1
            for char in word:
                # keep on increasing the s search index to right
                # once visited.
                pos = s.find(char, pos + 1)
                # if a character is not encountered
                # break the loop
                if pos == -1:
                    break
            # if all characters are encountered
            # make it as result
            if pos != -1:
                result = word
        return result


if __name__ == "__main__":
    dictionary = Dictionary()
    print(dictionary.longest_word("abpcplea", ["ale", "apple", "monkey", "plea"]))
    print(dictionary.longest_word("abpcplea", ["a", "b", "c"]))