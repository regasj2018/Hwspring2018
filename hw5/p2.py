currentNumber = float(input("Give me an integer number: "))
if(currentNumber % 2.0) == 0.0:
	evennumber = currentNumber * 3 + 1
	print(evennumber)
else:
	oddnumber = currentNumber // 2
	print(oddnumber)
