from typing import List


class ReversePolishNotation:

    def __init__(self):
        """
        Constructor method which takes care of
        Reverse Polish Notation operations.
        """
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }

    def evaluate_RPN(self, tokens: List[str]) -> int:
        """
        Approach: Reducing the List Space with operations
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param tokens:
        :return:
        """
        stack = []
        for token in tokens:
            if token not in self.operations:
                stack.append(int(token))
                continue
            y = stack.pop()
            x = stack.pop()
            operator = self.operations[token]
            stack.append(operator(x, y))
        return stack[0]

    def evaluate_RPN_(self, tokens: List[str]) -> int:
        """
        Approach: Reducing the List Space
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param tokens:
        :return:
        """
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue
            y = stack.pop()
            x = stack.pop()
            operator = token

            if operator == "+":
                stack.append(x + y)
            elif operator == "-":
                stack.append(x - y)
            elif operator == "*":
                stack.append(x * y)
            elif operator == "/":
                stack.append(int(x / y))
        return stack[0]


if __name__ == "__main__":
    rpn = ReversePolishNotation()
    print(rpn.evaluate_RPN(["2", "1", "+", "3", "*"]))
    print(rpn.evaluate_RPN_(["2", "1", "+", "3", "*"]))
