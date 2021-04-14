from typing import List
from collections import defaultdict


class Anagrams:

    def group(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Categorize By Count
        Time Complexity: O(NK)
        Space Complexity: O(NK)
        - N length of string list.
        - maximum length of string.
        :param strs:
        :return:
        """
        result = defaultdict(list)
        # result = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            # when default dict is used.
            result[tuple(count)].append(string)
            """
            if tuple(count) in result:
                result[tuple(count)].append(string)
            else:
                result[tuple(count)] = [string]
            """

        return result.values()


if __name__ == "__main__":
    anagrams = Anagrams()
    print(anagrams.group(
        ["eat", "tea", "tan", "ate", "nat", "bat"]
    ))