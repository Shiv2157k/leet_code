

class LastWordLength:

    def length_of_last_word(self, string: str) -> int:
        """
        Approach: Two Loop
        :param string:
        :return:
        """
        index = len(string) - 1
        while index > 0 and string[index] == ' ':
            index -= 1

        length = 0
        while index > 0 and string[index] != ' ':
            index -= 1
            length += 1
        return length

    def length_of_last_word_(self, string: str) -> int:
        """
        Approach: Single Loop
        :param string:
        :return:
        """
        index, length = len(string), 0
        while index > 0:
            index -= 1
            if string[index] != ' ':
                length += 1
            elif length > 0:
                return length
        return length

    def length_of_last_word__(self, string: str) -> int:
        return 0 if not string or string.isspace() else len(string.split()[-1])


if __name__ == "__main__":
    word_length = LastWordLength()
    print(word_length.length_of_last_word('Hello Shiva Kumar Nadicherra '))
    print(word_length.length_of_last_word_('Hello Shiva Kumar Nadicherra '))
    print(word_length.length_of_last_word__('Hello Shiva Kumar Nadicherra '))