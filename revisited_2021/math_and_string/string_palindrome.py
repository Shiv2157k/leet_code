

class String:

    def pal_rec(self, s: str, l: int, r: int):
        if l == r:
            return True
        if s[l] != s[r]:
            return False
        if l < r + 1:
            return self.pal_rec(s, s + 1, r - 1)
        return True

    def is_pal(self, s: str) -> bool:
        """
        Approach: Recursion
        :param s:
        :return:
        """
        if not s:
            return True
        return self.pal_rec(s, 0, len(s) - 1)

    def is_palindrome(self, s: str) -> bool:
        """
        Approach: Two Pointers
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        left, right = 0, len(s) - 1
        s = s.upper()
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    string = String()
    print(string.is_palindrome("A man, a plan, a canal: Panama"))