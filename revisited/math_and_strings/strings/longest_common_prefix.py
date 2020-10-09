from typing import List


class Prefix:

    def get_longest_common(self, strs: List[str]) -> str:
        """
        Approach: Min and Max
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param strs:
        :return:
        """
        # base case
        if not strs:
            return ""

        min_str = min(strs)
        max_str = max(strs)

        for index, letter in enumerate(min_str):
            if letter != max_str[index]:
                return min_str[:index]
        return min_str

    def get_longest_common_(self, strs: List[str]) -> str:
        """
        Approach: Binary Search
        Time Complexity: O(S log m)
        Space Complexity: O(1)
        :param strs:
        :return:
        """

        # base case
        if not strs:
            return ""
        # get the minimum length string
        min_len_str = min(strs, key=len)
        # initiate
        # left pointer to zero
        # right pointer to the length of min length string
        left, right = 0, len(min_len_str)
        # loop through until left is less than or equal to right
        while left <= right:

            # calculate the middle index
            pivot = (left + right) // 2
            # get the prefix from 1st index string
            pref = strs[0][:pivot]
            # check if all the strings has same prefix
            # if true increment the left pointer by 1
            if all(s.startswith(pref) for s in strs[1:]):
                left += 1
            else:  # decrement the right pointer by 1
                right -= 1
        return strs[0][:(left + right) // 2]


if __name__ == "__main__":
    prefix = Prefix()
    print(prefix.get_longest_common(["float", "flow", "flight"]))
    print(prefix.get_longest_common_(["float", "flow", "flight"]))
    print(prefix.get_longest_common(["float", "glow", "light"]))
    print(prefix.get_longest_common_(["float", "glow", "light"]))