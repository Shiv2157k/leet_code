from typing import List
from collections import defaultdict, deque


class WordLadder:

    def __init__(self):

        self.word_size = 0
        self.inter_word_combinations = defaultdict(list)

    def visit_word_node(self, queue: deque, visitor, other_visitor):

        curr_word, level = queue.popleft()
        for i in range(self.word_size):
            inter_word = curr_word[:i] + "*" + curr_word[i + 1:]
            for word in self.inter_word_combinations[inter_word]:
                if word in other_visitor:
                    return level + other_visitor[word]
                if word not in visitor:
                    visitor[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def get_ladder_length_(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Approach: BFS Bi-directional
        Time Complexity: O(M * N^2)
        Space Complexity: O(M * N^2)
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        if end_word not in word_list or not begin_word or not end_word or not word_list:
            return 0

        self.word_size = len(begin_word)

        for word in word_list:
            for i in range(self.word_size):
                self.inter_word_combinations[word[:i] + "*" + word[i + 1:]].append(word)

        queue_begin = deque([(begin_word, 1)])
        queue_end = deque([(end_word, 1)])

        visited_begin = {begin_word: 1}
        visited_end = {end_word: 1}

        ans = None

        while queue_begin and queue_end:
            ans = self.visit_word_node(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visit_word_node(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0

    def get_ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Approach: BFS
        Time Complexity: O(M * N^2)
        Space Complexity: O(M * N^2)
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        # validation
        if end_word not in word_list or not begin_word or not end_word or not word_list:
            return 0
        # length of words
        word_length = len(begin_word)
        # build a dictionary with combinations of words with ignoring
        # one letter from it and store them as keys and words as values.
        word_combinations = defaultdict(list)
        for word in word_list:
            for i in range(word_length):
                word_combinations[word[:i] + "*" + word[i + 1:]].append(word)

        # do the bfs using queues
        # add the beginWord and level to 1 in the queue
        # as a tuple
        queue = deque([(begin_word, 1)])
        # keep track of the words so that no repetition
        # takes place.
        visitor = {begin_word: True}

        # loop through the queue.
        while queue:
            # pop the current word and level
            current_word, level = queue.popleft()

            # loop through the word length
            for i in range(word_length):
                # intermediate word h*t
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # loop through the intermediate word combinations in the
                # combination dictionary
                for word in word_combinations[intermediate_word]:
                    # if the word is end word increase the level
                    if word == end_word:
                        return level + 1
                    # if the word is not in the visited
                    # mark it in the visitor dict
                    # add it to the queue and increase the level
                    if word not in visitor:
                        visitor[word] = True
                        queue.append((word, level + 1))
                # clean up the combination dict of the
                word_combinations[intermediate_word] = []
        return 0


if __name__ == "__main__":

    word_ladder = WordLadder()
    print(word_ladder.get_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(word_ladder.get_ladder_length_("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))



