class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # new=list(s)

        # for i in range(len(new)):

        #     for j in range(i+1,i+2):

        #         if new[i]==new[j]:

        #             temp = new[j]

        #             new[i-1]=new[j]

        #             new[i-j]=temp

        #             for letters in new:

        #                 string = "".join(letters)

        #             return string

        # return ""


        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1

        max_freq = max(freq)
        if max_freq > (len(s) + 1) // 2:
            return ""

        res = []
        while len(res) < len(s):
            maxIdx = freq.index(max(freq))
            char = chr(maxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] -= 1
            if freq[maxIdx] == 0:
                continue

            tmp = freq[maxIdx]
            freq[maxIdx] = float("-inf")
            nextMaxIdx = freq.index(max(freq))
            char = chr(nextMaxIdx + ord('a'))
            res.append(char)
            freq[maxIdx] = tmp
            freq[nextMaxIdx] -= 1

        return ''.join(res)