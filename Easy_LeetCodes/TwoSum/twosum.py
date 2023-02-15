class Solution(object):
    def twoSum(self, nums, target):
        for index, value in enumerate(nums):
            for index2, value2 in enumerate(nums):
                if index != index2:
                    if value+value2 == target:
                        return [index, index2]