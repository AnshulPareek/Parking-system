a = [1,2,3,4,5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]

def line():
    print("|",end="")
    for j in range(9):
        print(f"|----",end="")
    print("||")
def space():
    print("|",end="")
    for j in range(9):
        print(f"|    ",end="")
    print("||")
def structure():
    for i in range(13):
        if i%2==0:
            line()
        elif i == 1:
            print("|",end="")
            for j in range(9):
                print(f"| 0{a[0][j]} ",end="")
            print("||")
        elif i == 5:
            print("|",end="")
            for j in range(9):
                if j>1 and j<7:
                    print(f"| {a[1][j-2]} ",end="")
                else:
                    print(f"|    ",end="")
            print("||")
        elif i == 7:
            print("|",end="")
            for j in range(9):
                if j>1 and j<7:
                    print(f"| {a[2][j-2]} ",end="")
                else:
                    print(f"|    ",end="")
            print("||")
        elif i == 11:
            print("|",end="")
            for j in range(9):
                if j>1 and j<7:
                    print(f"| {a[3][j-2]} ",end="")
                else:
                    print(f"|    ",end="")
            print("||")
        else:
            space()

    for i in range(2):
        print("||",end="")
        for j in range(9):
            if j<2 or j>6:
                print(f"    ",end="|")
            else:
                if j==6:
                    print(f"    |",end="")
                else:
                    print(f"     ",end="")
        print("|")
structure()

def park():
    loc = int(input("\nEnter the location at which you want to park Your car = "))
    cc = input("Enter your car name first two letters = ")
    if loc>0 and loc<10:
        if loc != a[0][loc-1]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[0][loc-1] = cc
            print(f"Your Car \"{cc}\" is succesfully parked at number {loc}.")
    elif loc>9 and loc<15:
        if loc != a[1][loc-10]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[1][loc-10] = cc
            print(f"Your Car \"{cc}\" is succesfully parked at number {loc}.")
    elif loc>14 and loc<20:
        if loc != a[2][loc-15]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[2][loc-15] = cc
            print(f"Your Car \"{cc}\" is succesfully parked at number {loc}.")
    elif loc>19 and loc<25:
        if loc != a[3][loc-20]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[3][loc-20] = cc
            print(f"Your Car \"{cc}\" is succesfully parked at number {loc}.")
    else:
        print("\nSorry to inform you but our parking plot only have 24 location to park.\nKindly take an overview first.")
def pull():
    cc = input("Enter your car name = ")
    loc = int(input("Enter your car parking location = "))

    if loc>0 and loc<10:
        if cc == a[0][loc-1]:
            a[0][loc-1] = loc
            print(f"Here you go, your car {cc} has succesfully removed from the location number {loc}.\nThanks for your cooperation.")
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>9 and loc<15:
        if cc == a[1][loc-10]:
            a[1][loc-10] = loc
            print(f"Here you go, your car {cc} has succesfully removed from the location number {loc}.\nThanks for your cooperation.")
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>14 and loc<20:
        if cc == a[2][loc-15]:
            a[2][loc-15] = loc
            print(f"Here you go, your car {cc} has succesfully removed from the location number {loc}.\nThanks for your cooperation.")
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>19 and loc<25:
        if cc == a[3][loc-20]:
            a[3][loc-20] = loc
            print(f"Here you go, your car {cc} has succesfully removed from the location number {loc}.\nThanks for your cooperation.")
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
def update():
    cc = input("Enter your car name = ")
    loc = int(input("Enter your current car parking location = "))
    uloc = int(input("Enter desired car parking location = "))
    if loc>0 and loc<10:
        if cc == a[0][loc-1]:
            a[0][loc-1] = loc
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>9 and loc<15:
        if cc == a[1][loc-10]:
            a[1][loc-10] = loc
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>14 and loc<20:
        if cc == a[2][loc-15]:
            a[2][loc-15] = loc
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")
    elif loc>19 and loc<25:
        if cc == a[3][loc-20]:
            a[3][loc-20] = loc
        else:
            print(f"You entered incorrect details.\nKindly get a look at overview again.")


    if uloc>0 and uloc<10:
        if uloc != a[0][uloc-1]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[0][uloc-1] = cc
            print(f"Your Car \"{cc}\" location is succesfully updated to number {uloc} from {loc}.")
    elif uloc>9 and uloc<15:
        if uloc != a[1][uloc-10]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[1][uloc-10] = cc
            print(f"Your Car \"{cc}\" location is succesfully updated to number {uloc} from {loc}.")
    elif uloc>14 and uloc<20:
        if uloc != a[2][uloc-15]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[2][uloc-15] = cc
            print(f"Your Car \"{cc}\" location is succesfully updated to number {uloc} from {loc}.")
    elif uloc>19 and uloc<25:
        if uloc != a[3][uloc-20]:
            print(f"\nSorry!,Someone else had taken that spot.\nYou can try another location by getting an overview.")
        else:
            a[3][uloc-20] = cc
            print(f"Your Car \"{cc}\" location is succesfully updated to number {uloc} from {loc}.")
    else:
        print("\nSorry to inform you but our parking plot only have 24 location to park.\nKindly take an overview first.")

def main():
    b = int(input("1. Get Parking Area Overview again.\n2. Park Your Car.\n3. To pull out your car from parking plot.\n4. Update your car location.\n\nChoose a number = "))
    c = 'A'
    if b == 1:
        structure()
        c = input("\n\nDo u want to do more operations(Y/N) :- ")
        if c == 'Y':
            main()
        elif c == 'y':
            main()
        else:
            exit()
    elif b == 2:
        park()
        c = input("\n\nDo u want to do more operations(Y/N) :- ")
        if c == 'Y':
            main()
        elif c == 'y':
            main()
        else:
            exit()
    elif b == 3:
        pull()
        c = input("\n\nDo u want to do more operations(Y/N) :- ")
        if c == 'Y':
            main()
        elif c == 'y':
            main()
        else:
            exit()
    elif b == 4:
        update()
        c = input("\n\nDo u want to do more operations(Y/N) :- ")
        if c == 'Y':
            main()
        elif c == 'y':
            main()
        else:
            exit()
main()