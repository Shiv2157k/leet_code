class Parentheses:

    def is_valid(self, s: str) -> bool:
        """
        Approach: Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        stack = []
        mapper = {"}": "{", ")": "(", "]": "["}

        for char in s:

            if char in mapper:
                top = stack.pop() if stack else "$"
                if top != mapper[char]:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.is_valid("()(())"))
    print(parentheses.is_valid("((())"))
    print(parentheses.is_valid("))(())"))
