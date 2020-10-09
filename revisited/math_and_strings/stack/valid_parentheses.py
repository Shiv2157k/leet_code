class Parentheses:

    def is_valid(self, string: str) -> bool:
        """
        Approach: Using Stack
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        mapper = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        stack = []
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
    print(parentheses.is_valid("()[]{}"))
    print(parentheses.is_valid("()]{}"))
    print(parentheses.is_valid("{{}}[][()]"))
