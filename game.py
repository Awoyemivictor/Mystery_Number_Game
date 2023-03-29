import random as r

# welcome screen
user_name = input('Type your name : ').title()
print(f'Hello {user_name}.')

user_said = input(f'{user_name} do you want to play Number Guessing game (Y/N) : ').lower()

while True:

    if ('y' not in user_said) and ('n' not in user_said) and (user_said != True):
        user_said = input('Invalid keyword\nType again : ').lower()

    elif 'y' in user_said:
        winning_number = r.randint(1,10)
        user_guessed = int(input('\nYou have 6 guesses.\nGuess any number between 1 and 10\nGuess the number : '))
        turn = 1

        while True:
        
            if winning_number == user_guessed:
                print(f'Congrats you guessed the number in {turn} times.')
                break

            elif turn == 6:
                print(f'Sorry You can\'t guess the number. The number is {winning_number}.')
                break

            else:
                if winning_number > user_guessed:
                    print('Too Low')
                else:
                    print('Too High')

                print(f'You have {6-turn} guesses left.')
                turn += 1
                user_guessed = int(input('Guess again : '))

        user_said = input(f'\n{user_name} do you want to play more (Y/N) : ')

    else:
        print(f'\nOk Bye {user_name}. See You soon.')
        break


# # importing the libraries
# import random
# import math


# # intro section
# print("""hello!!!
# this is a guessing game.
# please enter your bound for the game to start""")


# # getting the inputs
# lower = int(input("Enter Lower bound:- "))
# upper = int(input("Enter Upper bound:- "))

# # generating the random number between the chosen bound
# x = random.randint(lower, upper)
# print("\n\tYou've only ",
#       round(math.log(upper - lower + 1, 2)),
#       " chances to guess the integer!\n")

# # Initializing the number of guesses.
# guess_count = 0

# # while loop for each round of the game
# while guess_count < math.log(upper - lower + 1, 2):
#     guess_count += 1

#     # taking guessing number as input
#     guess = int(input("Guess a number:- "))

#     # Condition testing
#     if x == guess:
#         print("Congratulations you did it in ",
#               guess_count, " try")
#         # Once guessed, loop will break
#         break
#     elif x > guess:
#         print("You guessed too small!")
#         print("You have ", round(math.log(upper - lower + 1, 2)) -
#               guess_count, " guess left")
#     elif x < guess:
#         print("You Guessed too high!")
#         print("You have ", round(math.log(upper - lower + 1, 2)) -
#               guess_count, " guess left")


# # If you guessed more than your chances the game will end
# if guess_count >= math.log(upper - lower + 1, 2):
#     print("\nThe number is %d" % x)
#     print("\tBetter Luck Next time!")