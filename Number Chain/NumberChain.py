# Initial variable to track game play
Play = 'y'
Start = 0
while Play == 'y':
    Number = int(input("How Many Numbers?: "))
    for x in range(Start, Start+Number):
        print(x)
    Start = Start + Number
    Play = input("Would You Like to Play Again?: ")
    if Play != 'y':
        print("Thank You for Playing.")
 
    

    