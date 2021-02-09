class String:

    def longest_palindrome_(self, s: str) -> str:
        """
        Approach: Manacher's Algorithm
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        ss = "#".join("${}^".format(s))
        center = right_bound = 0
        length = len(ss)
        tracker = [0] * length
        for idx in range(1, length - 1):
            # calculate the current mirror
            mirror = 2 * center - idx
            # if current index is within the right boundary
            # apply the two conditions
            if idx < right_bound:
                tracker[idx] = min(tracker[mirror], right_bound - idx)

            # expand the current center
            while idx - (1 - tracker[idx]) >= 0 and idx + (1 + tracker[idx]) < length and ss[idx - 1 - tracker[idx]] == ss[idx + 1 + tracker[idx]]:
                tracker[idx] += 1

            # re-align the center and right bound
            if idx + tracker[idx] > right_bound:
                center = idx
                right_bound = idx + tracker[idx]

        max_len, center_idx = max((val, idx) for idx, val in enumerate(tracker))
        return s[(center_idx - max_len) // 2: (center_idx + max_len) // 2]

    def expand_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longest_palindrome(self, s: str) -> str:
        """
        Approach: Expand Around Center
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        if not s or len(s) < 1:
            return ""
        start = end = 0
        for idx in range(len(s)):
            odd_len = self.expand_center(s, idx, idx)
            even_len = self.expand_center(s, idx, idx + 1)

            length = max(even_len, odd_len)
            if length > end - start:
                start = idx - ((length - 1) // 2)
                end = idx + length // 2
        return s[start: end + 1]


if __name__ == "__main__":
    string = String()
    print(string.longest_palindrome("babad"))
    print(string.longest_palindrome("baaabcbb"))
    print(string.longest_palindrome_("babad"))
    print(string.longest_palindrome_("baaabcbb"))