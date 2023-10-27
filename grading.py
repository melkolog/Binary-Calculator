midtermScore = int(input("Enter Your Midterm Grade: "))
didAllLabs = input("Attended all classes? Y/N: ")

if didAllLabs == "Y":
    didAllLabs = True
else:
    didAllLabs = False

if midtermScore > 59 and didAllLabs == True:
    print("Can take final!")
else:
    print("Cannot take final!")