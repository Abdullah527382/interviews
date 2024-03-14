class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if (i > 0 and nums[i - 1] == a):
                continue
            l, r = i + 1, len(nums) - 1
            while (l < r):
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l - 1] == nums[l]):
                        l += 1
        return res