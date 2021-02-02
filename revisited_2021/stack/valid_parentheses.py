

class Parentheses:

    def is_valid(self, string: str) -> bool:
        """
        Approach: Using Stacks
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """
        stack = []
        mapper = {"}": "{", "]": "[", ")": "("}
        for char in string:
            if char in mapper:
                top_element = stack.pop() if stack else "$"
                if mapper[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.is_valid("(()[]{}){}"))
    print(parentheses.is_valid("{{{{{{{{}[]]"))