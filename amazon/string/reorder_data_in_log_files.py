from typing import List


class Logs:

    def reorder(self, logs: List[str]) -> List[str]:
        """
        Approach: Sorting by Keys
        Time Complexity: O(M * N* log N)
        Space Complexity: O(M * N)
        :param logs:
        :return:
        """
        def get_key(logs: str):
            _id, rest = logs.split(maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)
        return sorted(logs, key=get_key)


if __name__ == "__main__":
    log = Logs()
    print(log.reorder(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    ))