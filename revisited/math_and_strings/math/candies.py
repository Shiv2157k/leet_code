from typing import List


class Candy:

    def get_all_candies(self, child_ratings: List[int]) -> int:
        """
        Approach: Single Pass with Constant Space
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param child_ratings:
        :return:
        """
        childs = len(child_ratings)
        if childs <= 1:
            return childs
        up = peak = down = 0
        total_candies = 1
        for child in range(1, childs):
            # peak
            if child_ratings[child] > child_ratings[child - 1]:
                up += 1
                down = 0
                peak = up
                total_candies += up + 1
            # if it is a flat surface
            elif child_ratings[child] == child_ratings[child - 1]:
                # reset all and add 1 to total candies
                up = down = peak = 0
                total_candies += 1
            else:  # valley
                down += 1
                up = 0
                total_candies += down + 1 + [0, -1][peak >= down]
        return total_candies

    def get_all_candies__(self, child_ratings: List[int]) -> int:
        """
        Approach: Using one array
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param child_ratings:
        :return:
        """
        childs = len(child_ratings)
        candies = [1] * childs

        for child in range(1, childs):
            if child_ratings[child] > child_ratings[child - 1]:
                candies[child] = candies[child - 1] + 1

        total_candies = candies[-1]
        for child in range(childs - 2, -1, -1):
            if child_ratings[child] > child_ratings[child + 1]:
                candies[child] = max(candies[child], candies[child + 1] + 1)
            total_candies += candies[child]
        return total_candies

    def get_all_candies___(self, child_ratings: List[int]) -> int:
        """
        Approach: Using two arrays
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param child_ratings:
        :return:
        """
        childs = len(child_ratings)
        left_2_right = [1] * childs
        right_2_left = [1] * childs

        for left in range(1, childs):
            if child_ratings[left] > child_ratings[left - 1]:
                left_2_right[left] = left_2_right[left - 1] + 1
            right = childs - 1 - left
            if child_ratings[right] > child_ratings[right + 1]:
                right_2_left[right] = right_2_left[right + 1] + 1

        total_candies = 0
        for i in range(childs):
            total_candies += max(left_2_right[i], right_2_left[i])
        return total_candies

    def get_all_candies____(self, child_ratings: List[int]) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        :param child_ratings:
        :return:
        """
        childs = len(child_ratings)
        flag = True
        candies = [1] * childs

        while flag:
            flag = False
            for child in range(childs):
                if child != childs - 1 and child_ratings[child] > child_ratings[child + 1] and candies[child] <= candies[child + 1]:
                    candies[child] = candies[child + 1] + 1
                    flag = True
                if child > 0 and child_ratings[child] > child_ratings[child - 1] and candies[child] <= candies[child - 1]:
                    candies[child] = candies[child - 1] + 1
                    flag = True

        return sum(candies)


if __name__ == "__main__":
    kids = Candy()
    print(kids.get_all_candies____([1, 2, 2]))
    print(kids.get_all_candies___([1, 2, 2]))
    print(kids.get_all_candies__([1, 2, 2]))
    print(kids.get_all_candies([1, 2, 2]))
    print(kids.get_all_candies([1, 2, 3, 4, 5, 3, 2, 1, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))