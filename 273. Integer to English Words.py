class Solution:
    def numberToWords(self, num: int) -> str:
        return("Zero" if num == 0 else ' '.join(filter(None,self.helper(num))))
    def __init__(self):
        self.under20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
                 "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen",
                 "Eighteen","Nineteen"]
        self.tens=["","Ten","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.places=["Hundred","Thousand","Million","Billion"]

    # def numberToWords(self, num: int) -> str:
    #     return("Zero" if num == 0 else ' '.join(filter(None,self.helper(num))))

    def helper(self,num):
        if num < 20:
            return [self.under20[num]]
        elif num < 100:
            return [self.tens[num//10]]+self.helper(num%10)
        elif num < 1000:
            return self.helper(num//100)+[self.places[0]]+self.helper(num%100)
        elif num < 1000000: #thousands
            return self.helper(num//1000)+[self.places[1]]+self.helper(num%1000)
        elif num < 1000000000: #millions
            return self.helper(num//1000000)+[self.places[2]]+self.helper(num%1000000)     
        else: #billions
            return self.helper(num//1000000000)+[self.places[3]]+self.helper(num%1000000000) 
    