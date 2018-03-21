import csv
with open('roster.csv' , 'rb')as gpa:
	reader = csv.reader(gpa)
	for row in reader:
		print row

