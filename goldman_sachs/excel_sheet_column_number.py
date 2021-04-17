

class Excel:

    def title_to_number(self, string: str) -> int:
        """
        Approach: Left to Right
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        number = 0
        for char in string:
            number *= 26
            number += (ord(char) - ord("A") + 1)
        return number


if __name__ == "__main__":
    excel = Excel()
    print(excel.title_to_number("A"))
    print(excel.title_to_number("AB"))
    print(excel.title_to_number("ZY"))
    print(excel.title_to_number("FXSHRXW"))