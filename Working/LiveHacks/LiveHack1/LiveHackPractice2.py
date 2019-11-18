money = int(input("How much money did you earn? :"))
average = int(input("What is your averge mark?:"))

if (money >= 500 and average >= 80):
    print("You will go to Europe")
elif (money < 500 and average >= 80):
    print("You will go to California")
else:
    print("You will stay home")
