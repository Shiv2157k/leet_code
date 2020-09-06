from typing import List


class Candy:

    def get_total_distributed_candies(self, ratings: List[int]) -> int:
        """
        Approach: Peak Valley with constant space
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param ratings:
        :return:
        """

        # base case
        childs = len(ratings)
        if childs <= 1:
            return childs
        result = 1
        up = down = peak = 0

        for i in range(1, childs):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                result += up + 1
            elif ratings[i] == ratings[i - 1]:
                up = down = peak = 0
                result += 1
            else:
                down += 1
                up = 0
                result += down + 1 + [0, -1][peak >= down]
        return result

    def get_total_distributed_candies_(self, ratings: List[int]) -> int:
        """
        Approach: Using single array.
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param ratings:
        :return:
        """
        # base case
        childs = len(ratings)
        if childs <= 1:
            return childs

        candies = [1] * childs
        for i in range(1, childs):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        total = candies[-1]
        for i in range(childs - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total += candies[i]
        return total


if __name__ == "__main__":
    candy = Candy()
    print(candy.get_total_distributed_candies([1, 0, 2]))
    print(candy.get_total_distributed_candies_([1, 0, 2]))
    print(candy.get_total_distributed_candies([1, 2, 3, 4, 5, 3, 2, 1, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))
    print(candy.get_total_distributed_candies_([1, 2, 3, 4, 5, 3, 2, 1, 6, 5, 4, 3, 3, 2, 1, 1, 3, 3, 3, 4, 2]))