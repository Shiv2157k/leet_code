class String:

    def compress(self, chars: str) -> int:
        """
        Approach: Read and write heads.
        Time Complexity:
        Space Complexity:
        :param chars:
        :return:
        """

        write = anchor = 0

        for read, char in enumerate(chars):
            # we hit any of the below edge case
            if read + 1 == len(chars) or chars[read + 1] != char:
                chars[write] = chars[anchor]
                write += 1
                # current index is greater than anchor
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = chars[anchor]
                        # increment the writer
                        write += 1
                # update the anchor
                anchor = read + 1
        return write


if __name__ == "__main__":
    string = String()
    print(string.compress(["a", "a", "b", "b", "b"]))
    print(string.compress(["a", "b"]))
    print(string.compress(["a"]))
    print(string.compress(["s", "s"]))
    print(string.compress(["a", "a", "a", "a", "a", "a"]))
    print(string.compress(["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]))