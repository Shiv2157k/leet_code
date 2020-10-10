class Binary:

    def additions(self, b1: str, b2: str) -> str:
        """
        Built in method
        :param b1:
        :param b2:
        :return:
        """
        return "{0:b}".format(int(b1, 2) + int(b2, 2))

    def addition_(self, b1: str, b2: str) -> str:
        """
        Approach: Bit Manipulation
        Time Complexity: O(N + M)
        Space Complexity: O(max(N, M))
        :param b1:
        :param b2:
        :return:
        """
        a, b = int(b1, 2), int(b2, 2)

        while b:
            a, b = (a ^ b), (a & b) << 1
        return bin(a)[2:]

    def addition(self, b1: str, b2: str) -> str:
        """
        Approach: Bit by Bit Computation
        Time Complexity: O(max(N,M))
        Space Complexity: O(max(N,M))
        :param b1:
        :param b2:
        :return:
        """
        length = max(len(b1), len(b2))
        b1, b2 = b1.zfill(length), b2.zfill(length)

        ans, carry = [], 0

        for idx in range(length - 1, -1, -1):

            if b1[idx] == "1":
                carry += 1
            if b2[idx] == "1":
                carry += 1

            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            carry //= 2
        if carry == 1:
            ans.append("1")
        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    binary = Binary()
    print(binary.addition("1111", "11"))
    print(binary.addition("11", "1"))
    print(binary.addition("1010", "1011"))
    print(binary.addition_("1111", "11"))
    print(binary.addition_("11", "1"))
    print(binary.addition_("1010", "1011"))
    print(binary.additions("1111", "11"))
    print(binary.additions("11", "1"))
    print(binary.additions("1010", "1011"))