import random

begin = 1
end = 6
roll1 = (begin,end)
roll2 = (begin,end)
score1 = 0
score2 = 0
rollresult1 = roll1
rollresult2 = roll2

def roll(begin,end):
	return random.randint(begin,end)

def RoundWinner(rollresult1,rollresult2):
	if(rollresult1 > rollresult2):
		return "Player 1 wins this round!"
	elif(rollresult2 > rollresult1):
		return "Player 2 Wins the Round!"
	else:
		return "Tie, now Re-roll"

def GameWinner(score1,score2):
	if(score1 > score2):
		return "Player 1 wins the game!"
	elif(score2 > score1):
		return "Player 2 wins the game!"
	else:
		return "No winner!"

gamerun = 3

while(gamerun >= 0):
	rollresult1 = roll(begin,end)
	rollresult2 = roll(begin,end)
	rollwin = RoundWinner(rollresult1,rollresult2)
	if(rollresult1 > rollresult2):
		score1 += 1
	elif(rollresult2 > rollresult1):
		score2 += 1
	gamerun -= 1
	print(rollresult1,rollresult2,rollwin)

gamewin = GameWinner(score1,score2)

print(gamewin)
