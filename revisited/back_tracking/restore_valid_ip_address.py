from typing import List


class IPAddress:

    def restore(self, s: str) -> List[List[str]]:
        """
        Approach: Backtracking
        Time Complexity:
        Space Complexity:
        :param s:
        :return:
        """

        def valid(segment: str) -> bool:
            """
            Checks if the current segment is valid or not
            1. less than or equal to 255
            2. no leading zeros
            :param segment:
            :return:
            """
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1

        def update(curr_pos: int):
            """
            Updates the last dot position
            :param curr_pos:
            :return:
            """
            segment = s[curr_pos + 1: length]
            if valid(segment):
                segments.append(segment)
                addresses.append(".".join(segments))
                segments.pop()  # pop out the last added segment

        def back_track(prev_pos: int = -1, dots: int = 3):
            # loop through all the possible
            # segments in range prev_pos to min(prev_pos + 4, n - 1)
            for curr_pos in range(prev_pos + 1, min(length - 1, prev_pos + 4)):
                # pick a segment from the given string
                segment = s[prev_pos + 1: curr_pos + 1]
                if valid(segment):  # if segment is valid add it to segments
                    segments.append(segment)
                    # if you have reached last dot placement
                    if dots - 1 == 0:
                        update(curr_pos)  # update the last one
                    else:  # keep back tracking
                        back_track(curr_pos, dots - 1)
                    segments.pop()  # pop the last segment out
        length = len(s)
        # to store all valid ip addresses
        addresses = []
        # to store each valid segment
        segments = []
        back_track()
        return addresses


if __name__ == "__main__":
    ip_addresses = IPAddress()
    print(ip_addresses.restore("25525511135"))
