from typing import List


class CombinationSum:

    def back_track(self, candidates: List[int], index: int, target: int, path: List[int], result: List[List[int]]):
        """
        Method for back tracking.
        :param candidates:
        :param index:
        :param target:
        :param path:
        :param result:
        :return:
        """
        # base case 1
        if target == 0 and path not in result:
            result.append(path)
            return  # back track
        # base case 2
        if target < 0 or index >= len(candidates):
            return  # back track

        for idx in range(index, len(candidates)):
            self.back_track(candidates, idx, target - candidates[idx], path + [candidates[idx]], result)

    def get_all(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back tracking.
        N - number of candidates.
        T - target value.
        M - minimal value among the candidates.
        Time Complexity: O (N ^ (T / M + 1))
        Space Complexity: O(T / M)
        :param candidates:
        :param target:
        :return:
        """
        # validation
        if not candidates or min(candidates) > target:
            return []

        result = []
        self.back_track(candidates, 0, target, [], result)
        return result


if __name__ == "__main__":
    combinations = CombinationSum()
    print(combinations.get_all([2, 3, 5], 8))