

class String:

    def compress(self, characters: str) -> int:
        """
        Approach: Read and Write Heads
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param characters:
        :return:
        0 1 2 3 4 5 6
        a a a b b c c
        a3b2c2
        """
        write = anchor = 0
        for read, ch in enumerate(characters):
            if read + 1 == len(characters) or characters[read + 1] != ch:
                characters[write] = characters[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        characters[write] = digit
                        write += 1
                anchor = read + 1
        return write


if __name__ == "__main__":
    string = String()
    print(string.compress(["a", "a", "b", "b", "c", "c"]))
    print(string.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
    print(string.compress(["a", "a", "a", "b", "c", "c", "c"]))
    print(string.compress(["a"]))

