
class MySolution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        rotations = 0
        minValue = nums[0]
        while (l < r):
            m = (l + r)//2
            if nums[m] < nums[l]:
                rotations += 1 
                minValue = min(nums[m], minValue)
                l += 1
            elif nums[m] > nums[r]:
                rotations += 1
                minValue = min(nums[r], minValue)
                r -= 1
            else:
                l += 1
        return min(minValue,nums[rotations])