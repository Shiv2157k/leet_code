
class Parentheses:

    def min_remove(self, s: str) -> str:
        """
        Approach:
        Time Complexity:
        Space Complexity:
        :param s:
        :return:
        """
        stack = []
        ignore_indices = set()
        balance = 0

        for idx, char in enumerate(s):

            if char not in "()":
                balance += 1
            elif char == "(":
                stack.append(idx)
            elif not stack:
                ignore_indices.add(idx)
            else:
                stack.pop()

        ignore_indices = ignore_indices.union(set(stack))
        string_builder = []

        for idx, char in enumerate(s):
            if idx not in ignore_indices:
                string_builder.append(char)
        return "".join(string_builder)

    def min_remove_(self, s: str) -> str:

        def del_invalid_parentheses(s: str, open_bracket: str, close_bracket: str):
            sb = []
            balance = 0
            for char in s:
                if char == open_bracket:
                    balance += 1
                elif char == close_bracket:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(char)
            return "".join(sb)

        s = del_invalid_parentheses(s, "(", ")")
        s = del_invalid_parentheses(s[::-1], ")", "(")
        return s[::-1]

    def min_remove__(self, s: str) -> str:
        """
        Approach:
        Time Complexity:
        Space Complexity:
        :param s:
        :return:
        """

        balance = open_seen = 0
        first_pass_chars = []

        for char in s:
            if char == "(":
                balance += 1
                open_seen += 1
            elif char == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(char)

        open_to_keep = open_seen - balance
        result = []

        for char in first_pass_chars:
            if char == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(char)
        return "".join(result)


if __name__ == "__main__":
    parentheses = Parentheses()
    # output: l(e)et(co)de
    print(parentheses.min_remove("l(e)et((co)d(e"))
    print(parentheses.min_remove_("l(e)et((co)d(e"))
    print(parentheses.min_remove__("l(e)et((co)d(e"))

    print(parentheses.min_remove("a)b(c)d"))
    print(parentheses.min_remove_("a)b(c)d"))
    print(parentheses.min_remove__("a)b(c)d"))

    print(parentheses.min_remove("lee(t(c)o)de)"))
    print(parentheses.min_remove_("lee(t(c)o)de)"))
    print(parentheses.min_remove__("lee(t(c)o)de)"))