from typing import List, Union


class BasicCalculator:

    def evaluate_expression(self, stack: List[Union[str, int]]) -> int:
        result = stack.pop() if stack else 0
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                result += stack.pop()
            else:
                result -= stack.pop()
        return result

    def calculate(self, string: str) -> int:
        """
        Approach: Stack with string reversal
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """
        stack = []
        counter = operand = 0

        # (3 + 4 + 9) = > )9+4+3+(
        # loop in a reverse way
        for i in range(len(string) - 1, -1, -1):
            char = string[i]

            # if the character is a digit
            if char.isdigit():
                # do the operand logic
                operand += (10**counter * int(char))
                # increment the operand counter
                counter += 1
            # else if the char is not an empty string
            elif char != " ":
                if counter:
                    # append the operand into the stack
                    stack.append(operand)
                    # reset the operand and counter
                    operand = counter = 0
                # if you have reached the end
                if char == "(":
                    # evaluate the stack
                    result = self.evaluate_expression(stack)
                    # pop the stack
                    stack.pop()

                    # append the result into the stack
                    stack.append(result)
                # if it is a non digit
                else:
                    # append it to the stack
                    stack.append(char)
        # if there is an operand
        if counter:
            stack.append(operand)
        return self.evaluate_expression(stack)


if __name__ == "__main__":

    calculator = BasicCalculator()
    print(calculator.calculate("(3 + 4 + 5)"))
    print(calculator.calculate("(1 + 1 - 1)"))