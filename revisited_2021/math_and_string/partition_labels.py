from typing import List


class Labels:

    def get_partitions(self, string: str) -> List[int]:
        """
        Approach:
        Time Complexity:
        Space Complexity:
        :param string:
        :return:
        """
        # store the occurrences
        last_occurrence, partitions = {}, []
        start, end = 0, None
        for i, char in enumerate(string):
            last_occurrence[char] = i

        # make intervals
        for i, char in enumerate(string):
            if end is None:
                end = last_occurrence[char]
            if end == i:
                partitions.append(end - start + 1)
                start = end + 1
                end = None
            elif last_occurrence[char] > end:
                end = last_occurrence[char]

        # return results
        return partitions


if __name__ == "__main__":
    labels = Labels()
    print(labels.get_partitions("ababcbacadefegdehijhklij"))
    print(labels.get_partitions("abacdc"))
