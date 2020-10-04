from typing import List, Union


class BasicCalculator:

    def evaluate(self, stack: List[Union[int, str]]) -> int:
        """
        Evaluates the stack and calculates the results respectively.
        :param stack:
        :return:
        """
        result = stack.pop() if stack else 0
        # loop through the stack until you reach stack[-1] to ")"
        while stack and stack[-1] != ")":
            sign = stack.pop()
            if sign == "+":
                result += stack.pop()
            else:
                result -= stack.pop()
        return result

    def get_result(self, string: str) -> int:
        """
        Approach: Using Stack
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param string:
        :return:
        """
        stack = []
        # operand - numbers to convert into their respective digit
        # for calculating the digits
        # number_count - to keep track of numbers in a string
        operand = number_count = 0

        # loop from reverse
        # to follow the bracket priority
        # (7 - 8 + 9) -> ) 9 + 8 - 7 (
        for idx in range(len(string) - 1, -1, -1):
            char = string[idx]
            # if char is a digit
            if char.isdigit():
                # add it to the operand
                # with number count power of 10
                operand += (10**number_count * int(char))
                # increment the number count
                number_count += 1
            elif char != " ":  # if this is not a digit
                # if the number count exists
                if number_count:
                    # add the operand to the stack
                    stack.append(operand)
                    # reset the number count and operand to 0
                    number_count = operand = 0
                if char == "(":  # if you have reached the closing bracket
                    # it is time to evaluate the expression so far
                    result = self.evaluate(stack)
                    # pop the last added
                    stack.pop()
                    # add the new result
                    stack.append(result)
                else:  # add all the non digits
                    stack.append(char)

        # to evaluate the remaining numbers in stack if operand exists
        # based on the number count
        if number_count:
            stack.append(operand)

        return self.evaluate(stack)


if __name__ == "__main__":
    calculator = BasicCalculator()
    print(calculator.get_result("(7 - 8 + 9)"))
    print(calculator.get_result("1 + 1"))
    print(calculator.get_result("(3 + 4 - (8 + (10 + 5) + 12) - 18)"))
    print(calculator.get_result("(3 + 4 - (8 + (10 + 5) + 12) + 38)"))