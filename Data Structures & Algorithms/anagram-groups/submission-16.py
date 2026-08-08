class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#FAILED
        # new=[]
        

        # for i in range(len(strs)):

        #     sub=[]

        #     sub.append(strs[i])

        #     for j in range(i+1,len(strs)):

        #         for strings in strs:
        #             for letters in strings:
        #                 if len(strs[i])==len(strs[j]) and
        # strs[i].count(letters)==strs[j].count(letters):

                            #  sub.append(strs[j])

                            # new.append(sub)

        #  return new


    #     new = []
    #     visited = set()  # Keeps track of indices already grouped

    #     for i in range(len(strs)):
    #         if i in visited:
    #             continue  # Skip if strs[i] was already put in a group

    #         sub = []
    #         sub.append(strs[i])
    #         visited.add(i)

    #   # 1. Start j at i + 1 to only check future strings
    #         for j in range(i + 1, len(strs)):
    #             if j in visited:
    #                 continue

    #             if len(strs[i]) == len(strs[j]):
    #                 is_match = True

    #       # 2. Only check the letters of strs[i]
    #                 for letter in set(strs[i]):
    #         # 3. If ANY letter count doesn't match, it's not an anagram
    #                     if strs[i].count(letter) != strs[j].count(letter):
    #                         is_match = False
    #                         break

    #       # If ALL letter counts matched, append strs[j]
    #                 if is_match:
    #                     sub.append(strs[j])
    #                     visited.add(j)

    #   # 4. Append the complete group AFTER finishing the j loop
    #         new.append(sub)

    #     return new 



        # res={}

        # for string in strs:

        #     sortedS="".join(sorted(string))

        #     if sortedS not in res:

        #         res[sortedS]=[]

        #     res[sortedS].append(string)

        # return list(res.values())


        # res=defaultdict(list)

        # for string in strs:

        #     sortedS="".join(sorted(string))

        #     res[sortedS].append(string)

        # return list(res.values())


        res=defaultdict(list)

        for string in strs :

            count=[0]*26

            for c in string:

                count[ord(c)-ord('a')]+=1

            res[tuple(count)].append(string)
        
        return list(res.values())

            
                

        













            




            






        