# 3.4
party = ['tom','jerry','jim']
print(party)
# 3.5
print(party[2])
party[2]='bill'
print(party)
# 3.6
party.insert(0,'damen')
party.insert(2,'sherry')
party.append('ham')
print(party)
for i in range(4):
    party.pop()
print(party)
del party[0]
del party[0]
print(party)