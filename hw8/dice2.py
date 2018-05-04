import random

def dicesum():

        return random.randint(1,6)

def winner(firstplayer,secondplayer):

        if firstplayer > secondplayer or (d1 == d2 == d3 == d4):

                return fpname + " win the round."

        elif secondplayer > firstplayer or (d5 == d6 == d7 == d8):

                return spname + " win the round."

        else:

		if tiefirst > tiesecond:

			return fpname + " win the round."

		elif tiesecond > tiefirst:

			return spname + " win the round."

		else:

			return (winner)

def finalwinner(fpwin,spwin):

        if fpwin > spwin:

                return fpname + " win the game."

        elif spwin > fpwin:

                return spname + " win the game."

        else:

                return (game)

fpname = raw_input ("what is your name?")

spname = raw_input ("what is your name?")

round = 3

fpwin = 0

spwin = 0

while (round >= 0):

	d1= dicesum()
	d2= dicesum()
	d3= dicesum()
	d4= dicesum()
	d5= dicesum()
	d6= dicesum()
	d7= dicesum()
	d8= dicesum()
	d9= dicesum()
	d10= dicesum()

	firstplayer = d1 * d2 * d3 * d4

        secondplayer = d5 * d6 * d7 * d8

	tiefirst = d9

	tiesecond = d10

        game = winner(firstplayer,secondplayer)

        if (firstplayer > secondplayer):

                fpwin += 1

        elif (secondplayer > firstplayer):

                spwin += 1

        round -= 1
        print (firstplayer,secondplayer,game)

gamewin = finalwinner(fpwin,spwin)

print (gamewin)

#new Changes
#uses 4 die per person,
#biggest number wins,
#if all 4 numbers are same they win,
#if they tie they each roll one die till winner,




