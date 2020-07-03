from typing import List


class GrayCode:

    def get_sequence(self, n: int) -> List[int]:

        sequence = [0]
        for i in range(1, 2**n):
            sequence.append(sequence[-1] ^ (i & -i))
        return sequence


if __name__ == "__main__":
    gray_code = GrayCode()
    print(gray_code.get_sequence(2))
    print(gray_code.get_sequence(3))
    print(gray_code.get_sequence(4))
