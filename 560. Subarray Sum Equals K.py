class Solution:
    def subarraySum(self, nums, k):
        answer = 0
        pre = 0
        df = defaultdict(int)
        df[0] = 1
        for i in nums:
            pre += i
            answer += df[pre - k]
            df[pre] += 1
        return answer
        # i=0
        # s=0
        # c=0
        # for j in range(len(nums)):
        #     s+=nums[j]
        #     while s > k:
        #         s-=nums[i]
        #         i+=1
        #     if s==k:
        #         c+=1
        # return c