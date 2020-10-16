"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:
输入: [1,2,3]
输出: 6

示例 2:
输入: [1,2,3,4]
输出: 24

注意:
给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""


class Solution:
    def maximumProduct(self, nums: list) -> int:
        nums.sort()
        count = 0
        for i in nums:
            if i < 0:
                count += 1
            else:
                break
        if count % 2 == 0:
            nums_new = []
            for i in range(0, len(nums)):
                if nums[i] < 0:
                    nums[i] = abs(nums[i])
                    if abs(nums[i]) not in nums:
                        nums_new.append(abs(nums[i]))
                    else:
                        continue
            nums.sort()
            return nums[-1] * nums[-2] * nums[-3]
        else:
            return nums[-1] * nums[-2] * nums[-3]


solution = Solution()
print(solution.maximumProduct([1, 2, 3]))
print(solution.maximumProduct([-1, -2, 1, 2, 3]))
