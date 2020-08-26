from typing import List
from collections import defaultdict


class WordLadder:

    def find_ladder(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        """
        Approach: BFS - bidirectional
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """

        tree, word_set, n = defaultdict(set), set(word_list), len(begin_word)
        # base case
        if end_word not in word_set:
            return []

        # to indicate found a ladder path
        # to keep track of current level
        # for keeping track of next level
        found, queue, next_queue = False, {begin_word}, set()

        # while a path is found or queue is empty
        while queue and not found:
            # remove already used from word set
            word_set -= set(queue)

            # for each word in current level
            for w in queue:
                # for each with one word difference
                for y in [w[:i] + c + w[i + 1:] for i in range(n) for c in "qwertyuiopasdfghjklzxcvbnm"]:
                    # if present in the word set
                    if y in word_set:
                        # if found, reach the shortest sol level, won't do next level.
                        if y == end_word:
                            found = True
                        else:  # if not found
                            #  prepare the next queue
                            next_queue.add(y)
                        tree[w].add(y)  # add the trace
            queue, next_queue = next_queue, set()  # reset the while loop for next level

        def back_track(string):  # back tracking from the tree
            return [[string]] if string == end_word else[[string] + rest for y in tree[string] for rest in back_track(y)]
        return back_track(begin_word)


if __name__ == "__main__":
    word_ladder = WordLadder()
    print(word_ladder.find_ladder("hot", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
