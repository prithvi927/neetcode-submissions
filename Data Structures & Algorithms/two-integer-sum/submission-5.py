class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


# This is the brute force approach , time complexity is O(n^2) and space complexity is O(1), we need to optomize time complexity more 
        # for i in range(len(nums)):

        #     for j in range(1,len(nums)):

        #         if nums[i]+nums[j]==target and i!=j:

        #             return [i,j]


    # IN THIS APPROACH WE MADE TIME COMPLEXITY REACH TO O(nlogn) 
        # A=[]

        # for i,num in enumerate(nums):

        #     A.append([num,i])

        # A.sort()

        # i,j=0,len(nums)-1

        # while i<j:

        #     curr=A[i][0]+A[j][0]

        #     if curr==target:

        #         return [min(A[i][1],A[j][1]),
        #                 max(A[i][1],A[j][1])]

        #     elif curr<target:

        #         i=i+1

        #     else:

        #         j=j-1


    # we achieved time complexity as O(n) but we can optimize this further

        # indices={}

        # for i,n in enumerate(nums):

        #     indices[n]=i

        # for i,n in enumerate(nums):

        #     diff=target-n

        #     if diff in indices and indices[diff]!=i:

        #         return [i,indices[diff]]


# more optimzed : by using hash map single pass

        indices={}

        for i,n in enumerate(nums):

            diff=target-n

            if diff in indices:

                return [indices[diff],i]
            
            else:
                indices[n]=i

           
        





    
        

