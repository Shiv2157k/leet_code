from typing import List
from collections import defaultdict


class Anagrams:

    def group_(self, strings: List[str]) -> List[List[str]]:
        """
        Approach: Categorize by Count.
        N - length of strings.
        K - max length of strings.
        Time Complexity: O(NK)
        Space Complexity:
        :param strings:
        :return:
        """
        anagrams_list = defaultdict(list)
        for string in strings:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            anagrams_list[tuple(count)].append(string)
        return anagrams_list.values()

    def group(self, strings: List[str]) -> List[List[str]]:
        """
        Approach: Categorize by Sorted string.
        N - length of strings
        K - max length of strings
        Time Complexity: O(NK log K)
        Space Complexity: O(NK)
        :param strings:
        :return:
        """
        anagrams_list = defaultdict(list)

        for string in strings:
            anagrams_list[tuple(sorted(string))].append(string)
        return anagrams_list.values()


if __name__ == "__main__":
    anagrams = Anagrams()
    print(anagrams.group(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(anagrams.group_(["eat", "tea", "tan", "ate", "nat", "bat"]))