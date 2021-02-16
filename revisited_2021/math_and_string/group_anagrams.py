from typing import List
from collections import defaultdict


class Anagrams:

    def group(self, strs: List[str]) -> List[str]:
        """
        Approach: Categorize by count
        Time Complexity: O(NK)
        Space Complexity: O(NK)
        :param strs:
        :return:
        """
        ans = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(string)
        return ans.values()

    def group_(self, strs: List[str]) -> List[str]:
        """
        Approach: Categorize by sorted string
        Time Complexity: O(N log K)
        Space Complexity: O(NK)
        :param strs:
        :return:
        """
        ans = defaultdict(list)
        for string in strs:
            ans[tuple(sorted(string))].append(string)
        return ans.values()


if __name__ == "__main__":
    anagrams = Anagrams()
    print(anagrams.group_(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(anagrams.group(["eat", "tea", "tan", "ate", "nat", "bat"]))
