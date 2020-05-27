from typing import List

class PlusOne:

    def get_result(self, digits: List[int]) -> List[int]:
        """
        Approach: School Book Addition
        :param digits:
        :return:
        """
        _len = len(digits)
        for i in range(_len):
            # index from the right
            index = _len - 1 - i
            # if the last index value is 9 make it to 0
            if digits[index] == 9:
                digits[index] = 0
            # add one to the remaining all.
            else:
                digits[index] += 1
                return digits
        # when all the values in the list is 9 add one to the front
        return [1] + digits


if __name__ == "__main__":
    plus_one = PlusOne()
    print(plus_one.get_result([1, 2, 3, 4]))
    print(plus_one.get_result([1, 2, 9, 9]))
    print(plus_one.get_result([1, 2, 8, 9]))