from collections import defaultdict


class Words:

    def re_arrange(self, text: str) -> str:
        """
        Approach: Using Adjacency list
        Time Complexity: O(N * R)
        R - Repetition
        Space Complexity: O(N)
        :param text:
        :return:
        """

        adjacency_list = defaultdict(list)
        w = text.split(" ")

        for word in w:
            adjacency_list[len(word)].append(word)

        max_len = max(adjacency_list)
        result = []

        for key in range(1, max_len + 1):
            if key in adjacency_list:
                for word in adjacency_list[key]:
                    result.append(word)

        return " ".join(result).capitalize()


if __name__ == "__main__":
    words = Words()
    print(words.re_arrange("Keep calm and do leetcode and have fun"))