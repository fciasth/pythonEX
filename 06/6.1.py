alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_1 = {}
alien_1['color'] = 'red'
print(alien_1)
alien_1['color'] = 'yellow'
print(alien_1)
del alien_0['points']
print(alien_0)

favorite_languages ={
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python'
}
for key,value in favorite_languages.items():
    print("\nkey"+key)
    print("Value"+value)
for name in favorite_languages.keys():
    print(name)
for name in sorted(favorite_languages.keys()):
    print(name)