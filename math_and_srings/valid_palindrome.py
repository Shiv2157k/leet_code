
class Palindrome:

    def is_valid(self, sentence: str) -> bool:
        """
        Approach: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param sentence:
        :return:
        """
        left, right = 0, len(sentence) - 1

        while left < right:

            while left < right and not sentence[left].isalnum():
                left += 1
            while left < right and not sentence[right].isalnum():
                right -= 1

            if left < right and sentence[left].lower() != sentence[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    palindrome = Palindrome()
    print(palindrome.is_valid("A man, a plan, a canal: Panama "))
    print(palindrome.is_valid("2A man, a plan, a canal: Panama 1"))
    print(palindrome.is_valid("A man, a plan, a canal: Panama 1"))
    print(palindrome.is_valid("1A man, a plan, a canal: Panama 1"))
