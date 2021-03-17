import heapq
from typing import List
from collections import defaultdict
from itertools import combinations


class Analyzer:

    def most_visited_pattern(self, timestamp: List[int], username: List[str], website: List[str]):
        """
        Approach:
        Time Complexity: O(N^3) - N: maximum number of websites per user.
        Space Complexity: O(N)
        :param timestamp:
        :param username:
        :param website:
        :return:
        """
        # for sorting it based on timestamp, username and website
        heap = []
        for idx in range(len(timestamp)):
            heapq.heappush(heap, (timestamp[idx], website[idx], username[idx]))

        users = defaultdict(list)
        while heap:
            _, web_site, user_name = heapq.heappop(heap)
            users[user_name].append(web_site)
        counter = defaultdict(int)
        maximum = 0
        result = tuple()

        for user, web_sites in users.items():
            combos = combinations(web_sites, 3)
            for sequence in set(combos):
                counter[sequence] += 1
                if counter[sequence] > maximum:
                    maximum = counter[sequence]
                    result = sequence
                elif counter[sequence] == maximum:
                    if result > sequence:
                        result = sequence
        return result


if __name__ == "__main__":
    analyzer = Analyzer()
    print(analyzer.most_visited_pattern(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
        ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    ))
