

class String:

    def longest_substr_len_wo_rept_char(self, s: str) -> int:
        """
        Approach: Sliding Window Optimized
        Time Complexity: O(N)
        Space Complexity: O(min(M, N))
        :param s:
        :return:
        """

        max_len = left = 0
        hash_map = {}

        for right, char in enumerate(s):
            if char in hash_map:
                max_len = max(max_len, right - left)
                left = max(left, hash_map[char] + 1)

            hash_map[char] = right
        return max(max_len, len(s) - left)


if __name__ == "__main__":

    string = String()
    print(string.longest_substr_len_wo_rept_char("au"))
    print(string.longest_substr_len_wo_rept_char("abcdeafbdgcbb"))
    print(string.longest_substr_len_wo_rept_char("ssss"))
    print(string.longest_substr_len_wo_rept_char(" "))
    print(string.longest_substr_len_wo_rept_char(""))