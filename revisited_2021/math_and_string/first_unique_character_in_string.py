class String:

    def first_unique_character(self, s: str) -> int:
        """
        Approach: Linear
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        from collections import Counter
        counter = Counter(s)

        for idx, char in enumerate(s):
            if counter[char] == 1:
                return idx
        return -1


if __name__ == "__main__":
    string = String()
    print(string.first_unique_character("leetcode"))
    print(string.first_unique_character("hackerrank"))
    print(string.first_unique_character("penandpaper"))
    print(string.first_unique_character(""))