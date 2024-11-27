#Braden Leach
#Nov 27 2024 
#Text Adventure Game two


from time import sleep #need once
import sys # need this once for exit
#---Set Variables--- 
lives = 3
score = 0 

rucksack = ['key','duck','brush']

def gameover():
   if lives <= 0:
     print(f'You have run out of lives, {name}')
     print('GAME OVER!!!')
     lives_score()
     sys.exit()


def lives_score():
    print()
    print('*********************************')
    print(f'you have, {lives}, lives left')
    print(f'Your score is {score}')
    print(f'Your rucksack contains {rucksack}')
    print('*********************************')
    print()
#----welcome----
name = input('What is your name: ')

print(f'Welcome, {name}, to the adventure!')
print()
print()
lives_score()
print()
sleep(2)

#--------scenario 1--------

print('''You awake to the sound of an old crone cooking in her pot.''')
print()
sleep(2)
print('She is singing an old song about cooking.')
print()
sleep(2)
print('...I think she about to cook you!')

#----CHOICE 1----#

choice1 = input('Press r to run away or e to use magic: ')

if choice1 == 'r':
    sleep(1)
    print('The old crone catches you and puts you in the pot')
    lives = lives -1 # lose a life
else:
    sleep(1)
    print('you cast a spell on her and she explodes!!')
    score = score + 5 # add 5 to score 
sleep(1)
lives_score() 

#----SCENARIO 2----#
sleep(1)
print('''You move further into the forest. It is full of
strange and worrying noises. What other strange creatures 
might you encounter?''')
sleep(2)
print()

print('you hear a scratching noice')
sleep(1)
print()

print('''it's getting closer...''')
sleep(2)
print()

print('''Oh phew! It's just a cute fluffy bunny!''')
print()
print()

#----CHOICE 2----#

choice2 = input('''Press S to strike it, press K to kill it or 
press r to run away: ''')

if choice2 == 's':
    print(f'The bunny reveals ENORMOUS fangs and bites your head off')
    lives = lives - 1 # lose a life
elif choice2 == 'k':
    print('''The bunny reveals ENORMOUS fangs, buy you kill it 
before it can bite you!''')
    score = score + 5 # add 5 points 
else: 
    print('''the bunny is quicker than it looks...
and before you know it, it hops onto you...
reveals ENORMOUS fangs and bites your head off!''')
    lives = lives - 1 # lose a life

lives_score()

#---- SCENARIO 3 ----#
print('As you walk through the forest you find a house')
print()
sleep(2)
print("Unlike the old crone's cottage, it is warm, invinting and makes you feel safe.")
print()
sleep(2)
print('You walk up to the door and try to open it, but it is locked!')
print()
sleep(2)
print('Perhaps there is something in your bag which can help?')
print()
sleep(2)
print(f'You look in your ruchsack and find: {rucksack}\n')

# ----CHOICE 3----#

choice3 = input('''Press K to use the key, D to pull out the duck, 
or b to try and break the window with the brush: ''')

if choice3 == 'k':
    print('''To your great luck, the key fits then door, and you 
open the door to the house ''')
    score = score + 5 
    rucksack.remove('key')
elif choice3 == "d":
    print('You pull out the duck...')
    print()
    sleep(2)
    print("Although it doesn't help, it makes you feel better!")
    score = score + 2
    rucksack.remove('duck')
else: 
    print('You try and break the glass with the brush...')
    print()
    sleep(2)
    print('But it satters the glass and goes in your arm!')
    lives = lives - 1 
    rucksack.remove('brush')
    sleep(2)
    print()
    gameover()

lives_score()

#----SCENARIO 4----#
print(f'''YOu look around yourself in the house. It is a
very nice, homely and comfortable cottage. You get the
felling someone kind lives here. ''')
sleep(1)
print()
print(f'''You look around yourself again and see a table with
a cake! Your stomach rumbles noisly. You did not realise how 
hungry you were. Besides the cake is a knife. You decide it 
wouldn't be a problem to slice the cake. ''')
print()
sleep(2)

#---- CHOICE 4 ----#

choice4 = input('''Press A to eat the cake now, or b to put it 
in your rucksack for later.''')

if choice4 == 'a':
    print(f'''You eat the cake. It's very delicious and you feel a
bit better, even though that old hag situation 
is still freaking you out.''')
    score = score + 2 
else: 
    print('You carefully wrap the cake and store it for later')
    rucksack.append('cake')

lives_score()

#----SCENARIO 5----#

print('The door to the cottage opens suddenly! You are surprised!')
sleep(2)
print()
print()
print(f'''Standing ther is a little old man. He is surp''')