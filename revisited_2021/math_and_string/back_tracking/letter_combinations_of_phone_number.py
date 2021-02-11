from typing import List


class PhoneBook:

    mapper = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letter_combinations(self, digits: str) -> List[str]:
        """
        Approach: Back Tracking
        Time Complexity: O(3^N * 4^M)
        Space Complexity: O(3^N * 4^M)
        :param digits:
        :return:
        """

        def back_track(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in self.mapper[next_digits[0]]:
                    back_track(combination + letter, next_digits[1:])

        output = []
        if digits:
            back_track("", digits)
        return output


if __name__ == "__main__":
    phone_book = PhoneBook()
    print(phone_book.letter_combinations("23"))
    print(phone_book.letter_combinations("234"))
    print(phone_book.letter_combinations("9"))