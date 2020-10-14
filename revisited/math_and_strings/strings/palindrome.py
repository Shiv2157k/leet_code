class Sentence:

    def is_palindrome(self, string: str) -> bool:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """
        left, right = 0, len(string) - 1
        while left < right:

            while left < right and not string[left].isalnum():
                left += 1
            while left < right and not string[right].isalnum():
                right -= 1

            if left < right and string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sentence = Sentence()
    print(sentence.is_palindrome("A man, a plan, a canal: Panama"))
    print(sentence.is_palindrome("race a car"))