from typing import List
from collections import defaultdict


class WordLadder:

    def get_all_minimum(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        """
        Approach: DFS
        :param begin_word:
        :param end_word:
        :param word_list:
        :return:
        """
        tree, word_set, n = defaultdict(set), set(word_list), len(begin_word)

        # base case
        if end_word not in word_list:
            return []

        found, queue, next_queue = False, {begin_word}, set()

        while queue and not found:
            word_set -= set(queue)
            for w in queue:
                for y in [w[:i] + c + w[i + 1:] for i in range(n) for c in "qwertyuiopasdfghjklmnbvcxz"]:
                    if y in word_set:
                        if y == end_word:
                            found = True
                        else:
                            next_queue.add(y)
                        tree[w].add(y)
            queue, next_queue = next_queue, set()

        def back_track(x):
            return [[x]] if x == end_word else [[x] + rest for y in tree[x] for rest in back_track(y)]

        return back_track(begin_word)


if __name__ == "__main__":
    word_ladder = WordLadder()
    print(word_ladder.get_all_minimum("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))