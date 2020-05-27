

class AddBinary:

    def add_binary_(self, a: str, b: str) -> str:
        """
        Approach: Using python built-in functions.
        :param a:
        :param b:
        :return:
        """
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def add_binary__(self, a: str, b: str) -> str:
        """
        Approach: Bit by Bit Computation.
        :param a:
        :param b:
        :return:
        """
        max_len = max(len(a), len(b))
        # filling the leading zeroes with max len of a and b
        a, b = a.zfill(max_len), b.zfill(max_len)
        carry, result = 0, []

        # loop through right side of a and b
        for i in range(max_len - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            # if one of a and b has value 1
            if carry % 2 == 1:
                result.append('1')
            else:
                result.append('0')

            # divide the carry by 2 to re-initialize with 1
            carry //= 2

        if carry == 1:
            result.append('1')

        result.reverse()
        return ''.join(result)

    def add_binary(self, a: str, b: str) -> str:
        """
        Approach: Bit Manipulation.
        :param a:
        :param b:
        :return:
        """
        # Convert binary strings to integer number
        x, y = int(a, 2), int(b, 2)

        # loop until carry is 0
        while y:
            # result is xor of x and y.
            result = x ^ y
            # carry left shift with and of x and y.
            carry = (x & y) << 1
            x, y = result, carry
        # converting the integer back to binary.
        return bin(x)[2:]


if __name__ == "__main__":
    answer = AddBinary()
    print(answer.add_binary__('101', '11'))
    print(answer.add_binary_('101', '11'))
    print(answer.add_binary('101', '11'))
    print(answer.add_binary__('101', '10'))
    print(answer.add_binary('101', '10'))