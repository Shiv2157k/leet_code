

class Permutations:

    def get_sequence(self, n: int, k: int) -> str:
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param n:
        :param k:
        :return:
        """

        factorials, digits = [1], ["1"]

        # generate factorials and digits
        for i in range(1, n):
            factorials.append(factorials[i - 1] * i)
            digits.append(str(i + 1))

        # decrement k by 1 to suit the o index
        k -= 1
        output = []
        # start extracting permutation sequence from factorial
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k = k - idx * factorials[i]

            output.append(digits[idx])
            del digits[idx]
        return "".join(output)


if __name__ == "__main__":
    permutation = Permutations()
    print(permutation.get_sequence(3, 3))
    print(permutation.get_sequence(4, 14))