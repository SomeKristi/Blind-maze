# Blind maze game
# Made by SomeKristi on GitHub

from maps import *
from style import *


def Game():
    print("starting game\n")
    global won,playing
    won=False
    playing=True
    
    pPos= [0,0]
    print(style.refreshScreen)

    c=0
    chance=1
    from random import randint
    for line in map:
        i=0
        for char in line:
            if char==-1:
                if randint(1,chance) == 1:
                    pPos=[i,c]
                    chance+=1
            i+=1
        c+=1
    c=0

    def check(cords):
        test=[0,0]
        test[0]=pPos[0] + cords[0]
        test[1]=pPos[1] + cords[1]

        if test[0] < 0 or test[1] < 0 or test[1] > len(map)-1 or test[0] > len(map[test[1]])-1:
            heading()
            return False,f"{style.red}You were blocked by a wall{style.reset}"
        elif map[test[1]][test[0]]==-1:
            heading()
            return True,f"{style.yellow}You are back at spawn{style.reset}"
        elif map[test[1]][test[0]]==0:
            heading()
            return True,f"{style.blue}You moved{style.reset}"
        elif map[test[1]][test[0]]==1:
            heading()
            return False,f"{style.red}You were blocked by a wall{style.reset}"
        elif map[test[1]][test[0]]==2:
            global playing,won
            playing=False
            won=True
            heading()
            return True,f"{style.B_green}You reached the finish{style.reset}"

    heading()
    while playing:
        print(f"{style.dim}[left/right/up/down/exit]{style.reset}")
        get=input("action: ")
        print(style.refreshScreen)
        if get=="left":
            moved,feed=check((-1,0))
            print(feed)
            if moved:
                pPos[0]-=1
        elif get=="right":
            moved,feed=check((1,0))
            print(feed)
            if moved:
                pPos[0]+=1
        elif get=="up":
            moved,feed=check((0,-1))
            print(feed)
            if moved:
                pPos[1]-=1
        elif get=="down":
            moved,feed=check((0,1))
            print(feed)
            if moved:
                pPos[1]+=1
        elif get=="exit":
            playing=False
        else:
            heading()
            print(f"{style.italic+style.B_red}invalid input{style.reset}")

    if won:
        print(f"{style.bold+style.B_green}YOU HAVE WON!!!!{style.reset}")
    else:
        print(f"{style.red+style.bold}Giving up already?{style.reset}")


menu=True
print(style.refreshScreen)
def heading():
    print(f"{style.B_blue+style.bold}Blind maze{style.reset}")
heading()
while menu:
    print("[play/exit]")
    get1=input("action: ")
    print(style.refreshScreen)
    if get1=="exit":
        menu=False
        print("bye")
    elif get1=="play":
        print(f"{style.B_blue+style.bold}Blind maze{style.reset}")
        print(f"<1-{mapAmount}>")
        get2=input("Select map: ")
        print(style.refreshScreen)
        if get2.isnumeric():
            if int(get2) > 0 and int(get2) <= mapAmount:
                map=vars()["map"+get2]
                Game()
            else:
                heading()
                print(f"{style.italic+style.B_red}numbe out off range{style.reset}")
        else:
            heading()
            print(f"{style.italic+style.B_red}invalid input{style.reset}")
    else:
        heading()
        print(f"{style.italic+style.B_red}invalid input{style.reset}")
