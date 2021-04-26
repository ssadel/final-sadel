
def image():
    root = Tk()      
    canvas = Canvas(root, width = 600, height = 600)      
    canvas.pack()      
    img = PhotoImage(file="/Users/sidneysadel/Downloads/final proj/gui/roulette2.png")
    canvas.create_image(20,20, anchor=NW, image=img)
    exit_button = Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=20)
    root.mainloop()#geeksforgeeks.org tkinter tutorials

def oddsMethod(bet):
    isInt=False
    isInRange=False
    isString=False
    a=0
    d={
        'red':2,
        'black':2,
        'even':2,
        'odd':2,
        'low':2,
        'high':2,
        'row1':3,
        'row2':3,
        'row3':3,
        'fst12':3,
        'snd12':3,
        'trd12':3,
        }
    try:
        bet=int(bet)
    except:
        isString=True
    else:
        isInt=True

    if (isInt==True) and (0<=bet<=36):
        isInRange=True
    elif (isInt==True) and (bet<0 or bet>36):
        isInRange=False
    

    odds=0
    if (isInt==True) and (isInRange==True):
        odds=36
    elif (isInt==True) and (isInRange==False):
        print('Invalid bet; int out of range')
        a+=1
        odds2=oddsMethod(input('Enter an int in range [0-32]: '))
    elif (isString==True):
        odds=d.get(bet)
    

    if a>0:
        return odds2, bet
    else:
        return odds, bet

def isAmountInt(n):
    a=0
    try:
        n=int(n)
    except:
        print('Invalid entry, not an integer')
        a+=1
        n2=isAmountInt(input('Enter an integer for bet amount: '))

    if a>0:
        return n2
    else:
        return n

def spin(bet):
    spin=r.randint(0, 36)
    win=False
    
    red=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    fst12=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    snd12=[13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    trd12=[25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    row1=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    row2=[2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    row3=[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]

    if (spin in red) and (bet=='red'):
        win=True
    elif (spin in black) and (bet=='black'):
        win=True
    elif (spin in fst12) and (bet=='fst12'):
        win=True
    elif (spin in snd12) and (bet=='snd12'):
        win=True
    elif (spin in trd12) and (bet=='trd12'):
        win=True
    elif (spin in row1) and (bet=='fstRow'):
        win=True
    elif (spin in row2) and (bet=='sndRow'):
        win=True
    elif (spin in row3) and (bet=='trdRow'):
        win=True
    elif (spin%2==0) and (bet!=0) and (bet=='even'):
        win=True
    elif (spin%2!=0) and (bet!=0) and (bet=='odd'):
        win=True
    elif (spin<=18) and (spin!=0) and (bet=='low'):
        win=True
    elif (spin>=19) and (bet=='high'):
        win=True
    elif spin==bet:
        win=True
    else:
        win=False
    return win, spin

#--main--

from tkinter import *
import random as r

image()

print("Welcome to Roulette!\nBy Sid Sadel\n-------------")

balance=0
print("Balance:", balance)

isPlay=True

while(isPlay==True):

    bet=input("Enter the bet you would like to take: ")
    rawAmount=input("Enter the amount you would like to place: ")

    amount=isAmountInt(rawAmount)#checks if amount is int/changes to int
    odds_and_bet=oddsMethod(bet)#returns tuple with odds amount [x:1] and bet as int/str

    balance-=amount

    if odds_and_bet[0] is None:
        print('Invalid bet, not in dictionary')
        odds=oddsMethod(input('Enter a new bet: '))

    win_amt=odds_and_bet[0]*amount
    print('\nIf the bet hits, you could win:', win_amt)

    spin_info=spin(odds_and_bet[1])#returns tuple containing if spin was a win, spin value

    print("\nSpin:", spin_info[1]) 
    if spin_info[0]==True:
        balance+=win_amt
        print("Winner!")
        print("\nBalance:", balance)
    else:
        print("Better Luck Next Time!")
        print("\nBalance:", balance)

    play=input("\nWould you like to play again? (Y or N): ")
    print()
    if play=='y' or play=='Y':
        isPlay=True
    elif play=='n' or play=='N':
        isPlay=False

