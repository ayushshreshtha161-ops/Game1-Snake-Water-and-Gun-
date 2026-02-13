#Snake Water Gun Game
'''
1 for snake
-1 for snake
0 for gun
'''
import random
computer = random.choice([1, -1, 0])
youstr = input('Enter your choice: ')
youDict ={'s': 1,'w': -1,'g': 0}
you = youDict[youstr]

if(computer == you):
    print("draw")
else:
    if(computer == -1 and you == 1):
        print ('you win!!')
    elif(computer == -1 and you == 0):
        print ('you lose!!')
    elif(computer == 1 and you == -1):
        print ('you lose!!')
    elif(computer == 1 and you == 0):
        print ('you win!!')
    elif(computer == 0 and you == -1):
        print ('you lose!!')

    else:
        print("something is worng")