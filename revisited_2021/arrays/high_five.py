from typing import List


class HighFive:

    def average_(self, items: List[List[int]]) -> List[int]:
        """
        Approach: Without python built in.
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param items:
        :return:
        """
        mapper = {}
        averages = []

        items.sort()
        for item in items:
            if item[0] in mapper:
                mapper[item[0]].append(item[1])
            else:
                mapper[item[0]] = [item[1]]
        for id, scores in mapper.items():
            scores.sort(reverse=True)
            total, i = 0, 0
            while i < 5 and i < len(scores):
                total += scores[i]
                i += 1
            averages.append([id, total//5])
        return averages

    def average(self, items: List[List[int]]) -> List[int]:
        """
        Approach: Python built-in
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        :param items:
        :return:
        """
        from collections import defaultdict
        items.sort()
        mapper, average = defaultdict(list), []

        for item in items:
            mapper[item[0]].append(item[1])

        for id, scores in mapper.items():
            scores.sort(reverse=True)
            average.append([id, sum(scores[:5]) // 5])
        return average


if __name__ == "__main__":
    high_five = HighFive()
    print(high_five.average(
        [[5, 91], [5, 92], [3, 93], [3, 97], [5, 60], [3, 77], [5, 65], [5, 87], [5, 100], [3, 100], [3, 76]]))
    print(high_five.average_(
        [[5, 91], [5, 92], [3, 93], [3, 97], [5, 60], [3, 77], [5, 65], [5, 87], [5, 100], [3, 100], [3, 76]]))
