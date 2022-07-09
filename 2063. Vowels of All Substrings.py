class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = list(map(lambda x: int(x in 'aeiou'), word))
        acc = list(accumulate(vowels, initial=0))
        acc2 = list(accumulate(acc))
        answer = 0
        for i in range(n+1):
            answer += acc2[-1] - acc2[i]
            if i > 0:
                answer -= (acc[i-1]) * (len(acc2) - i)
        return answer