class String:

    def last_substring_in_lexograph_order(self, s: str) -> str:
        """
        Approach: Two Pointers with a marker
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """
        left = tracker = 0
        right = 1
        while  right + tracker < len(s):
            # if both the left and right are same
            # increment the marker and skip the loop
            if s[left + tracker] == s[right + tracker]:
                tracker += 1
                continue
            elif s[left + tracker] > s[right + tracker]:
                # move the right with adding the marker value to it
                right = right + tracker + 1
            else:
                # update left and right
                left = max(left + tracker, right)
                right = right + 1
            # un mark the tracker
            tracker = 0
        return s[left:]


if __name__ == "__main__":
    string = String()
    print(string.last_substring_in_lexograph_order("ababa"))
    print(string.last_substring_in_lexograph_order("leetcode"))
    print(string.last_substring_in_lexograph_order("akabazaba"))
