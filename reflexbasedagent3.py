goalState = {'A': '0', 'B': '0', 'C': '0', 'D': '0'}
actions = {'0': 'CLEAN', '1': 'DIRTY'}
cost = 0
roomstate = {'A': '1', 'B': '1', 'C': '1', 'D': '1'}

print("Enter the starting location of the vacuum (A/B/C/D):")
location = input().strip().upper()


while location not in ['A', 'B', 'C', 'D']:
    print("Invalid location. Please enter A, B, C, or D:")
    location = input().strip().upper()

for room in roomstate:
    if room != location:
        print(f"Enter the status of room {room} (0 for clean, 1 for dirty):")
        status = input().strip()
        while status not in ['0', '1']:
            print("Invalid status. Please enter 0 for clean, 1 for dirty:")
            status = input().strip()
        roomstate[room] = status

print("Current state:", roomstate)
print("Goal state:", goalState)
print("Vacuum cleaner is placed in location:", location)

while roomstate != goalState:
    if roomstate[location] == '1': 
        roomstate[location] = '0'
        cost += 1
        print(f"Location {location} was dirty.")
        print(f"Location {location} has been cleaned.")


    if location == 'A':
        location = 'B'
    elif location == 'B':
        location = 'C'
    elif location == 'C':
        location = 'D'
    # elif location == 'D':
    #     location = 'A'

    if roomstate[location] == '1':
        cost += 1

    print("Moved to location:", location)

print("\nGoal state has been met.")
print("\nTotal cost:", cost)