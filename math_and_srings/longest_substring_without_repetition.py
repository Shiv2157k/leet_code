
class Substring:

    def get_longest_without_repetition(self, string: str) -> int:

        dictionary = {}
        length = index = 0

        for curr_index, char in enumerate(string):
            if char in dictionary:
                length = max(length, curr_index - index)
                index = max(index, dictionary[char] + 1)
            dictionary[char] = curr_index
        return max(length, len(string) - index)

    def get_longest_without_repetition_(self, string: str) -> int:

        dictionary = {}
        max_len = index = 0

        for curr_index, char in enumerate(string):
            if char in dictionary:
                start_idx = dictionary[char] + 1
                if start_idx > index:
                    index = start_idx
            curr_len = curr_index - index + 1
            if curr_len > max_len:
                max_len = curr_len
            dictionary[char] = curr_index
        return max_len


if __name__ == "__main__":

    sub_string = Substring()
    print(sub_string.get_longest_without_repetition("abcabcdabc"))
    print(sub_string.get_longest_without_repetition_("abcabcdabc"))
