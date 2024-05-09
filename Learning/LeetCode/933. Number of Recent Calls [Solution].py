"""
    Better because it uses deque which has an 0(1) to pop and append to the queue
"""

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the current request timestamp
        self.requests.append(t)
        # Remove requests that fall out of the 3000 ms window
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        # Return the number of requests within the 3000 ms window
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)