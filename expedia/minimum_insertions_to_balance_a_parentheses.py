

class Parentheses:

    def min_insertions(self, s: str) -> int:
        """
        Approach: Iteration
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        left_braces = count = index = 0

        # to make comparisions easier append an special char at end
        s += "$"

        while index < (len(s) - 1):

            if s[index] == "(":
                left_braces += 1
                index += 1
            elif s[index] == ")" and s[index + 1] == ")":
                if left_braces:
                    left_braces -= 1
                else: # left brace required
                    count += 1
                # move two steps forward
                index += 2
            elif s[index] == ")" and s[index + 1] != ")":
                if left_braces: # a single close brace required
                    left_braces -= 1
                    count += 1
                else: # one open and one close brace required
                    count += 2
                index += 1
        return count + (left_braces * 2)


if __name__ == "__main__":
    parentheses = Parentheses()
    print(parentheses.min_insertions("(()))"))
    print(parentheses.min_insertions("())"))
    print(parentheses.min_insertions("))())("))
    print(parentheses.min_insertions("(((((("))
    print(parentheses.min_insertions("))))))"))