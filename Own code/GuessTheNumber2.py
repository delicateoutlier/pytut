import random
guessestaken = 0

print ('Welcome , what is your name ?')
my_name = input()

number = random.randint(1,70)
print('Well,' + my_name + ',I am thinking about a number between 1 and 20.')

for guessesTaken in range(5):
    print('Take a guess.')
    guess = input()
    guess = int (guess)                                                         #added if it is an odd or even number
    if (guess % 2) == 0:
        print('{0} is even number. '.format(guess))
    else:
        print('{0} is odd number.'.format(guess))

    if guess < number:
        print ('Your guess is too low.')

    if guess > number :
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('Good job,' + my_name + '!You guessed my number in ' +
          guessesTaken + '  guessess!')

if guess !=number:
    number = str(number)
    print('Nope. The number I was thinking of was  .' + number + '   ')



