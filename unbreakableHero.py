'''
Heroes beta
version 0.1
inches
2017-11-17
'''
hp = 100
print('Welcome to Heroes\' world')
print('|The world is like this #####')
name = input('input your name:')

if not name:
	name = 'player01'

usermsg = [name, hp]

print("your hero's name is:", usermsg[0], ',Hp is:', usermsg[1] )
print('and now you are here:  *####, "a" for left, "d" for right')

userinput = input()
if userinput == 'd':
	print('you are here #*###')
if userinput == 'a':
    print('you are here *####')
