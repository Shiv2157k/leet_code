from typing import List


class PhoneNumber:

    def get_all_letter_combinations(self, digits: str) -> List[str]:
        """
        Approach: Back Tracking
        Time Complexity: O(3^N * 4^M)
        Space Complexity: O(3^N * 4^M)
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

        def back_track(combination: str, next_digit: str):
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
    phone_number = PhoneNumber()
    print(phone_number.get_all_letter_combinations("23"))
    print(phone_number.get_all_letter_combinations("69"))