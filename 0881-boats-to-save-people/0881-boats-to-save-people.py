class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        temp=boats=0
        l,r=0,len(people)-1
        while people[r]==limit:
            boats+=1
            r-=1
        while l<=r:
            if people[l]+people[r]<=limit:
                boats+=1
                l+=1
                r-=1
            else:
                r-=1
                boats+=1

        return boats