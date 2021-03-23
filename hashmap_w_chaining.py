
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000;
        self.buckets = [None] * self.size

    def put(self, key, value):
        '''
        Two scendarios:
        1. there's no collission and a new key starts a new chain
        2. there's a collision and

        :param key:
        :param value:
        :return:
        '''
        index = key % self.size
        #first scneario
        if self.buckets[index] == None:
            self.buckets[index] = ListNode(key, value)
        #second scenario, the bucket was taken at one point, so we begin chaining
        else:
            cur = self.buckets[index]
            while True:
                #this is when a key value pair udpates an older one
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                # this is the scenario where we've reached the end of the list so this is where you put the new list node
                if cur.next == None: break
                cur = cur.next

            #here you update the next value in the chain after you are at the end
            cur.next = ListNode(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size
        cur = self.buckets[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        index = key % self.size
        cur = prev = self.buckets[index]
        #not found just return
        if not cur: return
        #two scendarios, if it's the first element of the chain, then we update bucket index, if it's in the middle then we do
        #a two step process where we find it first, then update previous' pointer to cur.next
        if cur.pair[0] == key:
            self.buckets[index] = cur.next
        else:
            #going down the buckets
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    #breaks out of while statement
                    break
                else:
                    cur, prev = cur.next, prev.next

# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1000,6)
print(obj.get(1000))
# param_2 = obj.get(key)
# obj.remove(key)
