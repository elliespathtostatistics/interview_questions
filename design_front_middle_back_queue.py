class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A = []
        

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.A.insert(0, val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        index = len(self.A)//2       **
        self.A.insert(index, val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        index = len(self.A)
        self.A.insert(index, val) **
        
        

    def popFront(self):
        """
        :rtype: int
        """
        return (self.A or [-1]).pop(0)
        

    def popMiddle(self):
        """
        :rtype: int
        """
        index = len(self.A)//2 - 1 ******* this is your mistake, subtract 1 and then divide
        return (self.A or [-1]).pop(index)
        

    def popBack(self):
        """
        :rtype: int
        """
        return (self.A or [-1]).pop()
        
