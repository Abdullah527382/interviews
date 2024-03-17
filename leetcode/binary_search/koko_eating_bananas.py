class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        # [3,6,7,11] h = 8
        # The min value: 1 will give k = 27 but thats > 8
        # The max value: 11 will give k = 4 and thats < 8 but we should try to match for k = 8
        # We can brute force by just solving from l = 1 .. 11 and do k+=piles[i]//l and check if < or >
        # But instead lets just use binary to check our k value
        l = 1
        r = max(piles)
        res = r
        while (l <= r):
            k = (l + r)//2
            pileSum = 0
            for pile in piles:
                pileSum += math.ceil(float(pile)/k) 
            if pileSum > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        return res

# This has O(log(max(p))) where p is the input array