from typing import List


class SubString:

    def get_palindrome_partitions(self, string: str) -> List[List[str]]:

        # base case
        if not string:
            return []

        # verify palindrome
        def is_palindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        cache = {}

        # helper recursion function
        def helper(string: str) -> List[List[str]]:
            # base case
            if string in cache:
                return cache[string]
            res = []
            for start in range(len(string)):
                if is_palindrome(string[:start + 1]):
                    if start == len(string) - 1:
                        res.append([string[:start + 1]])
                    else:
                        sub_strs = helper(string[start + 1:])
                        for sub in sub_strs:
                            res.append([string[:start + 1]] + sub)
            cache[string] = res
            return res

        return helper(string)


if __name__ == "__main__":
    substring = SubString()
    print(substring.get_palindrome_partitions("aab"))