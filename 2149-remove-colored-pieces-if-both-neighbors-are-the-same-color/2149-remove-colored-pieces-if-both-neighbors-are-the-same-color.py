class Solution(object):
    def winnerOfGame(self, colors):
        alice_wins = 0
        bob_wins = 0
        i = 0

        while i < len(colors):
            if colors[i] == 'A':
                count_A = 0
                while i < len(colors) and colors[i] == 'A':
                    count_A += 1
                    i += 1
                alice_wins += max(0, count_A - 2)
            elif colors[i] == 'B':
                count_B = 0
                while i < len(colors) and colors[i] == 'B':
                    count_B += 1
                    i += 1
                bob_wins += max(0, count_B - 2)

        return alice_wins > bob_wins
