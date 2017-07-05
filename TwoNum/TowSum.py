class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            first = nums[i]
            scend = target - first
            if scend in nums:
                for j in range(0, len(nums)):
                    if nums[j] == scend and i != j:
                        return [i, j]
