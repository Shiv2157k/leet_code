class Parentheses:

    def is_valid(self, string: str) -> bool:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """
        stack = []
        mapper = {"]": "[", "}": "{", ")": "("}

        for char in string:
            if char in mapper:
                top = stack.pop() if stack else "$"
                if mapper[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.is_valid("{{[][[]]}}"))
    print(parentheses.is_valid("()[]{}"))
    print(parentheses.is_valid("{{)})"))


