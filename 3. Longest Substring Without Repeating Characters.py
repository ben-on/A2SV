class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=mx=0
        d={}
        for j in range(len(s)):
            # print(d)
            if s[j] in d:
                while s[i]!=s[j]:
                    del d[s[i]]
                    i+=1
                i+=1
            else:
                d[s[j]]=j
            mx=max(mx,len(d))
        return mx
