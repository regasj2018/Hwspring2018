

name = ('James')
print("name")
weather = ('Hot')
print("weather")
springbreak = ('I cant wait to leave today.')
print("springbreak"
goodbye = 'Goodbye'
print("bye"

list = []
list.append(name)
list.append(weather)
list.append(springbreak)
list.append(goodbye)

def integers(list):
	s = 0
	while(s<4):
		split = list[s]
		spliting = split.split()
		s = s + 1
		print (spliting)
	return(list)
