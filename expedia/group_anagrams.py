from typing import List


class Anagrams:

    def group(self, strs: List[str]) -> List[List[str]]:
        """
        Approach: Categorize by count
        Time Complexity: O(NK)
        Space Complexity: O(NK)
        :param strs:
        :return:
        """

        mapper = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            if tuple(count) not in mapper:
                mapper[tuple(count)] = [string]
            else:
                mapper[tuple(count)].append(string)
        return mapper.values()


if __name__ == "__main__":

    anagram = Anagrams()
    print(anagram.group(["eat", "tea", "tan", "ate", "nat", "bat"]))