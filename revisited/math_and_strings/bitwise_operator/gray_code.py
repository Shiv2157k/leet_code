from typing import List


class GrayCode:

    def generate(self, n: int) -> List[int]:
        """
        Approach: Bit Manipulation
        Formulae: res[-1] xor (Y & - Y)
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :return:
        How to get gray code from binary?
        xor of your last:
        Example:  Binary: 0111 - i/p
        0 1 1 1
        Gray Code:
        0 remains same
        xor of 0 and 1
        ie., 0 1
        xor of 1 and 1
        ie., 0 1 0-> i/p
        xor of 0 and 1
        ie., 0 1 0 1
        """
        gray = [0]
        for i in range(1, 2**n):
            gray.append(gray[-1] ^ (i & -i))
        return gray


if __name__ == "__main__":
    gray_code = GrayCode()
    print(gray_code.generate(2))