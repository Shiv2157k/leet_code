from typing import List


class LogFile:

    def re_order(self, logs: List[str]) -> List[str]:
        """
        Rules:
        -----
        1. Letter logs should be prioritized above all digit logs.
        2. Among letter logs, we should further sort them based on firstly
           on their content and then on their identifiers if content are
           identical.
        3. Among digit logs, they should remain in same order as they are
           in collection.
        Approach: Sorting by keys
        Time Complexity: O(M * N log N)
        Space Complexity: O(M * N)
        :param logs:
        :return:
        """

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, _id, rest) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)


if __name__ == "__main__":
    log_file = LogFile()
    print(log_file.re_order(
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero"
        ]
    ))
