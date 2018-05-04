
import random

player1 = raw_input("What is player 1 name!")
player2 = raw_input("What is player 2 name!")

begin = 1
end = 6
roll1 = (begin,end)
roll2 = (begin,end)
roll3 = (begin,end)
roll4 = (begin,end)
roll5 = (begin,end)
roll6 = (begin,end)
roll7 = (begin,end)
roll8 = (begin,end)

score1 = 0
score2 = 0
score3 = 0
score4 = 0
rollresult1 = roll1
rollresult2 = roll2
rollresult3 = roll3
rollresult4 = roll4
rollresult5 = roll5
rollresult6 = roll6
rollresult7 = roll7
rollresult8 = roll8

def roll(begin,end):
	return random.randint(begin,end)

def RoundWinner(rollresult1,rollresult2):
        if(rollresult1 > rollresult2):
                return (player1) + " wins this round!"
        elif(rollresult2 > rollresult1):
                return (player2) + " wins this Round!"
        else:
                return "Tie, now Re-roll"

def GameWinner(score1,score2):
        if(score1 > score2):
                return (player1) + " wins this game!"
        elif(score2 > score1):
                return (player2) + " wins this game!"
        else:
                return "No winner!"

gamerun = 3


while(gamerun >= 0):
	rollresult1 = roll(begin,end)
	rollresult2 = roll(begin,end)
	rollresult3 = roll(begin,end)
        rollresult4 = roll(begin,end)

	rollwin = RoundWinner(rollresult1,rollresult2)
	if(rollresult1 > rollresult2):
		score1 += 1
	elif(rollresult1 * rollresult2 < rollresult3 * rollresult4):
		score2 += 1
	gamerun -= 1
	print(rollresult1,rollresult2,rollwin)

gamewin = GameWinner(score1,score2)

print(gamewin)

