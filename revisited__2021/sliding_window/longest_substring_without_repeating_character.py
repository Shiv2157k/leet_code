

class String:

    def longest_substring_wo_rep_char_(self, s: str) -> int:
        """
        Approach: Sliding Window Optimized
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        if not s:
            return 0

        n = len(s)
        left = max_len = 0
        tracker = dict()

        for right in range(n):
            if s[right] in tracker:
                left = max(tracker[s[right]], left)
            max_len = max(max_len, right - left + 1)
            tracker[s[right]] = right + 1
        return max_len

    def longest_substring_wo_rep_char(self, s: str) -> int:
        """
        Approach: Sliding Window
        Time Complexity: O(2N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        if not s:
            return 0
        left = right = max_len = 0
        n = len(s)
        visited = set()

        while right < n:
            char = s[right]
            while char in visited:
                visited.remove(s[left])
                left += 1
            visited.add(char)
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


if __name__ == "__main__":
    string = String()
    print(string.longest_substring_wo_rep_char(
        "pwwkew"
    ))
    print(string.longest_substring_wo_rep_char_(
        "pwwkew"
    ))
    print(string.longest_substring_wo_rep_char(
        "abcdeafbdgcbb"
    ))
    print(string.longest_substring_wo_rep_char_(
        "abcdeafbdgcbb"
    ))
