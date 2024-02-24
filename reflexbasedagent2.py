# Reflex Agent


goalState={'A':'0','B':'0','C':'0'}
action =0 # 0 is clean ,1 is dirty
cost =0
roomState={'A':'1','B':'1','C':'1'}
#initial input
print("Enter in starting location of rooms(A/B/C)")
location=input()

for room in roomState:
    action=input("Enter the state of "+room +"(0 means Clean 1 means Dirty)")
    roomState[room]=action
   
print("Current state: "+ str(roomState))
print("Goal state: "+str(goalState)) 
print("Vaccum cleaner is placed in location "+str(location))
if (roomState!=goalState):
    if(roomState['A']=='1'):
        roomState['A']='0'
        cost+=1
        print("Location A was dirty\nLocartion A has been clean")
    if(roomState==goalState):
        print("Goalstate has been met.")
        print("\nTotal cost:" +str(cost))

    #if A is clean. Going From A-> B
    else:
        print("\nA is clean")
        print("\nA -> B")
        print("\nCost for moving within rooms =1")
        cost+=1
        if(roomState['B']=='1'):#if B is dirty
            roomState['B']='0'
            cost+=1
            print("Location B was Dirty\n Location B has been CLean")

        if (roomState ==goalState):
            print("Goal state has been met.")
            print("\nTotal cost: "+str(cost))
         #if B is clean. Going From B-> C
        else:
            print("\nB is clean")
            print("\nB -> C")
            print("\nCost for moving within rooms =1")
            cost+=1
            if(roomState['C']=='1'):#if C is dirty
                roomState['C']='0'
                cost+=1
                print("Location C was Dirty\n Location C has been CLean")
            if (roomState ==goalState):
                print("Goal state has been met.")
                print("\nTotal cost: "+str(cost))


else:
    print("\nAll rooms are already clean")
    print("\nTotal cost: "+ str(cost))