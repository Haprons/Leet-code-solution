class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []

        # Precompute bit counts for hours and minutes
        hourBits = [bin(h).count('1') for h in range(12)]
        minuteBits = [bin(m).count('1') for m in range(60)]

        for h in range(12):
            for m in range(60):
                if hourBits[h] + minuteBits[m] == turnedOn:
                    times.append(f"{h}:{m:02d}")

        return times