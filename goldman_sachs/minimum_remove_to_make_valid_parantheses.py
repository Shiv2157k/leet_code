

class Parentheses:

    def minimum_remove_to_make_valid(self, s: str) -> str:
        """
        Approach: Two Pass + String Builder
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        def del_invalid_parentheses(string: str, open_parentheses: str, close_parentheses: str) -> str:

            string_builder = []
            balance = 0
            for char in string:

                if char == open_parentheses:
                    balance += 1
                elif char == close_parentheses:
                    if balance == 0:
                        continue
                    balance -= 1
                string_builder.append(char)
            return "".join(string_builder)

        s = del_invalid_parentheses(s, "(", ")")
        s = del_invalid_parentheses(s[::-1], ")", "(")
        return s[::-1]

    def minimum_remove_to_make_valid_without_reverse(self, s: str) -> str:
        """
        Approach: Two Pass without reversing
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        filter_one = []
        open_seen = balance = 0

        for char in s:
            if char == "(":
                balance += 1
                open_seen += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1
            filter_one.append(char)

        final_filter = []
        open_needed = open_seen - balance
        for char in filter_one:
            if char == "(":
                open_needed -= 1
                if open_needed < 0:
                    continue
            final_filter.append(char)
        return "".join(final_filter)


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.minimum_remove_to_make_valid("lee(t(c)o)de)"))
    print(parentheses.minimum_remove_to_make_valid("a)b(c)d"))
    print(parentheses.minimum_remove_to_make_valid("))(("))
    print("+++++++++++++++++++")
    print(parentheses.minimum_remove_to_make_valid_without_reverse("lee(t(c)o)de)"))
    print(parentheses.minimum_remove_to_make_valid_without_reverse("a)b(c)d"))
    print(parentheses.minimum_remove_to_make_valid_without_reverse("))(("))