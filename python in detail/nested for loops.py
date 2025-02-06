### something a little more complex. 
# domino tiles. 
# two for loops, one inside the other is called nested for loops. 

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print() #it prints out domino type of tiles.

print("\n")

teams = ['BAN', 'SRI', 'ENG', "AUS"]
for homeTeam in teams:
    for awayTeam in teams:
        if homeTeam != awayTeam:
            print(homeTeam + " vs " + awayTeam)

print("\n")