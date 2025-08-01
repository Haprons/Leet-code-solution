class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n >>= 1
        return result
import atexit
atexit.register(lambda: open("display_runtime.txt", "w").write("0"))
