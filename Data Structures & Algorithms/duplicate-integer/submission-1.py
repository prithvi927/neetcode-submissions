class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


# brute force:
        # count=0
 
        # for i in range(len(nums)):

        #     for j in range(i+1,len(nums)):

        #         if nums[i]==nums[j]:

        #             count=count+1

        # if count>0:

        #     return True
        # else:

        #     return False



#optimal approach

        seen=set()

        for num in nums:

            if num in seen:

                return True
            
            seen.add(num)

        return False

        

