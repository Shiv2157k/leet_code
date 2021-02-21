class ExcelSheet:

    def title_to_number(self, s: str) -> int:
        """
        Approach: Left to Right
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        number = 0
        for ch in s:
            number *= 26
            number += (ord(ch) - ord("A") + 1)
        return number


if __name__ == "__main__":
    excel_sheet = ExcelSheet()
    print(excel_sheet.title_to_number("AB"))
    print(excel_sheet.title_to_number("ABC"))