from typing import List


class Strings:

    def get_longest_common_prefix(self, strs: List[str]):
        """
        Approach: Binary Search
        Time Complexity: O(S log m)
        Space Complexity: O(1)
        :param strs:
        :return:
        """
        if not strs:
            return ""

        min_str = min(strs, key=len)
        left, right = 0, len(min_str)

        while left <= right:
            pivot = (left + right) // 2
            prefix = strs[0][:pivot]
            if all(s.startswith(prefix) for s in strs[1:]):
                left += 1
            else:
                right -= 1
        return strs[0][:(left + right) // 2]


if __name__ == "__main__":
    lprefix = Strings()
    print(lprefix.get_longest_common_prefix(["flowers", "floor", "flow"]))