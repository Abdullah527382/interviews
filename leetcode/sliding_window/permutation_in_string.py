class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # We solve this question through having 2 string count arrays where we keep track of the matches count 
        # The string count arrays will have values -> ASCII counts (ord(c) - ord("a"))
        # if matches == 26 we return True
        # A sliding window from start of s1 till s2 will updates matches and s1Count, s2count arrays

        if (len(s1) > len(s2)):
            return False

        s1count, s2count = [0] * 26, [0] * 26
        matches = 0

        # Initialize our s1count,s2count based on s1
        # e.g s1 = abc, s2 = deabc
        for s in range(len(s1)): 
            s1count[ord(s1[s]) - ord("a")] += 1
            s2count[ord(s2[s]) - ord("a")] += 1

        # Initialize matches based on whether string counts are equal at the indexes
        for c in range(26):
            if (s1count[c] == s2count[c]):
                matches += 1
        
        # Sliding window to check whether s1 exists in s2 as a permutation
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            # Add new r value to s2count and check whether it exists in s1count
            index = ord(s2[r]) - ord("a")
            s2count[index] += 1
            if s2count[index] == s1count[index]:
                matches += 1
            elif s2count[index] == s1count[index] + 1:
                matches -= 1
            
            # remove new l char value in s2count and check whether it exists in s1count
            index = ord(s2[l]) -  ord("a")
            s2count[index] -= 1
            if s2count[index] == s1count[index]:
                matches += 1
            elif s2count[index] == s1count[index] - 1:
                matches -= 1
            l += 1
        return matches == 26