class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # only 3/27 test cases passed
        # for letter in s:

        #     if letter not in t:

        #         return False

        # return True


# passes all test cases but  time complexity is O(n^2) which is worse time , space complexity is alsredy in optimal state , so we need to make time complexity optimal
        # if len(s) != len(t):
        #     return False

        # s_new = set(s)

        # t_new = set(t)

        # for letter in s_new:

        #     if s.count(letter) != t.count(letter):

        #         return False

        # return 
    
#TIME COMPLEXITY IMPROVEMENT 1: Time complexity = nlogn, python sorting uses timsort

        # if len(s)!=len(t):

        #     return False

        # return sorted(s)==sorted(t)


# TIME COMPLEXITY IMPROVEMENT 2:

        if len(s)!=len(t):

            return False

        s_count={}

        t_count={}

        for letter in s:

            s_count[letter] = 1+s_count.get(letter,0)

        for letter in t:

            t_count[letter]=1+t_count.get(letter,0)


        return s_count==t_count









    
