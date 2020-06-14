

class Atoi:

    def get_string_to_integer(self, string: str) -> int:
        """
        Approach: Iteration using ord() function.
        :param string:
        :return:
        """
        string = string.strip()
        if not string:
            return 0

        is_negative, integer = False, 0

        if string[0] == "-":
            is_negative = True
        elif string[0] == "+":
            is_negative = False
        elif not string[0].isnumeric():
            return 0
        else:
            integer = ord(string[0]) - ord("0")

        for i in range(1, len(string)):
            if string[i].isnumeric():
                integer = integer * 10 + (ord(string[i]) - ord("0"))
                if not is_negative and integer >= 2**31 - 1:
                    return 2**31 - 1
                if is_negative and integer >= 2**31:
                    return -2**31
            else:
                break
        return -integer if is_negative else integer


if __name__ == "__main__":

    atoi = Atoi()
    print(atoi.get_string_to_integer(" -345 "))
    print(atoi.get_string_to_integer(" -9999999999999999999"))
    print(atoi.get_string_to_integer(" 99999999999999999999"))
    print(atoi.get_string_to_integer(" 453 "))