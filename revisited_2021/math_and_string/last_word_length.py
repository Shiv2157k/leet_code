

class String:

    def get_last_word_length(self, s: str) -> int:
        """
        Approach: One Loop Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        length, idx = 0, len(s)
        while idx > 0:
            idx -= 1
            if s[idx] != " ":
                length += 1
            elif length > 0:
                return length
        return length

    def _get_last_word_length(self, s: str) -> int:
        """
        Approach: String Index Manipulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        idx = len(s) - 1
        # trim trailing spaces
        while idx >= 0 and s[idx] == " ":
            idx -= 1
        # find last word length
        length = 0
        while idx >= 0 and s[idx] != " ":
            idx -= 1
            length += 1
        return length

    def get_last_word_length_built_in(self, s: str) -> int:
        """
        Approach: Built-in method
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        return 0 if not s or s.isspace() else len(s.split(" ")[-1])


if __name__ == "__main__":
    string = String()
    print(string.get_last_word_length("Hello World"))
    print(string.get_last_word_length("H"))
    print(string._get_last_word_length("Hello World"))
    print(string._get_last_word_length("H"))
    print(string.get_last_word_length_built_in("Hello World"))
    print(string.get_last_word_length_built_in("H"))
