class SearchInsertPosition(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        is_search = False
        for i in range(0, length):
            if target < nums[i] and not is_search:
                index = i
                is_search = True
            elif target == nums[i]:
                return i
        if length <= 0 or (length > 0 and nums[0] > target):
            return 0
        elif length > 0 and nums[length - 1] < target:
            return length 
        else:
            return index

