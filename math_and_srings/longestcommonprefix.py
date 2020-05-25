class LongestCommonPrefix:

    def longest_common_prefix_1(self, string: str) -> str:
        """
        Approach: Using min and max function.
        :param string:
        :return:
        """
        if not string:
            return ''
        m, M = min(string), max(string)

        for i, letter in enumerate(m):
            if letter != M[i]:
                return m[:i]
        return m

    def longest_common_prefix_2(self, string: str) -> str:
        """
        Approach: Binary Search
        :param string:
        :return:
        """
        if not string:
            return ''
        m = min(string, key=len)
        left, right = 0, len(m)

        while left <= right:
            pivot = (left + right) // 2
            prefix = string[0][:pivot]
            if all(s.startswith(prefix) for s in string[1:]):
                left = pivot + 1
            else:
                right = pivot - 1
        return string[0][:(left + right) // 2]


if __name__ == "__main__":
    lcp = LongestCommonPrefix()
    print(lcp.longest_common_prefix_1(['flower', 'flow', 'float']))
    print(lcp.longest_common_prefix_2(['flower', 'flow', 'float']))