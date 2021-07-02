from typing import List


class Cake:

    def max_area(self, h: int, w: int, horizontal_cuts: List[int], vertical_cuts: List[int]) -> int:
        """
        Approach: Sort
        Time Complexity: O(N log (N) + M log (M))
        Space Complexity: O(1)
        :param h:
        :param w:
        :param horizontal_cuts:
        :param vertical_cuts:
        :return:
        """

        horizontal_cuts = sorted(horizontal_cuts)
        vertical_cuts = sorted(vertical_cuts)

        horizontal_cuts.append(h)
        vertical_cuts.append(w)

        max_height = max_width = 0
        prev_hc = prev_wc = 0

        for horizontal_cut in horizontal_cuts:
            max_height = max(max_height, horizontal_cut - prev_hc)
            prev_hc = horizontal_cut

        for vertical_cut in vertical_cuts:
            max_width = max(max_width, vertical_cut - prev_wc)
            prev_wc = vertical_cut

        return (max_height * max_width) % (10**9 + 7)


if __name__ == "__main__":
    cake = Cake()
    print(cake.max_area(5, 4, [1, 2, 4], [1, 3]))
