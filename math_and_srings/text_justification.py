from typing import List


class Text:

    def justify_text(self, words: str, max_width: int) -> List[str]:
        """
        Approach: Greedy
        :param words:
        :param max_width:
        :return:
        """
        text, index = [], 0
        # while index is less then word length
        while index < len(words):
            line_start = index
            space_left = max_width - len(words[index])
            index += 1
            # keep looping until it reaches the maxWidth limit
            while index < len(words) and space_left - len(words[index]) - 1 >= 0:
                space_left = space_left - len(words[index]) - 1
                index += 1
            # total line length so far
            line_length = index - line_start
            # to handle single word at the end or last index in words
            if index == len(words) or line_length == 1:
                text.append(" ".join(words[line_start: index]) + " " * space_left)
            else:
                divider_count = line_length - 1
                divider_size = (space_left + line_length - 1) // divider_count
                big_divider_count = space_left % divider_count
                line = ""
                for i in range(divider_count):
                    line += words[line_start + i] + " " * divider_size
                    if i < big_divider_count:
                        line += " "
                line += words[index - 1]
                text.append(line)
        return text


if __name__ == "__main__":
    text = Text()
    print(text.justify_text(["This", "is", "an", "example", "of", "text", "justification."], 16))