print("Welcome To The Quiz!!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
cnt = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    cnt += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    cnt += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    cnt += 1
else:
    print("Incorrect!")

answer = input("Last, What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    cnt += 1
else:
    print("Incorrect!")
print("You have got "+str(cnt)+"/4")
