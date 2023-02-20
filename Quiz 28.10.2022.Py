def quiz():

    print("Hello, and welcome to my world quiz!")
    print("For each question, you get 3 guesses, and a chance to score")
    print("up to 3 points. Guess correctly in the least amount of tries to get a higher score")

    def leaderboard():
        print("1) Gamerboy737: 11")
        print("2) MelonMan: 10")
        print("3) TheUserWhoRules: 8")
        print("4) dls: 5")

    guesses = 3 
    score = 0

    def question1():
        input("What is the capital of Wales?") 
        if input() == "Cardiff":
            print("WELL DONE!")
            if guesses > 2:
                score += 3
            elif guesses > 1:
                score += 2
            else:
                score += 1    
        else:
            guesses -= 1
            print("Unlucky, you have", guesses ,"guess left")
    
    guesses = 3 
    while guesses > 0:
        question1()
    print("Unlucky. The correct answer was Cardiff")

    def question2():
        input("What foods are most famous in Italy (multiple answers)?") 
        if input() == "pizza" or "pasta":
            print("WELL DONE!")
            if guesses > 2:
                score += 3
            elif guesses > 1:
                score += 2
            else:
                score += 1  
        else:
            guesses -= 1
            print("Unlucky, you have", guesses ,"guess left")
    
 
    while guesses > 0:
        question2()
    print("Oh dear, the possible answers were pizza and pasta")

    def question3():
        input("What is the largest city in the world?") 
        if input() == "Chongqing":
            print("WELL DONE!")
            if guesses > 2:
                score += 3
            elif guesses > 1:
                score += 2
            else:
                score += 1  
        else:
            guesses -= 1
            print("Unlucky, you have", guesses ,"guess left")
    
 
    while guesses > 0:
        question3()
    print("Oops, looks like the correct answer was Chongqing")

    def question4():
        input("Final question: What is the second largest continent in the world?") 
        if input() == "Africa":
            print("WELL DONE!")
            if guesses > 2:
                score += 3
            elif guesses > 1:
                score += 2
            else:
                score += 1  
        else:
            guesses -= 1
            print("Unlucky, you have", guesses ,"guess left")
    
 
    while guesses > 0:
        question4()
    print("The correct answer was Africa")

    print("Thanks for playing my quiz, you scored",score,)
    input("What is your username?")
    name = input

    leaderboard()
    if score > 11:
        print("Congratulations " ,name,", you beat Gamerboy737 and got the highscore!!!")
    elif score > 10:
        print("Congratulations " ,name,", you beat MelonMan!")
    elif score > 8:
        print("Congratulations " ,name,", you beat TheUserWhoRules!")
    elif score > 5:
        print("Congratulations " ,name,", you beat dls! (Not much of an achievement to be honest)")
    else:
        print("Looks like you're at the bottom of the leaderboard. Better luck next time.")

    input("Would you like to play again? Type yes to play again, or enter to end the quiz")
    if input() == "yes":
        quiz()
    else:
        print("Bye!")