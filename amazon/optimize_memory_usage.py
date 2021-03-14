from typing import List


class Memory:

    def optimize_memory_usage(self, k: int, foreground_tasks: List[int], background_tasks: List[int]) -> List[List[int]]:

        if k == 0 or (not len(foreground_tasks) and not len(background_tasks)):
            return [[-1, -1]]

        bg_list, fg_list = [], []

        for i in range(len(foreground_tasks)):
            fg_list.append()
