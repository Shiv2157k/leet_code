class String:

    def last_substring_in_lexographic_order(self, s: str) -> str:
        """
        Intuition: We need the first element and moving forward all to be the largest.
        Approach: Three Pointer / Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :return:
        """

        marker = left = 0
        right = 1
        # "abczabzzcdzazc"
        while marker + right < len(s):

            # if they are same element increment the marker
            # in this case both the right and left moves forward
            if s[marker + left] == s[marker + right]:
                marker += 1
                continue

            # if the left character is greater than right character
            # increment only the right pointer moves forward
            if s[marker + left] > s[marker + right]:
                right = right + marker + 1
            # if the left character is lesser than the right character
            # update both the left and right pointer
            else:
                left = max(right, left + marker)
                right = left + 1
            # re-set the marker
            marker = 0
        return s[left:]


if __name__ == "__main__":
    string = String()
    print(string.last_substring_in_lexographic_order("abab"))
    print(string.last_substring_in_lexographic_order("abczabzzcdzazc"))
    print(string.last_substring_in_lexographic_order("abczabzlcdzmzc"))