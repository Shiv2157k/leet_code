

class String:

    def minimum_remove_to_make_valid_parentheses(self, s: str) -> str:
        """
        Approach: Shortened two pass string builder
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        balance = open_seen = 0
        first_pass_characters = []
        for ch in s:
            if ch == "(":
                open_seen += 1
                balance += 1
            if ch == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass_characters.append(ch)

        open_to_keep = open_seen - balance
        result = []
        for ch in first_pass_characters:
            if ch == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            result.append(ch)
        return "".join(result)


if __name__ == "__main__":
    string = String()
    print(string.minimum_remove_to_make_valid_parentheses("l(e)et((co)d(e"))
    print(string.minimum_remove_to_make_valid_parentheses("lee(t(c)o)de)"))