from typing import List
from collections import defaultdict as dictionary


class Anagram:

    def group(self, strings: List[str]) -> List[List[str]]:
        """
        Approach: Categorized by sorted string.
        Time Complexity: O(NK log K)
        Space Complexity: O(NK)
        :param strings:
        :return:
        """
        anagrams = dictionary(list)
        for string in strings:
            anagrams[tuple(sorted(string))].append(string)
        return anagrams.values()

    def group_(self, strings: List[str]) -> List[List[str]]:
        """
        Approach: Categorized by count.
        Time Complexity: O(NK)
        Space Complexity: O(NK)
        :param strings:
        :return:
        """
        anagrams = dictionary(list)
        for string in strings:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(string)
        return anagrams.values()


if __name__ == "__main__":

    anagram = Anagram()
    print(anagram.group(["eat", "tan", "ate", "tea", "nat", "bat", "tab", "fan"]))
    print(anagram.group_(["eat", "tan", "ate", "tea", "nat", "bat", "tab", "fan"]))
