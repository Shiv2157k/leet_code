class String:

    def get_longest_substring_length(self, s: str) -> int:
        """
        Approach: Sliding Window
        Time Complexity: O(N)
        Space Complexity (HashMap): O(min(m,n))
        Space Complexity (Table): O(m)
        :param s:
        :return:
        """
        hash_map = {}
        index = max_len = 0
        for idx, char in enumerate(s):
            if char in hash_map:
                max_len = max(max_len, idx - index)
                index = max(index, hash_map[char] + 1)

            hash_map[char] = idx
        return max(max_len, len(s) - index)


if __name__ == "__main__":
    string = String()
    print(string.get_longest_substring_length("a"))
    print(string.get_longest_substring_length(" "))
    print(string.get_longest_substring_length("au"))
    print(string.get_longest_substring_length("aua"))
    print(string.get_longest_substring_length("abcabcababa"))