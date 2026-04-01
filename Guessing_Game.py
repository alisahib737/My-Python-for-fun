# Change the variabel in name line-2 to change the word also change the hints in line-22,line-24 and line-26  
name = "banana"
_1 = "_"
_2 = "_"
_3 = "_"
_4 = "_"
_5 = "_"
_6 = "_"
hint_limit = 0
repitions = 100
while True:
    if name[0] == _1 and name[1] == _2 and name[2] == _3 and name[3] == _4 and name[4] == _5 and name[5] == _6:
        print("-"*50 + "Congratulations! You have guessed the word correctly" + "-"*50)
        break
    else:
        print("-" * 100)
        print(f"Word : {_1} {_2} {_3} {_4} {_5} {_6}")
    guess = input("Guess the letter or ask for a 'hint' :")
    if guess == "hint":
        hint_limit = hint_limit + 1
        if hint_limit == 1:
            print("It is a Fruit")
        elif hint_limit == 2:
            print("It's plant is the largest herb in the world")
        elif hint_limit == 3:
            print("It has high amount of calories")
        else :
            print("You've run out of hints")
        repitions -= 1
    elif len(guess) == 1:
        if guess == name[0]:
            if name[0] != _1:
                print("Correct Guess!")
                _1 = guess
                continue
        if guess == name[1]:
            if name[1] != _2:
                print("Correct Guess!")
                _2 = guess
                continue
        if guess == name[2]:
             if name[2] != _3:
                print("Correct Guess!")
                _3 = guess
                continue
        if guess == name[3]:
            if name[3] != _4:
                print("Correct Guess!")
                _4 = guess
                continue
        if guess == name[4]:
            if name[4] != _5:
                print("Correct Guess!")
                _5 = guess
                continue
        if guess == name[5]:
            if name[5] != _6:
                print("Correct Guess!")
                _6 = guess
                continue
        else :
            print("Wrong Guess!")
        repitions -= 1
    else :
        if hint_limit < 4:
            print("Invalid Input, Try Guessing one letter at a time or ask for hints. ")
        else:
            print("Invalid Input, Try Guessing one letter at a time.")
    if repitions == 0 :
        break
if repitions == 0 :
    print("You've Failed at the game")
else:
    score = repitions * 100 - hint_limit * 500
    if score < 0:
        score = 0
    if repitions == 0:
        print("You have failed to guess the word")
    else:
        print("Your score is :", score)
