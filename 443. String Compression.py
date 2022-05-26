class Solution:
    def compress(self, chars: List[str]) -> int:
        s,i,j="",0,0
        while i < len(chars) :
            if s and chars[i] == s[-1] :
                j+=1
                i+=1
            else :
                if j > 1 :
                    s+=str(j)
                s+=chars[i]
                j=1
                i+=1
        if j > 1 :
            s+=str(j)
        for j in range(len(chars)-len(s)) :
            chars.pop()
        for k in range(len(chars)) :
            chars[k]=s[k]
        return len(chars)


