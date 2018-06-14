print(4%3)
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

unconfirmed_user = ['alice','brian','candace']
confirmed_user = []
while unconfirmed_user:
    current_number = unconfirmed_user.pop()
    print("Verifying user:"+current_number.title())

pets = ['dog','cat','goldfish','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)