class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        # klist=[]

        # res={}

        # for number in nums:

        #     if number in res:

        #         res[number]+=1  #mistake: res[number]=count+1 (made no sense)
            
        #     else:
        #         res[number]=1  #mistake:res[number]=1 was outside else block
        
        # new=list(sorted(res.values()))  #mistake: List,sort((res.values()))

        # n=len(new)

        # for i in range(n-1,n-1-k,-1): #mistake: (n-1,k)

        #     target_value=new[i]

        #     for key,val in res.items():
        #         if val==target_value:
        #             klist.append((key)) # mistake :- {key}
        #             del res[key]  # Prevents re-matching this key on duplicate values
        #             break         # Breaks inner loop after picking ONE matching key for target_value

        # return klist


        # klist=[]

        # res={}

        # for number in nums:

        #     if number in res:

        #         res[number]+=1  #mistake: res[number]=count+1 (made no sense)
            
        #     else:
        #         res[number]=1  #mistake:res[number]=1 was outside else block
        
        # new=list(sorted(res.values()))  #mistake: List,sort((res.values()))

        # n=len(new)

        # # Get the threshold frequency of the kth most frequent element
        # threshold = new[n-k]

        # for key, val in res.items():
        #     if val >= threshold:
        #         klist.append(key)

        # return klist[:k]



        # klist=[]

        # res=defaultdict(int)

        # for number in nums:

        #         res[number]+=1  #mistake: res[number]=count+1 (made no sense)
        
        # new=list(sorted(res.values()))  #mistake: List,sort((res.values()))

        # n=len(new)

        # # Get the threshold frequency of the kth most frequent element
        # threshold = new[n-k]

        # for key, val in res.items():
        #     if val >= threshold:
        #         klist.append(key)

        # return klist[:k]


        count ={}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:

            count[num] = 1+count.get(num,0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(len(freq)-1,0,-1):

            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res 