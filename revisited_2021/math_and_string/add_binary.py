

class Binary:

    def get_sum(self, a: str, b: str) -> str:
        """
        Approach: Bit by bit Computation
        Time Complexity: O(max(n.m))
        Space Complexity: O(max(n,m))
        :param a:
        :param b:
        :return:
        """
        length = max(len(a), len(b))
        a, b = a.zfill(length), b.zfill(length)

        ans = []

        carry = 0
        for i in range(length - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1
            if carry % 2 == 1:
                ans.append("1")
            else:
                ans.append("0")
            carry //= 2
        if carry == 1:
            ans.append("1")
        ans.reverse()
        return "".join(ans)

    def get_sum_(self, a: str, b: str) -> str:
        """
        Approach: Bit Manipulation
        Time Complexity: O(M + N)
        Space Complexity: O(max(M, N))
        :param a:
        :param b:
        :return:
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            ans = x ^ y
            carry = (x & y) << 1
            x, y = ans, carry
        return bin(x)[2:]


if __name__ == "__main__":
    binary = Binary()
    print(binary.get_sum_("11", "1"))
    print(binary.get_sum("11", "1"))