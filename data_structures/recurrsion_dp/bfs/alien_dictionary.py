from typing import List
from collections import defaultdict, Counter, deque


class AlienDictionary:

    def get_alien_order(self, words: List[str]) -> str:
        """
        Approach: Breadth First Search
        Time Complexity: O(C)
        Space Complexity: O(1)
        :param words:
        :return:
        """
        # Step 0:
        # set the data structures
        # initiate the in_degree with 0
        adjacent_list = defaultdict(set)
        in_degree = Counter({w: 0 for word in words for w in word})

        # Step 1:
        # build the adjacent list
        # increment the in_degree based of the adjacent list
        for first_word, second_word in zip(words, words[1:]):
            for fl, sl in zip(first_word, second_word):
                if fl != sl:
                    if sl not in adjacent_list[fl]:
                        adjacent_list[fl].add(sl)
                        in_degree[sl] += 1
                    break
            else:  # check the first word and second word length
                if len(second_word) < len(first_word):
                    return ""

        # Step 2:
        # initialise the output
        # put the no indegree letters into the queue
        output = []
        queue = deque([w for w in in_degree if in_degree[w] == 0])
        # loop through the queue and keep adding the no links to output
        while queue:
            l = queue.popleft()
            output.append(l)
            for nl in adjacent_list[l]:
                in_degree[nl] -= 1
                if in_degree[nl] == 0:
                    queue.append(nl)

        # check if the output length is less than in_degree length
        # if it is then return empty
        if len(output) < len(in_degree):
            return ""
        return "".join(output)


if __name__ == "__main__":
    alien_dictionary = AlienDictionary()
    print(alien_dictionary.get_alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
    print(alien_dictionary.get_alien_order(
        ["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt", "cdht", "ktgxt", "ktgch", "ktdw", "ktdc", "jqw", "jmc", "jmg"]))
