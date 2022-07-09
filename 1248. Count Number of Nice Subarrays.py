class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):

            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        currsum = 0
        subarray = 0
        hashmap = {}

        for num in nums:
            currsum += num

            if currsum == k:
                subarray += 1

            if currsum - k in hashmap:
                subarray += hashmap[currsum - k]

            if currsum in hashmap:
                hashmap[currsum] += 1

            else:
                hashmap[currsum] = 1

        return subarray