class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        first = sum(int(c) for c in num[:n//2] if c != "?")
        second = sum(int(c) for c in num[n//2:] if c != "?")
        first_turns = num[:n//2].count("?")
        second_turns = num[n//2:].count("?")
        
        c = min(first_turns, second_turns)
        first_turns -= c
        second_turns -= c

        if first_turns and first > second:
            return True
        if second_turns and second > first:
            return True
        turns = first_turns + second_turns
        if turns % 2 == 1:
            return True
        return 9 * turns// 2 != abs(second-first)