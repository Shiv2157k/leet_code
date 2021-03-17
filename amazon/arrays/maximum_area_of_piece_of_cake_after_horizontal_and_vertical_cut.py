from typing import List


class Cake:

    def max_area_cut(self, h: int, w: int, horizontal_cuts: List[int], vertical_cuts: List[int]):
        """
        Approach: Sorting with no extra space
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param h:
        :param w:
        :param horizontal_cuts:
        :param vertical_cuts:
        :return:
        """
        # step 1: sort the horizontal and vertical cuts.
        horizontal_cuts = sorted(horizontal_cuts)
        vertical_cuts = sorted(vertical_cuts)

        # step 2: append the height and width at then end of the
        #         array for handling borders
        horizontal_cuts.append(h)
        vertical_cuts.append(w)
        # step 3: initialize max width and max height
        max_width = max_height = prev_hc = prev_wc = 0
        # step 4: individually loop through the cuts and find
        #         maximum height and maximum width
        for horizontal_cut in horizontal_cuts:
            max_height = max(max_height, horizontal_cut - prev_hc)
            prev_hc = horizontal_cut
        for vertical_cut in vertical_cuts:
            max_width = max(max_width, vertical_cut - prev_wc)
            prev_wc = vertical_cut

        # step 5: return max_width * max_height
        return (max_width * max_height) % (10**9 + 7)


if __name__ == "__main__":
    cake = Cake()
    print(cake.max_area_cut(5, 4, [1, 4, 2], [1, 3]))