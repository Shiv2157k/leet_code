from typing import List
from collections import deque, defaultdict, Counter


class AlienDictionary:

    def get_order(self, words: List[str]) -> str:
        """
        Approach: BFS
        N -> Total number of strings in words
        U -> Unique characters in word dictionary
        C -> total number of words in word dictionary
        Time Complexity: O(C)
        Space Complexity: O(1) or O(U + min(U^2, N))
        :param words:
        :return:
        """
        # Step: 0
        # build the reverse adjacent list
        rev_adj_list = {char: [] for word in words for char in word}

        # Find all the edges and put them inside reverse adjacent list
        for first_word, second_word in zip(words, words[1:]):
            for fl, sl in zip(first_word, second_word):
                if fl != sl:
                    rev_adj_list[sl].append(fl)
                    break
            else: # check second word isn't a prefix of first word
                if len(second_word) < len(first_word):
                    return ""

        seen = {}  # False - grey, True - black
        output = []

        def visit(node):
            # base case
            if node in seen:
                return seen[node]

            seen[node] = False  # represents marked as grey
            for next_node in rev_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False  # cycle was detected go down

            seen[node] = True  # mark as black which means no more going down
            output.append(node)
            return True

        if not all(visit(node) for node in rev_adj_list):
            return ""

        return "".join(output)

    def get_order_of_words(self, words: List[str]) -> str:
        """
        Approach: BFS
        N -> Total number of strings in words
        U -> Unique characters in word dictionary
        C -> total number of words in word dictionary
        Time Complexity: O(C)
        Space Complexity: O(1) or O(U + min(U^2, N))
        :param words:
        :return:
        """
        # Step:0
        # - set up the data structures for adjacent list and in degree
        adjacent_list = defaultdict(set)
        in_degree = Counter({char: 0 for word in words for char in word})

        # Step 1:
        # generate the adjacent list link
        # generate the in degree count
        for first_word, second_word in zip(words, words[1:]):
            for first_letter, second_letter in zip(first_word, second_word):
                if first_letter != second_letter:
                    if second_letter not in adjacent_list[first_letter]:
                        # add the second letter as a
                        adjacent_list[first_letter].add(second_letter)
                        # count the in degree link
                        in_degree[second_letter] += 1
                    break
            else:  # if first and second letter are not prefix return empty string
                if len(second_word) < len(first_word):
                    return ""

        # Step 2:
        # Assembling a valid alphabet ordering
        # add all the characters with count 0 in the in_degree
        # as those doesn't have link in wards to them
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        output = []

        # loop through the queue until it is empty
        while queue:
            char = queue.popleft()
            output.append(char)
            for link in adjacent_list[char]:
                in_degree[link] -= 1
                if in_degree[link] == 0:
                    queue.append(link)

        # base case if the output doesn't have all the unique characters
        # means it is not a valid dictionary and return "" as per problem
        if len(output) < len(in_degree):
            return ""
        return "".join(output)


if __name__ == "__main__":
    alien_dict = AlienDictionary()
    print(alien_dict.get_order_of_words(["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt", "cdht", "ktgxt", "ktgch", "ktdc", "jqw", "jmc", "jmg"]))
    print(alien_dict.get_order_of_words(["wrt", "wrf", "er", "ett", "rftt"]))
    print(alien_dict.get_order(["wxqkj", "whqg", "cckgh", "cdxg", "cdxdt", "cdht", "ktgxt", "ktgch", "ktdc", "jqw", "jmc", "jmg"]))
    print(alien_dict.get_order(["wrt", "wrf", "er", "ett", "rftt"]))


