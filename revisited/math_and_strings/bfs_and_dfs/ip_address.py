from typing import List


class IPAddress:

    def get_all_valid(self, string: str) -> List[str]:
        """
        Approach: Back tracking - Recursion
        :param string:
        :return:
        """

        def is_valid(segment: str) -> bool:
            """
            Determines if the given segment is valid by below rules.
            It is valid:
            1. if the segment is less than or equal to 255.
            2. the first character could be '0' only if the segment is
               equal to '0'
            :param segment:
            :return:
            """
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1

        def update(curr_pos: int):
            """
            Appends the current list of segments to the list of solutions.
            :param curr_pos:
            :return:
            """
            segment = string[curr_pos + 1: n]
            if is_valid(segment):
                segments.append(segment)
                addresses.append(".".join(segments))
                segments.pop()

        def back_track(prev_pos=-1, dots=3):
            """
            Does the back tracking.
            :param prev_pos:
                the position of the previously place dot.
            :param dots:
                number of dots to place.
            :return:
            """
            # The current dot i.e., curr_pos can be placed in a
            # range from prev_pos + 1 to prev_pos + 4.
            # Dot cannot be placed after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = string[prev_pos + 1: curr_pos + 1]
                if is_valid(segment):
                    # place the dot.
                    segments.append(segment)
                    # if all the three dots are placed.
                    if dots - 1 == 0:
                        # add solution to the output.
                        update(curr_pos)
                    else:
                        # continue to place the dots.
                        back_track(curr_pos, dots - 1)
                    # remove the last placed dots
                    segments.pop()

        n = len(string)
        addresses, segments = [], []

        back_track()
        return addresses


if __name__ == "__main__":

    ip_address = IPAddress()
    print(ip_address.get_all_valid("25525511135"))
