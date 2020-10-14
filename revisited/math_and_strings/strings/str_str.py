class Strstr:

    def get_needle_index_(self, haystack: str, needle: str) -> int:
        """
        Approach: Two Pointers - Linear Time Slice
        Time Complexity: O((N - H) N)
        Space Complexity: O(1)
        :param haystack:
        :param needle:
        :return:
        """
        N, H = len(needle), len(haystack)

        if N == 0:
            return 0

        pH = 0
        while pH < H - N + 1:
            # find the starting char of needle index in the haystack
            while pH < H - N + 1 and haystack[pH] != needle[0]:
                pH += 1

            # initiate variables to traverse the valid needle strings
            pN = 0
            while pN < N and pH < H and haystack[pH] == needle[pN]:
                # increment the pointers
                pN += 1
                pH += 1

            # if we have reached the end of needle
            # return the index
            if pN == N:
                return pH - N
            # other wise back track the pH
            pH = pH - pN + 1
        return - 1

    def get_needle_index__(self, haystack: str, needle: str) -> int:
        """
        Approach: Substring - Linear Time Slice
        Time Complexity: O((N - H) N)
        Space Complexity: O(1)
        :param haystack:
        :param needle:
        :return:
        """
        N, H = len(needle), len(haystack)

        for start in range(H - N + 1):
            if haystack[start: start + N] == needle:
                return start
        return -1

    # Rabin Karp algorithm needs to be revisited


if __name__ == "__main__":
    str_str = Strstr()
    print(str_str.get_needle_index__("hello", "ll"))
    print(str_str.get_needle_index_("hello", "ll"))