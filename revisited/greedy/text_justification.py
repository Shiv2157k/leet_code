from typing import List


class TextJustification:

    def justify(self, words: List[str], max_width: int) -> List[str]:
        """
        Approach: Greedy
        Time Complexity: O( lines * max_width)
        Space Complexity: O( lines * max_width)
        :param words:
        :param max_width:
        :return:
        """

        right_idx, text, n = 0, [], len(words)

        # until right index is less than the last index
        while right_idx < n:
            # left index where we start
            left_idx = right_idx
            # total number of spaces left from our max width
            # - 1 at the end for adding a minimum space after each word
            space_left = max_width - len(words[right_idx])
            # increment the right index
            right_idx += 1
            # keep incrementing right index until you can
            # loop through and decrement space left until it reaches 0
            while right_idx < n and space_left - len(words[right_idx]) - 1 >= 0:
                space_left -= len(words[right_idx]) - 1
                right_idx += 1

            # calculate the line length
            line_length = right_idx - left_idx
            # check whether it is a left justification or middle justification
            # condition for left justification
            #   if line length reaches the end or space left is just 1
            if right_idx == n or line_length == 1:
                text.append(" ". join(words[left_idx: right_idx]) + " " * space_left)
            else:  # if this is a middle justification
                # minimum space between each word of the current line length
                # i.e line length - 1
                space_sections = line_length - 1
                # number of space that needs to be added in each space section.
                # space_left - total number of spaces left
                # line length - how many words we are taking in on a line
                space_divider = (space_left + line_length - 1) // space_sections
                extra_space = space_left % space_sections
                line = ""

                # loop through the space section
                for i in range(space_sections):
                    line += words[left_idx + i] + " " * space_divider
                    # if i is less than extra space
                    if i < extra_space:
                        line += " "
                line += words[right_idx - 1]
                text.append(line)
        return text


if __name__ == "__main__":
    text_justification = TextJustification()
    print(text_justification.justify(["Shiva", "is", "having", "fun", "with", "leet", "code"], 11))

