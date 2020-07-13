from typing import List


class Palindrome:

    def partition_palindrome(self, s: str) -> List[List[str]]:
        """
        Approach: Recursion with Memoization.
        :param s:
        :return:
        """
        if not s:
            return []
        cache = {}

        def is_pal(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(string):
            if string in cache:
                return cache[string]
            res = []
            for i in range(len(string)):
                if is_pal(string[:i + 1]):
                    if i == len(string) - 1:
                        res.append([string[: i + 1]])
                    else:
                        subs = helper(string[i + 1:])
                        for sub in subs:
                            res.append([string[:i + 1]] + sub)
            cache[string] = res
            return res
        return helper(s)

    def is_palindrome(self, num: int) -> bool:
        """
        Approach: Revert to half
        :param num:
        :return:
        """
        if num < 0 or (num % 10 == 0 and num != 0):
            return False

        half = 0
        while num > half:
            half = half * 10 + num % 10
            num //= 10
        return num == half or num == half // 10

    def get_longest_palindrome_substring(self, string: str) -> str:
        """
        Approach: Manacher's Algorithm
        Time Complexity: O(n)
        :param string:
        :return:
        """
        # adding special characters to handle even palindrome.
        new_string = '#'.join('@{}!'.format(string))
        # main center and right boundary.
        center = boundary = 0
        length = len(new_string)
        # to track the palindrome substring lengths and centers.
        pal_track = [0] * length

        for mid in range(1, length - 1):

            # formulae for finding the mirror
            mirror = 2 * center - mid
            # if mid is inside the range of right boundary then update
            # the palindrome tracker.
            if mid < boundary:
                pal_track[mid] = min(boundary - mid, pal_track[mirror])

            # expand the current mid and update the new length of the
            # palindrome.
            while mid - 1 - pal_track[mid] >= 0 and mid + 1 + pal_track[mid] < length  \
                    and new_string[mid - 1 - pal_track[mid]] == new_string[mid + 1 + pal_track[mid]]:
                pal_track[mid] += 1

            # update the main center and the boundary if
            # new palindrome centered at mid is past the boundary.
            if mid + pal_track[mid] > boundary:
                center = mid
                boundary = mid + pal_track[mid]

        # find the maximum length of the palindrome and its center index.
        max_len, pal_index = max((val, i) for i, val in enumerate(pal_track))
        return string[(pal_index - max_len) // 2: (max_len + pal_index) // 2]


if __name__ == "__main__":
    pal = Palindrome()
    print(pal.is_palindrome(112111))
    print(pal.get_longest_palindrome_substring("ababbdbdbbdbdbbbdbbddsljef"))
    print(pal.partition_palindrome("aab"))