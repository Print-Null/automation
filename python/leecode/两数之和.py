"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        index_list = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i not in index_list:
                        index_list.append(i)
                    if j not in index_list:
                        index_list.append(j)
        return index_list


solution = Solution()
print(solution.two_sum([2, 4, 5, 7, 11, 15], 9))
print(solution.two_sum([3, 3, 3, 3], 6))
