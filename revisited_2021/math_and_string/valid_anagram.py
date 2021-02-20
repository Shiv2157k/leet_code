

class Anagram:

    def is_valid(self, s: str, t: str):
        """
        Approach: Hash Table
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] += 1
            counter[ord(t[i]) - ord("a")] -= 1

        for count in counter:
            if count != 0:
                return False
        return True


if __name__ == "__main__":
    anagram = Anagram()
    print(anagram.is_valid("rat", "tar"))
    print(anagram.is_valid("", ""))
    print(anagram.is_valid("a", "b"))