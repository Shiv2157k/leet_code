class ZigZag:

    def convert(self, string: str, num_rows: int) -> str:
        """
        Approach: Visit by row.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param string:
        :return:
        """
        if num_rows <= 1:
            return string

        interval, string_len, output = 2 * num_rows - 2, len(string), ""

        for row in range(num_rows):
            for index in range(row, string_len, interval):
                output += string[index]
                second_index = (index - row) + (interval - row)
                if (second_index - row) % interval != 0 and second_index < string_len:
                    output += string[second_index]
        return output


if __name__ == "__main__":

    zigzag = ZigZag()
    print(zigzag.convert("PAYPALISHIRING", 3))