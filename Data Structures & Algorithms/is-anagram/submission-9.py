class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # only 3/27 test cases passed
        # for letter in s:

        #     if letter not in t:

        #         return False

        # return True


# passes all test cases but  time complexity is O(n^2) which is worse time , space complexity is alsredy in optimal state , so we need to make time complexity optimal
        if len(s) != len(t):
            return False

        for letter in s:

            if s.count(letter) != t.count(letter):

                return False

        return True 
    
#TIME COMPLEXITY IMPROVEMENT 1: Time complexity = nlogn, python sorting uses timsort

        # if len(s)!=len(t):

        #     return False

        # return sorted(s)==sorted(t)


# TIME COMPLEXITY IMPROVEMENT 2:

        # if len(s)!=len(t):

        #     return False

        # s_count={}

        # t_count={}

        # for letter in s:

        #     s_count[letter] = 1+s_count.get(letter,0)

        # for letter in t:

        #     t_count[letter]=1+t_count.get(letter,0)


        # return s_count==t_count


#   WHAT IS s_count[letter] = 1+s_count.get(letter,0)??

# This line is a clever Python trick to safely increment the character count in a dictionary (hash map) without getting a `KeyError`.

# Here is the step-by-step breakdown of how it works:

#"letter" is key here, and "s_count" is the dictionary name , so as we know a dict conatians a key and value of the key

# by doing "s_count[letter] =...." the we are assigning the value of the key "letter" in dict "s_count" as "....."

# now this "...." is "1+s_count.get(letter,0)" this, that is we assigned the value of the key  "letter" in dict "s_count" as "1+s_count.get(letter,0)"

# whats "1+s_count.get(letter,0)" ? this is code that actually counts the freqency (quantity) of each letter in string s.

# how ? s_count.get(letter,0) -> .get checks the "letter" key in s_count dict , if it doesnt fin the key there (which is ofc it wont find it for the first time cuz our dictionary is empty), it returns 0 (this is the fallback value we assigned if key is not found in s_count)
# then 1 is added . why ? cuz everytime we get a letter in sting "s" we hv to increase its count in value of key "letter", as the value of the key "letter" in s_count dict represents the frequency of letter in string s

# for eg. s=aab

# 1st iteration :- letter = a , 
# s_count.get(a,0)-> ".get" finds key "a" in s_count dict,  
# s_count[a] found in  s_count dict ? ans- NO, cuz s_count is empty initially emoty, 
#so 0 (fallback) avlue returned, so  s_count[a]=1+0 -> s_count[a]=1 so s_count={a:1} where a is letter found in string "s" and 1 is letter a's frequency








    
