

class String:

    def get_longest_palindrome_substring(self, s: str) -> str:
        """
        Approach: Manacher's Algorithm
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        strs = "#".join("&{}$".format(s))
        length = len(strs)
        tracker = [0] * length
        center = right_bound = 0
        for mid in range(1, length - 1):
            # find the mirror
            mirror = 2 * center - mid

            # if mid is with-in boundary
            if mid < right_bound:
                tracker[mid] = min(right_bound - mid, tracker[mirror])

            # expand the center
            while mid + (1 + tracker[mid]) < length and mid - (1 - tracker[mid]) >= 0 \
                    and strs[mid + 1 + tracker[mid]] == strs[mid - 1 - tracker[mid]]:
                tracker[mid] += 1

            # if the current mid exceeds the right boundary
            if mid + tracker[mid] > right_bound:
                center = mid
                right_bound = mid + tracker[mid]

        max_len, center_idx = max((val, i) for i, val in enumerate(tracker))
        return s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]

    def expand_around_center(self, s: str, left: int, right: int):
        """
        Expands around the center and returns the center index.
        :param s:
        :param left:
        :param right:
        :return:
        """
        # keep expanding around the center if it satisfies
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def get_longest_palindromic_substring(self, s: str) -> str:
        """
        Approach: Expand around the center
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        # base case
        if not s and len(s) < 1:
            return ""

        start = end = 0

        # loop through the string
        for idx in range(len(s)):
            odd_len = self.expand_around_center(s, idx, idx)
            even_len = self.expand_around_center(s, idx, idx + 1)
            len_ = max(odd_len, even_len)

            # we have found a max length
            # calculate the start and end points
            if len_ > end - start:
                start = idx - ((len_ - 1) // 2)
                end = idx + len_ // 2
        return s[start: end + 1]


if __name__ == "__main__":
    string = String()
    print(string.get_longest_palindromic_substring("aabbaa"))
    print(string.get_longest_palindrome_substring("aaabbaa"))
    print(string.get_longest_palindromic_substring("racecar"))
    print(string.get_longest_palindrome_substring("racecar"))
    print(string.get_longest_palindromic_substring("sdhadad"))
    print(string.get_longest_palindrome_substring("sdhadad"))
    print(string.get_longest_palindromic_substring(""))
    print(string.get_longest_palindrome_substring(""))
    print(string.get_longest_palindromic_substring("a"))
    print(string.get_longest_palindrome_substring("a"))
    print(string.get_longest_palindromic_substring("aa"))
    print(string.get_longest_palindrome_substring("aa"))