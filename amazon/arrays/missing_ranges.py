from typing import List


class Ranges:

    def get_missing_range(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        Approach: Linear Scan
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param nums:
        :param lower:
        :param upper:
        :return:
        """

        def format_range(lower: int, upper: int) -> str:
            if lower == upper:
                return str(lower)
            return "{lower}->{upper}".format(lower=str(lower), upper=str(upper))

        prev = lower - 1
        length = len(nums)
        missing_ranges = []
        for idx in range(length + 1):
            curr = nums[idx] if idx < length else upper + 1
            if prev + 1 <= curr - 1:
                missing_ranges.append(format_range(prev + 1, curr - 1))
            prev = curr
        return missing_ranges


if __name__ == "__main__":
    ranges = Ranges()
    print(ranges.get_missing_range(
        nums=[0, 1, 3, 50, 75], lower=0, upper=99
    ))
    print(ranges.get_missing_range(
        nums=[], lower=1, upper=1
    ))
    print(ranges.get_missing_range(
        nums=[-1], lower=-3, upper=-1
    ))
    print(ranges.get_missing_range(
        nums=[-1], lower=-2, upper=-1
    ))
