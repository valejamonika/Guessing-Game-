import random

play_game = 'y'
while(play_game == 'y' or play_game == 'Y'):
    answer = random.randint(1,100)
    guess_number = int(input("You Have To Guess A Number Between 1 to 100 ?"))
    count = 1


    while guess_number != answer:
        if guess_number > answer:
            print("OOPS! Your Given Number is Too Large . Please Try Again To Reach Goal...")
        if guess_number < answer:
            print("OOPS! Your Given Number is Too Small . Please Try Again To Reach Goal...")
        
        guess_number = int(input("You Have To Guess A Number Between 1 to 100 ?"))
        count +=1
    print("Brilliant ! You Got It. You Tried " + str(count) + 'times.')
    play_game = input('Press "Y" To Continue................ And Any Key To Quit The Game............ ')