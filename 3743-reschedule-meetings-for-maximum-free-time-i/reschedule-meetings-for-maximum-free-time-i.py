class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        n, busy=len(startTime), 0
        for i in range(k):
            busy+=endTime[i]-startTime[i] 

        if n==k: return eventTime-busy

        ans=startTime[k]-busy

        l=0
        for r in range(k, n):
            busy+=(endTime[r]-startTime[r])-(endTime[l]-startTime[l])
            end=eventTime if r==n-1 else startTime[r+1]
            start=endTime[l]
            ans=max(ans, end-start-busy)
            l+=1
        return ans