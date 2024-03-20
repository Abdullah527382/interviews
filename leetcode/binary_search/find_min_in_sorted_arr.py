
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

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: i
        """
        # The main difference between yours and the solution is the l, r updates when searching
        # They should be l = m + 1 and r = m - 1
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while (l <= r):
            if (nums[l] < nums[r]): #Its already sorted
                res = min(nums[l], res)
                break

            m = (l + r)//2

            if nums[l] >= nums[m]:
                # Search the right
                l = m + 1
            else:
                r = m - 1
            res = min(res, nums[m])
        return res