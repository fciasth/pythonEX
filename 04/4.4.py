players = ['mike','joshua','peal','bill','tiger']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[-3:])
print("Here are first three players on my team:")
for player in players[:3]:
    print(player.title())
myFriend = players[:]
print(myFriend)
