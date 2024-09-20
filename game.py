#  quiz game
#List of questions
questions = ("Which Sport is known as popular sports?:",
             "Which player has most followers in the world?:",
             "Which Country has largest democracy?:")
#List of options             
options =   (("A.Football", "B.Cricket","C.Basketball"),
             ("A.Virat Kohli", "B.Cristiano Ronaldo", "C.Lionel Messi"),
             ("A.Newzealand", "B.Brazil", "C.India"))
#answer and guesses
answers = ("A","B","C")
guesses = []
score = 0
questions_num = 0
print("Welcome to quiz game!!!")

for question in questions:
    print("----------------------")
    print(question)
    for option in options[questions_num]:
       print(option)


# Adding total score
    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questions_num]} is the correct answer")

    questions_num += 1

print("--------------------")
print("       RESULTS      ")
print("--------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end="")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end="")
print()


score = (score / len(questions) * 100)
print(f"Your score is: {score}%")

#feedback from game
if score == 100:
    print("Great!!! Player ")
elif score < 50:
    print("Good game!")
elif score > 50:
    print("Well Done!!!")
else:
    print("Better luck next time")

