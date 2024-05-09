"""
    Passes
"""

class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.queue = []

    def ping(self, t: int) -> int:
        # print("new ping time:", t)
        # print(" current queue is:", self.queue)

        if len(self.queue) > 0:

            first = self.peek()

            while t - first > 3000 and len(self.queue) > 0:
                # print(" removing time", first)
                self.queue.pop(0)
                if len(self.queue) > 0:
                    first = self.peek()
                else:
                    first = 0
            self.queue.append(t)
        else:
            self.queue.append(t)
        # print(" updated queue is:", self.queue)

        return len(self.queue)

    def peek(self):
        return self.queue[0]

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)