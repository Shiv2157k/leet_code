from typing import List


class PlusOne:

    def get_result(self, digits: List[int]) -> List[int]:
        """
        Approach: School Book Addition with Carry
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param digits:
        :return:
        """
        for idx in range(len(digits) - 1, -1, -1):
            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        return [1] + digits


if __name__ == "__main__":
    plus_one = PlusOne()
    print(plus_one.get_result([1, 9, 9]))
    print(plus_one.get_result([1, 2, 4]))
    print(plus_one.get_result([9, 9, 9]))
    print(plus_one.get_result([2, 9, 9, 9]))