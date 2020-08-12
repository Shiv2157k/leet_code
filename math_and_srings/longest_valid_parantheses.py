class Parentheses:

    def find_longest_valid_parentheses(self, string: str) -> int:
        """
        Approach: Using 2 pointers with no extra space
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param string:
        :return:
        """
        left = right = max_length = 0
        for i in range(len(string)):
            if string[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, right * 2)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(len(string) - 1, -1, -1):
            if string[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left * 2)
            elif left > right:
                left = right = 0
        return max_length

    def find_longest_valid_parentheses_(self, string: str) -> int:
        """
        Approach: Using Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param string:
        :return:
        """
        if not string:
            return 0
        max_length, stack = 0, [-1]
        for i in range(len(string)):
            if string[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

    def find_longest_valid_parentheses__(self, string: str) -> int:
        """
        Approach: Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(n)
        :param string:
        :return:
        """
        if not string:
            return 0

        max_length, cache = 0, [0] * len(string)

        for index in range(1, len(string)):
            if string[index] == ")":
                if string[index - 1] == "(":
                    cache[index] = 2 + (cache[index - 2] if index >= 2 else 0)
                elif index - cache[index - 1] > 0 and string[index - cache[index - 1] - 1] == "(":
                    cache[index] = cache[index - 1] + 2 + (cache[index - cache[index - 1] - 2] if index - cache[index - 1] >= 2 else 0)
            max_length = max(max_length, cache[index])
        return max_length


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.find_longest_valid_parentheses__("(()())"))
    print(parentheses.find_longest_valid_parentheses__("(()()"))
    print(parentheses.find_longest_valid_parentheses__(")("))
    print(parentheses.find_longest_valid_parentheses__(")(("))
    print(parentheses.find_longest_valid_parentheses__(")()("))
    print("===")
    print(parentheses.find_longest_valid_parentheses_("(()())"))
    print(parentheses.find_longest_valid_parentheses_("(()()"))
    print(parentheses.find_longest_valid_parentheses_(")("))
    print(parentheses.find_longest_valid_parentheses_(")(("))
    print(parentheses.find_longest_valid_parentheses_(")()("))
    print("===")
    print(parentheses.find_longest_valid_parentheses("(()())"))
    print(parentheses.find_longest_valid_parentheses("(()()"))
    print(parentheses.find_longest_valid_parentheses(")("))
    print(parentheses.find_longest_valid_parentheses(")(("))
    print(parentheses.find_longest_valid_parentheses(")()("))
