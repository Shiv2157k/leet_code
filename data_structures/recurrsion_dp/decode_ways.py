class Decode:

    def get_number_of_ways(self, s: str) -> int:
        """
        Approach: Recursion with memoization.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """

        def memoization(index: int, s: str) -> int:

            # if it reaches the end of the string return 1
            if index == len(s):
                return 1

            # if the string contains zero return 0
            # can't decoded return 0
            if s[index] == "0":
                return 0

            if index == len(s) - 1:
                return 1

            # check if it already exists in the cache
            # return the value from cache
            if index in cache:
                return cache[index]

            result = memoization(index + 1, s) + \
                     (memoization(index + 2, s) if (int(s[index: index + 2]) <= 26) else 0)
            cache[index] = result
            return result

        cache = {}
        # validation
        if not s:
            return 0
        return memoization(0, s)

    def get_number_of_ways_(self, s: str) -> int:
        """
        Approach: Iteration with dp
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param s:
        :return:
        """
        if not s:
            return 0

        tracker = [0 for _ in range(len(s) + 1)]
        tracker[0] = 1
        tracker[1] = 0 if s[0] == "0" else 1
        for index in range(2, len(tracker)):
            # handling single digit
            if s[index - 1] != "0":
                tracker[index] += tracker[index - 1]
            # handling two digit
            two_digit = int(s[index - 2: index])
            if 10 <= two_digit <= 26:
                tracker[index] += tracker[index - 2]
        return tracker[len(s)]


if __name__ == "__main__":
    decode = Decode()
    print(decode.get_number_of_ways("226"))
    print(decode.get_number_of_ways_("226"))

    print(decode.get_number_of_ways("3226"))
    print(decode.get_number_of_ways_("3226"))

    print(decode.get_number_of_ways("11226"))
    print(decode.get_number_of_ways_("11226"))
