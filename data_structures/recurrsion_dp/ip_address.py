from typing import List


class IpAddress:

    def get_valid_combinations(self, s: str) -> List[str]:

        # validator of each segment
        def valid(segment):
            return int(segment) <= 255 if segment[0] != "0" else len(segment) == 1

        # update if it is the last dot
        def update_address(curr_pos):
            segment = s[curr_pos + 1: n]
            if valid(segment):
                segments.append(segment)
                addresses.append(".".join(segments))
                segments.pop()

        # back track all the combinations
        def back_track(prev_pos=-1, dots=3):
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):

                segment = s[prev_pos + 1: curr_pos + 1]
                if valid(segment):
                    segments.append(segment)
                    if dots - 1 == 0:
                        update_address(curr_pos)
                    else:
                        back_track(curr_pos, dots - 1)
                    segments.pop()

        n = len(s)
        addresses, segments = [], []
        back_track()
        return addresses


if __name__ == "__main__":
    ip_address = IpAddress()
    print(ip_address.get_valid_combinations("25525511135"))