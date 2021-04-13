class String:

    def index_of_first_unique_character(self, chars: str) -> int:
        """
        Approach: Hash Map
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param chars:
        :return:
        """

        hash_map = {}
        for i in range(len(chars)):
            hash_map[chars[i]] = hash_map.get(chars[i], 0) + 1

        for i in range(len(chars)):
            if hash_map[chars[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    string = String()
    print(string.index_of_first_unique_character("leetcode"))
    print(string.index_of_first_unique_character("aaab"))
    print(string.index_of_first_unique_character("loveleetcode"))