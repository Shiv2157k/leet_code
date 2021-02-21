from typing import List

from sortedcontainers import SortedList


class Soldiers:

    def get_high_low(self, sl, rate):
        """
        :param ls:
        :param s:
        :return:
        """
        lo = sl.bisect_left(rate)
        hi = len(sl) - lo
        return lo, hi

    def team_numbers_(self, rating: List[int]) -> int:
        """
        Approach: Using SortedList
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param rating:
        :return:
        """
        teams = 0
        left = SortedList()
        right = SortedList(rating)

        for rate in rating:
            right.remove(rate)
            loL, hiL = self.get_high_low(left, rate)
            loR, hiR = self.get_high_low(right, rate)
            teams += loL * hiR + loR * hiL
            left.add(rate)
        return teams




    def team_numbers(self, rating: List[int]) -> int:
        """
        Approach: Primitive loop
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param ratings:
        :return:
        """
        teams = 0
        for p in range(1, len(rating)):
            x, loL, hoL, loR, hoR = rating[p], 0, 0, 0, 0
            for left in range(p):
                if x < rating[left]:
                    loL += 1
                else:
                    hoL += 1
            for right in range(p + 1, len(rating)):
                if x < rating[right]:
                    loR += 1
                else:
                    hoR += 1
            teams += loL * hoR + hoL * loR
        return teams


if __name__ == "__main__":
    soldiers = Soldiers()
    print(soldiers.team_numbers([2, 5, 3, 4, 1]))
    print(soldiers.team_numbers([1, 2, 3, 4, 5]))
    print(soldiers.team_numbers_([2, 5, 3, 4, 1]))
    print(soldiers.team_numbers_([1, 2, 3, 4, 5]))
