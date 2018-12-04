# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Sol(object):
    """docstring for ClassName"""
    def __init__(self, N):
        # super(ClassName, self).__init__()
        self.queue=[None]*N
        self.maxN=N
        self.ndx=0

    def record(self, order_id):
        print self.queue, self.ndx, order_id
        self.queue[self.ndx]=order_id
        self.ndx = (self.ndx+1)%self.maxN

    def get_last(self, i):
        print self.queue, self.ndx, i
        return self.queue[(self.ndx+self.maxN-i)%self.maxN]

if __name__ == '__main__':
    sol= Sol(5)
    for i in xrange(8):
        sol.record(i+100)
    for i in xrange(1,6):
        print sol.get_last(i)
