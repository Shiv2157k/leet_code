class Anagram:

    def is_valid(self, s: str, t: str) -> bool:
        """
        Approach: Hash Table
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :param t:
        :return:
        """
        # validation
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for i in range(len(s)):
            counter[ord(s) - ord("a")] += 1
            counter[ord(t) - ord("a")] -= 1

        for count in counter:
            if count:
                return False
        return True
