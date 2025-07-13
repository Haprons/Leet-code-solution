class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        res = 0
        for j in range(len(trainers)):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
                if i == len(players):
                    break
        return res