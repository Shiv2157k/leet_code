from typing import List


class ReversePolishNotation:

    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x/y)
        }

    def get_output(self, tokens: List[str]) -> int:
        """
        Approach: Evaluating the stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param tokens:
        :return:
        """
        stack = []
        for token in tokens:
            if token not in self.operations:
                stack.append(int(token))
                continue
            operator = token
            y = stack.pop()
            x = stack.pop()
            if operator == "+":
                stack.append(x + y)
            elif operator == "-":
                stack.append(x - y)
            elif operator == "*":
                stack.append(x * y)
            else:
                stack.append(int(x / y))
        return stack.pop()

    def get_output_(self, tokens: List[str]) -> int:
        """
        Approach: Evaluating the stack.
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param tokens:
        :return:
        """
        stack = []
        for token in tokens:
            if token not in self.operations:
                stack.append(int(token))
                continue
            operator = self.operations[token]
            y = stack.pop()
            x = stack.pop()
            stack.append(operator(x, y))
        return stack.pop()

    def get_output__(self, tokens: List[str]) -> int:
        """
        Approach: Reducing the list in place.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param tokens:
        :return:
        """
        position = 0
        while len(tokens) > 1:
            while tokens[position] not in "+-/*":
                position += 1

            operator = tokens[position]
            x = int(tokens[position - 2])
            y = int(tokens[position - 1])

            if operator == "+":
                tokens[position] = x + y
            elif operator == "-":
                tokens[position] = x - y
            elif operator == "*":
                tokens[position] = x * y
            else:
                tokens[position] = int(x / y)

            tokens.pop(position - 2)
            tokens.pop(position - 2)
            position -= 1
        return tokens[0]

    def get_output___(self, tokens: List[str]) -> int:
        """
        Approach: Reducing the list in place.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param tokens:
        :return:
        """

        position = 0
        while len(tokens) > 1:
            while tokens[position] not in self.operations:
                position += 1

            operation = self.operations[tokens[position]]
            x = int(tokens[position - 2])
            y = int(tokens[position - 1])
            tokens[position] = operation(x, y)
            tokens.pop(position - 2)
            tokens.pop(position - 2)
            position -= 1
        return tokens[0]


if __name__ == "__main__":
    output = ReversePolishNotation()
    print(output.get_output___(["2", "1", "+", "3", "*"]))
    print(output.get_output__(["2", "1", "+", "3", "*"]))
    print(output.get_output_(["2", "1", "+", "3", "*"]))
    print(output.get_output(["2", "1", "+", "3", "*"]))