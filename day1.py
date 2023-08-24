## Part 1
userName = input('What is your name? ')
monthAnswer = input('What month were you born in? ')
nameLength = len(userName)

print(f'Hello {userName}!')
print(f'There are {nameLength} letters in your name. ')

if monthAnswer == 'May':
    print('Happy birth Month!')
else:
    print('Your birthday is another month')

## Part 2
classNames = []
while True:
    className = input('Enter the names of your class(es), or hit the enter key to exit. ')
    if className == '':
        break
    classNames.append(className)

for className in classNames:
    print(className)












