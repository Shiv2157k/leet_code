from typing import List


class Cake:

    def max_area(self, h: int, w: int, hc: List[int], wc: List[int]) -> int:
        """
        Approach: Optimized (max height * max width)
        Time Complexity: O(N log N)
        Space Complexity: O(1)
        :param h:
        :param w:
        :param hc:
        :param wc:
        :return:
        """
        hc, wc = sorted(hc), sorted(wc)
        hc.append(h)
        wc.append(w)
        max_height = max_width = prev_height = prev_width = 0
        for height in hc:
            max_height = max(max_height, height - prev_height)
            prev_width = height
        for width in wc:
            max_width = max(max_width, width - prev_width)
            prev_width = width
        return max_height * max_width % 1000000007

    def max_area_(self, h: int, w: int, hc: List[int], wc: List[int]) -> int:
        """
        Naive Approach
        Time Complexity: O(MN)
        Space Complexity: O(1)
        :param h:
        :param w:
        :param hc:
        :param wc:
        :return:
        """
        horizontal_cuts = sorted(hc)
        vertical_cuts = sorted(wc)
        horizontal_cuts.append(h)
        vertical_cuts.append(w)
        max_area = prev_hc = 0
        for horizontal_cut in horizontal_cuts:
            prev_wc = 0
            for vertical_cut in vertical_cuts:
                area = (horizontal_cut - prev_hc) * (vertical_cut - prev_wc)
                max_area = max(area, max_area)
                prev_wc = vertical_cut
            prev_hc = horizontal_cut
        return max_area


if __name__ == "__main__":
    cake = Cake()
    print(cake.max_area(5, 4, [1, 2, 4], [1, 3]))
    print(cake.max_area_(5, 4, [1, 2, 4], [1, 3]))
