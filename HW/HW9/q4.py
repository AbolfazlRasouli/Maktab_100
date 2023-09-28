import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', type=int, default=0, help='start from')
parser.add_argument('-e', '--end', type=int, default=100, help='end')
parser.add_argument('-g', '--guess', type=int, default=5, help='how many guess')

args = parser.parse_args()

start = args.start
end = args.end
chance = args.guess

random_num = random.randint(start, end)

try:
    for chance_num in range(1, chance + 1):
        anwser = int(input(f'{chance_num} guess>>> '))
        if random_num == anwser:
            print('you WON!!! :D')
            break
        elif random_num < anwser and anwser <= end and start <= anwser:
            print('your guess is bigger than anwser!!! :O')
        elif random_num > anwser and anwser <= end and start <= anwser:
            print('your guess is smaller than anwser!!! :O')
        else:
            print(f'anwser must between {start} & {end}!!! :(')
    else:
        print('you LOST!!! :(')
except ValueError as e:
    print(e)