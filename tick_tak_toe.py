import random
import sys

#welcome screen
print("WELCOME! THIS IS YOUR FIRST PYTHON GAME")
player_1 = input("Enter Player 1 name ")
player_2 = input("Enter Player 2 name ")
cross = "X"
circle = "0"

#board contents
pos = [" "," "," "," "," "," "," "," "," "]
print("Chosing a random starter ")
chosen_player = random.randint(1,2)
ncp = 3 -chosen_player
if chosen_player == 1:
    print("Player 1 goes first")
else:
    print("Player 2 goes first")
last_occ = "0"

def Display(pos):
    h = "-----"
    v = "|"
    print(pos[0]+v+pos[1]+v+pos[2])
    print(h)
    print(pos[3]+v+pos[4]+v+pos[5])
    print(h)
    print(pos[6]+v+pos[7]+v+pos[8])
    
def Win(pos, curr):
    if pos[0] == curr and pos[3] == curr and pos[6] == curr :
        return True
    elif pos[1]==curr and pos[4]==curr and pos[7]==curr :
        return True
    elif pos[2]==curr and pos[5]==curr and pos[8]==curr :
        return True
    elif pos[0]==curr and pos[1]==curr and pos[2]==curr :
        return True
    elif pos[3]==curr and pos[4]==curr and pos[5]==curr :
        return  True
    elif pos[6]==curr and pos[7]==curr and pos[8]==curr :
        return  True
    elif pos[0]==curr and pos[4]==curr and pos[8]==curr :
        return True
    elif pos[6]==curr and pos[4]==curr and pos[2]==curr :
        return True
    else :
        return False

def Valid(pos, box) :
     if box >= 1 and box <= 9 :
        return pos[box-1] == " "
     else:
        return False


def End(pos):
    flag =  " " in pos
    return not flag
        
Display(pos)

#game starts
while(True):
    box = int(input("Which box do you want the number in [1-9]"))
    if Valid(pos, box) == True:
        if last_occ == cross:
            curr=circle
            pos[box-1] = curr
            last_occ = curr
        else :
            curr=cross
            pos[box-1] = curr
            last_occ = curr
    else:
        print("Give a valid input ")
        continue
        
    Display(pos)
    if Win(pos,curr) and curr == "X" :
        print("Person ",chosen_player," has won")
        sys.exit()
    elif Win(pos,curr) and curr == "0":
        print("Person ",ncp," has won")
        sys.exit()
        
    elif End(pos):
        print("Its a draw")
        sys.exit()
    

