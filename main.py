#Braden Leach
#Nov 27 2024 
#Text Adventure Game two


from time import sleep #need once
#---Set Variables--- 
lives = 3
score = 0 

rucksack = ['key','duck','brush']

def lives_score():
    print()
    print('*********************************')
    print(f'you have, {lives}, lives left')
    print(f'Your score is {score}')
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

if choice1.lower == 'r':
    print('The old crone catches you and puts you in the pot')
    lives = lives -1 # lose a life
else:
    print('you cast a spell on her and she explodes!!')
    score = score + 5 # add 5 to score 

lives_score() 

#----SCENARIO 2----#
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

if choice2.lower == 's':
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
print(f'You look in your ruchsack and find: {rucksack}')

# ----CHOICE 3----#

choice3 = input('''Press K to use the key, D to pull out the duck, 
or b to try and break the window with the brush: ''')