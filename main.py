


from turtle import *

from freegames import line

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def grid():
    "Draw Connect Four grid."
    bgcolor('light blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()


def tap(x, y):
    "Draw red or yellow circle in tapped row."
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()

# import random
# Min=1
# Max= 6


# roll_again= 'y'
# while roll_again=='y':
#   print('rolling the dice')
#   print('the value of the dice is: ')
#   dice1=random.randint(Min,Max)
#   dice2=random.randint(1,6)
#   print(dice1, dice2)
#   roll_again=input('Do you want to roll the dice again(y/n_): ')