from typing import List


class LogFiles:

    def re_order(self, logs: List[str]):

        def get_key(logs):
            _id, rest = logs.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)
        return sorted(logs, key=get_key)


if __name__ == "__main__":
    log_files = LogFiles()
    print(log_files.re_order(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    ))
    print(log_files.re_order(
        ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    ))