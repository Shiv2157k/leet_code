class Words:

    def get_last_word_length_(self, string: str) -> int:
        """
        Approach: String Index Manipulation
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """
        length, idx = 0, len(string) - 1
        while idx >= 0 and string[idx] == " ":
            idx -= 1

        while idx >= 0 and string[idx] != " ":
            idx -= 1
            length += 1
        return length

    def get_last_word_length(self, string: str) -> int:
        """
        Approach: One loop Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """
        length, idx = 0, len(string)

        while idx > 0:
            idx -= 1
            if string[idx] != " ":
                length += 1
            elif length > 0:
                return length
        return length

    def get_last_word_length__(self, string: str) -> int:
        """
        Approach: Built-in string methods
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """
        return 0 if not string or string.isspace() else len(string.split()[-1])


if __name__ == "__main__":
    words = Words()
    print(words.get_last_word_length("Hello World"))
    print(words.get_last_word_length_("Hello World"))
    print(words.get_last_word_length__("Hello World"))
    print(words.get_last_word_length("a "))
    print(words.get_last_word_length_("a "))
    print(words.get_last_word_length__("a "))
    print(words.get_last_word_length(""))
    print(words.get_last_word_length_(""))
    print(words.get_last_word_length__(""))

