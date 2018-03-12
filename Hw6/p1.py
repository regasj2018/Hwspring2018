type = raw_input("If you would like to enter an entire game enter 1, if you would like to enter in a game every turn enter in 2")

if(type == "1"):
	score = map(int, raw_input("Enter your score frame by frame seperated by a comma").split(","))
	print(str(sum(score)))
if(type == "2"):
	frame = 0
	frame = frame + 1
        while(frame < 11):
                print("entering row " + str(frame))
                score = raw_input("Enter the total pins knocked down.")


