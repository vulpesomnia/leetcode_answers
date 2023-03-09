class Solution(object):#https://leetcode.com/problems/running-sum-of-1d-array/
    def runningSum(self, nums):
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[:i+1]))
        return output