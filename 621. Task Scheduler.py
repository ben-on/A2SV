class Solution:
    	def leastInterval(self, tasks: List[str], n: int) -> int:
		count = Counter(tasks)
		pq = [-cnt for cnt in count.values()]
		heapify(pq)
		q = deque()
		time = 0
		while q or pq:
			if q and q[0][1] == time:
				cnt, _ = q.popleft()
				heappush(pq, cnt)
			if pq:
				cnt = heappop(pq)
				next_avail = time+n+1
				#decrement count
				cnt+=1
				if cnt: q.append((cnt,next_avail))
				time+=1
			elif q:
				time = q[0][1]

		return time