from collections import Counter


class Window:

    def get_min_window_substring(self, string: str, target: str) -> str:
        """
        Approach: Optimized Sliding Window.
        Time Complexity: O(|S| + |T|)
        Space Complexity: O(|S| + |T|)
        :param string:
        :param target:
        :return:
        """

        if not target or not string:
            return ""

        char_counts = Counter(target)
        required = len(char_counts)
        left = right = formed = 0
        filtered_string = []
        for idx, char in enumerate(string):
            if char in char_counts:
                filtered_string.append((idx, char))

        ans = float("inf"), None, None
        window_counts = {}

        while right < len(filtered_string):
            char = filtered_string[right][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == char_counts[char]:
                formed += 1

            while left <= right and required == formed:
                char = filtered_string[left][1]

                end = filtered_string[right][0]
                start = filtered_string[left][0]

                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[char] -= 1
                if window_counts[char] < char_counts[char]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float("inf") else string[ans[1]: ans[2] + 1]

    def get_min_window_substring_(self, string: str, target: str) -> str:
        """
        Approach: Sliding Window
        Time Complexity: O (|S| + |T|)
        Space Complexity: O (|S| + |T|)
        :param string:
        :param target:
        :return:
        """

        if not target or not string:
            return ""

        # store the character counts in the target
        char_tracker = Counter(target)
        # number of substring length required
        required = len(char_tracker)

        # left - left pointer
        # right - right pointer
        # formed - tracker to keep track of formed words in a window
        left = right = formed = 0

        # keep track of character counts in a window
        window_counts = {}

        # a tuple consisting of below
        # window length, left, right
        ans = float("inf"), None, None

        while right < len(string):
            char = string[right]

            # by default if this is a new character add 1 else
            # increment the existing count by 1
            window_counts[char] = window_counts.get(char, 0) + 1

            # check whether target character is present in the window
            # with same repetitions and increment the formed.
            if char in char_tracker and window_counts[char] == char_tracker[char]:
                formed += 1

            # once we have all the required characters
            # start contracting the left pointer
            while left <= right and required == formed:
                char = string[left]

                # if we found a minimum window update the window length
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                # if the character at left pointer pointed is no longer part of window
                window_counts[char] -= 1
                if char in char_tracker and window_counts[char] < char_tracker[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if ans[0] == float("inf") else string[ans[1]: ans[2] + 1]


if __name__ == "__main__":
    window = Window()
    print(window.get_min_window_substring("ADOBECODEBANC", "ABC"))
    print(window.get_min_window_substring_("ADOBECODEBANC", "ABC"))

