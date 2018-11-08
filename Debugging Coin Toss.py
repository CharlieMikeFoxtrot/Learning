import random, logging
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Program start.')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('guess is %s.' %(guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'
logging.debug('Toss is %s.' %(toss))
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('gues is %s.' % (guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')