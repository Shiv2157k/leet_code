from typing import List


class CombinationSum:

    def get_combinations(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        :param candidates:
        :param target:
        :return:
        """
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        combinations = []
        self.back_track(candidates, 0, target, [], combinations)
        return combinations

    def back_track(self, candidates, index, target, path, combinations):

        # base case
        if target == 0 and path not in combinations:
            combinations.append(path)
            return  # back track
        if target < 0 or index > len(candidates):
            return  # back track

        for candidate in range(index, len(candidates)):
            self.back_track(candidates,
                            candidate,
                            target - candidates[candidate],
                            path + [candidates[candidate]],
                            combinations
                            )

    def get_combinations_(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Dynamic Programming
        :param candidates:
        :param target:
        :return:
        """
        cache = {0: [[]]}

        for candidate in candidates:
            for tar in range(candidate, target + 1):
                if tar - candidate in cache:
                    if tar not in cache:
                        cache[tar] = []
                    for combination in cache[tar - candidate]:
                        cache[tar].append(combination + [candidate])
        return cache[target] if target in cache else []

    def get_unique_combinations(self, candidates: List[int], target: int) -> List[List[int]]:
        # validations
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        combinations = []
        self.back_track_unique(candidates, 0, target, [], combinations)
        return combinations

    def back_track_unique(self, candidates: List[int], index: int, target: int, path: List[int], combinations: List[List[int]]):
        # base case
        if target == 0 and path not in combinations:
            combinations.append(path)
            return  # back track
        if target < 0 or index >= len(candidates):
            return  # back track

        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            self.back_track_unique(candidates, i + 1, target - candidates[i], path + [candidates[i]], combinations)


if __name__ == "__main__":
    combination_sum = CombinationSum()
    print(combination_sum.get_combinations([2, 3, 6, 7], 7))
    print(combination_sum.get_combinations_([2, 3, 6, 7], 7))
    print(combination_sum.get_unique_combinations([10, 1, 2, 7, 6, 1, 5], 8))




