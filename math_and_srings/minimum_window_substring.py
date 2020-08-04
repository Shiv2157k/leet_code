from collections import Counter


class Window:

    def get_minimum_window_substring(self, string: str, substring: str) -> str:
        """
        Approach: Optimized Sliding Window
        Time Complexity: O(|S| + |T|)
        Space Complexity: O(|S| + |T|)
        :param string:
        :param substring:
        :return:
        """

        if not string or not substring:
            return ""
        # dictionary to keep count of all unique characters in
        # given sub string.
        substring_dict = Counter(substring)

        # filter all characters from string into a new list
        # along with their indexes
        # Criteria is the the character should be present in
        # substring dictionary
        filtered_string = []
        for index, char in enumerate(string):
            if char in substring_dict:
                filtered_string.append((index, char))

        # left, right pointers of sliding window
        # formed is to keep track of how many unique characters in substring
        # are present from the current string window frequency.
        left = right = formed = 0
        # number of unique character in the given substring
        # and windows count to keep track of the characters
        # repetition count.
        required, windows_count = len(substring_dict), {}
        # to store the lowest window
        # form: (window length, left, right)
        ans = float("inf"), None, None

        # Look for the characters only in filtered list instead of entire string.
        # This helps to reduce our search
        while right < len(filtered_string):
            # pick the cha
            char = filtered_string[right][1]
            windows_count[char] = windows_count.get(char, 0) + 1
            if windows_count[char] == substring_dict[char]:
                formed += 1
            # if the current window has all characters in desired frequencies
            # i.e., substring is present in the window
            while left <= right and formed == required:
                char = filtered_string[left][1]

                # keep updating the smallest window
                # until now
                end = filtered_string[right][0]
                start = filtered_string[left][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                windows_count[char] -= 1
                if windows_count[char] < substring_dict[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else string[ans[1]: ans[2] + 1]


if __name__ == "__main__":
    window = Window()
    print(window.get_minimum_window_substring("ADOBECODEBANC", "ABC"))