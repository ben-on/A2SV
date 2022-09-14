class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_idx = deque([i for i in range(len(senate)) if senate[i]=='R'])
        D_idx = deque([j for j in range(len(senate)) if senate[j]=='D'])
        n = len(senate)
        while R_idx and D_idx:
            r = R_idx.popleft()
            d = D_idx.popleft()
            if r < d:
                R_idx.append(n + r)
            else:
                D_idx.append(n + d)
        return 'Radiant' if R_idx else 'Dire'