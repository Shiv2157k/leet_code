from typing import List


class Phone:

    def get_letter_combination_of_number(self, digits: str) -> List[str]:
        """
        Approach: Back tracking
        Time Complexity: O(3^M * 4^N)
        Space Complexity: O(3^M * 4^N)
        :param digits:
        :return:
        """
        phone_book = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def back_track(combination, next_digit):

            # base case
            if len(next_digit) == 0:
                output.append(combination)
            else:
                for letter in phone_book[next_digit[0]]:
                    back_track(combination + letter, next_digit[1:])

        output = []
        if digits:
            back_track("", digits)
        return output


if __name__ == "__main__":

    phone = Phone()
    print(phone.get_letter_combination_of_number("23"))