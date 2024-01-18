import random # use for maths quiz 
import datetime # logs date and time 

## logs the  name, time, subject, level and Grade! 
def log_test_results(student_name, subject, level, grade):
   with open("test_log.txt", "a") as file:
       now = datetime.datetime.now()
       file.write(f"Student Name: {student_name}, Date and Time: {now}, Subject: {subject}, Level: {level}, Grade: {grade}\n")

first = input('What is your First name?')
second = input('Whats your second name?') 
print(f'Welcome {first}{second}')

while True: # continous the code if user presses "no"

    choice = int(input('Choose a quiz: \n1. Maths\n2. Irish'))
    if choice == 1:
        numQuestions = max(5, min(25, int(input('How many questions would you like (5-25)? '))))


        score = 0  # score starts at 0 and gets added by correct answers 
        counter = 0  # starts at 0, responable for the amount of questions asked. 
        feedback = '' # counter for the feedback 


        while counter < numQuestions: 
        
            num1 = random.randint(1,10) # randomizes first number 
            num2 = random.randint(1,10) # randomizes secodond number 
            operation = random.choice(['+', '-']) # randomizes operation 

            if operation == '-':
                num1, num2 = max(num1, num2), min(num1, num2)
                # this ensures that num1 is always greater or equal to num2 to avoid neg numbers.


            correctAnswer = num1 + num2 if operation == '+' else num1 - num2
            userAnswer = int(input(f' {num1} {operation} {num2} =')) # randomizes the numbers and the operation! 
            # gives us random numbers, the correct anser and asks user for the answer. 

            counter += 1  # adds to counter per question asked 

            if userAnswer == correctAnswer: 
                    print('Youre Right! \u2713')
                    score += 1 ## adds one to score per correct answer
                    feedback += f'{num1} {operation} {num2} = {userAnswer} Correct! \U0001F389 \n' # adds feedback to the end of code 
            else: 
                    print(f'Youre wrong \u274C the corret awnser is {correctAnswer}') # tells user its the wrong anwser and tells correct awnser. 
                    feedback += f'{num1} {operation} {num2} = {userAnswer} InCorrect!. Corecct Answer is {correctAnswer} \U0001F641 \n' # adds feedback to the end of the code

        percent = (score / numQuestions)* 100. # calculates the percentage. 
        

        if percent >= 80:
            print(f'youre score is {percent:.2f}%, \U0001F389 Excellent!')
        elif percent >= 60:
            print(f'youre score is {percent:.2f}%, \U0001F920 Good job!')
        elif percent >= 40:
            print(f'youre score is {percent:.2f}%, \U0001F614 Not bad, keep trying!')
        else:
            print(f'youre score is {percent:.2f}%, \U0001F641 You can do better, practice more!') 
        
        # if statement that prints a statement depending on the result! 

        print(feedback)
        log_test_results(first, "Maths", None, percent) ## adds logs into the log.txt file

    elif choice == 2:
        
        score = 0  # score starts at 0 and gets added by correct answers 
        counter = 0  # starts at 0, responable for the amount of questions asked. 
        feedback = '' # counter for the feedback 
        
        level = int(input("Youve chosen Irish! What level would you like?(1-5)"))

        irish = open(f'irish{level}.txt', 'r') # reads lines in file 
        for line in irish: 
                line= line.strip() # gets rid of final \n
                line= line.split(',') #splits it up , sep my commas 
                irish = line[0]  
                english = line[1]

                answer = input(f"{irish:10}").strip()
                if answer == english: 
                     print("Correct")
                     score += 1 
                     counter += 1
                     feedback += f'{irish} {answer} Correct! \U0001F389 \n '
                else: 
                     print(f"Wrong correct awnser is {english}")
                     feedback += f'Incorrect!. Corecct Answer is {english} \U0001F641 \n'

        percent = (score / 5 )* 100. # calculates the percentage. 

        if percent >= 70:
            print(f'youre score is {percent:.2f}%, \U0001F389 Excellent!')
            if level == 5:  # Check if the current level is the final level (level 5)
                    print("Congratulations! You have completed all levels.") # 
            else:    # Encourage moving to the next level if not the final level
                    print(f'You should try level {level + 1}')

        elif percent >= 50:
            print(f'youre score is {percent:.2f}%, \U0001F920 Good job!')
        elif percent >= 40:
            print(f'youre score is {percent:.2f}%, \U0001F614 Not bad, keep trying!')
        else:
            print(f'youre score is {percent:.2f}%, \U0001F641 You can do better, practice more!')

        print(feedback) 
        log_test_results(first, "Language", level, percent) ## adds logs into the log.txt file


    finished = input("are you finished ?").strip() 
    if finished == "yes": 
        print("Goodbye ! ")
        break

#finished input asks the user if theyre finished with this exam. If no, it loops. If yes it breaks and prints goodbye! 



