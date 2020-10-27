from typing import List


class CombinationSum:

    def back_track(self, candidates: List[int], index: int, target: int, path: List[int], result: List[List[int]]):
        """
        Method that does the back tracking.
        :param candidates:
        :param index:
        :param target:
        :param path:
        :param result:
        :return:
        """

        # base case 1:
        if target == 0 and path not in candidates:
            result.append(path)
            return  # back track
        if target < 0 or index >= len(candidates):
            return  # back track
        for idx in range(index, len(candidates)):
            if idx > index and candidates[idx] == candidates[idx - 1]:
                pass
            self.back_track(candidates, idx + 1, target - candidates[idx], path + [candidates[idx]], result)

    def get_all_unique_combinations(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        Time Complexity:
        Space Complexity:
        :param candidates:
        :param target:
        :return:
        """
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        results = []
        self.back_track(candidates, 0, target, [], results)
        return results


if __name__ == "__main__":
    combination = CombinationSum()
    print(combination.get_all_unique_combinations([10, 1, 2, 7, 6, 1, 5], 8))
    print(combination.get_all_unique_combinations([10, 1, 2, 7, 6, 1, 5], 1))
    print(combination.get_all_unique_combinations([10, 1, 2, 7, 6, 1, 5], 9))
    print(combination.get_all_unique_combinations([10, 7, 6, 5], 4))


