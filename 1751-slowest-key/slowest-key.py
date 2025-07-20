class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        pressTime = releaseTimes[0]
        key = keysPressed[0]
        n = len(releaseTimes)
        for i in range(n - 1):
            time = releaseTimes[i+1] - releaseTimes[i]
            if time > pressTime:
                pressTime = time
                key = keysPressed[i+1]
            elif time == pressTime:
                key = chr(max(ord(key),ord(keysPressed[i+1])))
        return key