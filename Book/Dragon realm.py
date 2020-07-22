import random
import time


def displayIntro():
    print(
        'Welcome you are in a land full of cookies and pitbulls. In front of you, you see two caves. In one cave the pitbull is friendly and will share his treasure with you. The other pitbulll is greedy and hungry and will eat you on sight.')
    print()


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into, 1 or 2?')
        cave = input()

        return cave


def checkCave(chosenCave):
    print('You approach the cave....')
    time.sleep(2)
    print('It is dark and spooky ...')
    time.sleep(2)
    print('A large pitbull jumps out in front of you! He opens his jaws and ...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
