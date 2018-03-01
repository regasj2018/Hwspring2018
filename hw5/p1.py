temp = float(raw_input("enter the tempreture on your thermometer"))

if(temp > 96.0):
        response = raw_input ("Are you warm?")
        if(response == "yes"):
                response = raw_input ("Try dressing up for the winter to keepyour tempreture up")
                if(response == "no"):
                        print("Hmph, you must be cold blooded")
else:
                        print("close to normal, you may want to try again later")

if(temp < 99.0):
        response = raw_input ("do you feel cold?")
        if(response == "yes"):
                response = raw_input("you may be running a fever")
        if(response == "no"):
                print("you must be warm blooded")
else:
                print("close to normal, you may want to try again later")


if(temp == 98.6):
        print("congratulations, you are normal and healthy")
else:
        print("close to normal, you may want to try again later")

