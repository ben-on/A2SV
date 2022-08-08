class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        d = defaultdict(int)
        
        mostVotePersons = [0] * len(persons)
        lv = -1 
        for i in range(len(persons)):
            d[persons[i]] += 1
            if lv == -1 or d[persons[i]] >= d[lv]:
                lv = persons[i]
            mostVotePersons[i] = lv
        
        self.times = times
        self.lead = mostVotePersons

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1 # binary search on times to find the most recent time before t
        return self.lead[idx]
    
# Your TopVotedCandidate object will be instantiated and called
# param_1 = obj.q(t) as such:
# obj = TopVotedCandidate(persons, times)