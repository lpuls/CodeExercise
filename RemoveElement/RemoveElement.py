class RemoveElement(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        while index < len(nums):
            value = nums[index]
            if value == val:
                del nums[index]
            else:
                index += 1
        return index;



