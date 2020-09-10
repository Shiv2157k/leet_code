from typing import List
from collections import defaultdict, deque


class WordLadder:

    def get_ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Approach: Breadth First Search
        Time Complexity: O(M^2 * N)
        Space Complexity: O(M^2 * N)
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        # base case
        if end_word not in word_list or not end_word or not begin_word or not word_list:
            return 0

        # get the common length
        L = len(begin_word)

        # build the word combinations with *
        word_combo_dict = defaultdict(list)
        for word in word_list:
            for i in range(L):
                word_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # for keeping track of the word if it has been tracked or not
        visited = {begin_word: True}
        # queue to perform bfs
        queue = deque([(begin_word, 1)])

        # loop through the queue
        while queue:
            curr_word, level = queue.popleft()
            for i in range(L):
                inter_word = curr_word[:i] + "*" + curr_word[i + 1:]
                for word in word_combo_dict[inter_word]:

                    # if we have reached the end word return incrementing the level with 1
                    if word == end_word:
                        return level + 1

                    if word not in visited:
                        # mark the word as tracked
                        visited[word] = True
                        # add the word into the queue and increment the level.
                        queue.append((word, level + 1))
                # erase the inter_word from the dictionary
                word_combo_dict[inter_word] = []
        return 0


if __name__ == "__main__":
    word_ladder = WordLadder()
    print(word_ladder.get_ladder_length("hit",
                                        "cog",
                                        ["hot", "dot", "dog", "lot", "log", "cog"]
                                        ))

        # perform dfs