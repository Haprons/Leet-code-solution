class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remain = n
        step = 1
        head = 1
        while remain > 1:
            if left or (remain % 2 == 1):
                head += step
            remain //= 2
            step *= 2
            left = not left
        return head