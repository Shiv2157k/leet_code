

class ValidParentheses:

    def is_valid(self, parentheses: str) -> bool:
        stack = []
        mapping = {"}": "{", ")": "(", "]": "["}
        for char in parentheses:
            # if we come across closed brackets we go into below condition.
            if char in mapping:
                top = stack.pop() if stack else "$"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    res = ValidParentheses()
    print(res.is_valid("(){(([]))}[]{}"))
    print(res.is_valid("{{}}[[]"))