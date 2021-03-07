import heapq
from itertools import combinations
from typing import List
from collections import defaultdict


class Analyzer:

    def analyze_pattern(self, username: List[str], timestamps: List[int], websites: List[str]):
        """
        Approach: Using heapq, combinations and defaultdict.
        :param username:
        :param timestamps:
        :param websites:
        :return:
        """
        # sort them based on time stamps
        heap = []
        for i in range(len(username)):
            heapq.heappush(heap, (timestamps[i], username[i], websites[i]))

        # store all the website visited by user
        users = defaultdict(list)
        while heap:
            _, user, web_site = heapq.heappop(heap)
            users[user].append(web_site)

        # get the combinations and gather the common count
        count = defaultdict(int)
        maximum, result = 0, tuple()

        for user, web_sites in users.items():
            combos = combinations(web_sites, 3)
            for sequence in set(combos):
                count[sequence] += 1
                if maximum < count[sequence]:
                    maximum = count[sequence]
                    result = sequence
                elif count[sequence] == maximum:
                    if sequence < result:
                        result = sequence
        return result


if __name__ == "__main__":
    analyzer = Analyzer()
    print(analyzer.analyze_pattern(
        ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        [1, 2, 3, 4, 1, 6, 7, 8, 9, 10],
        ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    ))
