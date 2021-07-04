from typing import List


class EarliestMoment:

    def when_every_one_becomes_friends(self, n: int, logs: List[List[int]]) -> int:
        """
        Approach: Union Find
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param n:
        :param logs:
        :return:
        """

        parent = [node for node in range(n)]

        def find(f1: int):
            while f1 != parent[f1]:
                f1 = parent[f1]
            return f1

        def union(f1: int, f2: int):
            nonlocal n
            p1 = find(f1)
            p2 = find(f2)

            if p1 != p2:
                parent[p1] = p2
                n -= 1

        for t, s1, s2 in sorted(logs):
            union(s1, s2)
            if n == 1:
                return t
        return -1
