class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # only 3/27 test cases passed
        # for letter in s:

        #     if letter not in t:

        #         return False

        # return True

        if len(s) != len(t):
            return False

        s_new = set(s)

        t_new = set(t)

        for letter in s_new:

            if s.count(letter) != t.count(letter):

                return False

        return True