import random

answer = random.randint(1, 10)
count = 0

while True:
    print("Your guess?", end="")
    guess = int(input())
    # count = count + 1
    count += 1

    if answer == guess:
        print("Bingo!! あなたは %i 回で正解しました" %count)
        break
    elif answer > guess:
        print("Bigger")
    else:
        print("Smaller")
