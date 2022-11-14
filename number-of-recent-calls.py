from collections import deque
import bisect

class RecentCounter:

    def __init__(self):
        self.calls = deque([])

    def ping(self, t: int) -> int:
        index = bisect.bisect_left(self.calls, t)
        self.calls.insert(index, t)
        
        return index - bisect.bisect_left(self.calls, t - 3000) + 1
        
recentCounter = RecentCounter()
assert recentCounter.ping(1) == 1
assert recentCounter.ping(100) == 2
assert recentCounter.ping(3001) == 3
assert recentCounter.ping(3002) == 3