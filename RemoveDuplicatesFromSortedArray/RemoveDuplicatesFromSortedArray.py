class RemoveDuplicatesFromSortedArray(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0

        count = 1
        current = nums[0]
        for item in nums:
            if item != current:
                current = item
                nums[count] = current
                count += 1

        return count




