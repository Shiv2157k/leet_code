from typing import List


class Labels:

    def all_partition_labels_(self, string: str) -> List[int]:
        """
        Approach: Two Pointers / Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """
        # step 1: store last occurrence of each table in a dictionary
        last_occurrence = dict()
        for index, char in enumerate(string):
            last_occurrence[char] = index
        partitions = []
        left = right = 0
        for index, char in enumerate(string):
            right = max(right, last_occurrence[char])
            if index == right:
                partitions.append(index - left + 1)
                left = index + 1
        return partitions

    def all_partition_labels(self, string: str) -> List[int]:
        """
        Approach: Two Pointers / Greedy
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param string:
        :return:
        """

        # step 1: store last occurrence of each table in a dictionary
        last_occurrence = dict()
        for index, char in enumerate(string):
            last_occurrence[char] = index
        # step 2: initialize start and end pointers to
        #         keep track of each partition  string length
        left, right = 0, None
        # initialize list to store all the partitions
        partitions = []
        # step 3: loop through and store all the partitions into a ist
        for index, char in enumerate(string):
            # if the right pointer is none
            # initialize it with current char occurrence value
            if right is None:
                right = last_occurrence[char]
            # if the character occurrence and current index is same
            # that is we have reached a partition
            # reset the two pointers
            if index == right:
                partitions.append(right - left + 1)
                left = right + 1
                right = None
            elif last_occurrence[char] > right:
                right = last_occurrence[char]
        return partitions


if __name__ == "__main__":
    labels = Labels()
    print(labels.all_partition_labels("ababcbacadefegdehijhklij"))
    print(labels.all_partition_labels_("ababcbacadefegdehijhklij"))
