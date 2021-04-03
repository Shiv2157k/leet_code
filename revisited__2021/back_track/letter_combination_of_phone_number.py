from typing import List


class PhoneBook:

    def letter_combination_of_number(self, digits: str):
        """
        Approach: Back tracking
        Time Complexity:
        Space Complexity:
        :param digits:
        :return:
        """

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def back_track(combination: str, next_digit: str):
            """
            Back tracking inner function.
            :param combination:
            :param next_digit:
            :return:
            """
            if not next_digit:
                output.append(combination)
            else:
                for letter in phone[next_digit[0]]:
                    back_track(combination + letter, next_digit[1:])

        output = []
        if digits:
            back_track("", digits)
        return output


if __name__ == "__main__":
    phonebook = PhoneBook()
    print(phonebook.letter_combination_of_number(
        "23"
    ))