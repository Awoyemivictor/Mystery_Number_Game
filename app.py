from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# import random as r

import game



st.set_page_config(page_title="Mystery Number Game", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Game
# def guessGame():
#     # st.header("Enter the difficulty level: \n")
#     # st.write("1 for easy!\t")
#     # st.write("2 for medium!\t")
#     # st.write("3 for difficult!\t")
#     # st.write("0 for ending the game!\n")

#     # // select the level of difficulty
#     # difficultChoice = input("Enter the number: ")
    
    
#     # // generating the secret number
#     # list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


#     user_name = input('Type your name : ').title()
#     print(f'Hello {user_name}.')

#     user_said = input(f'{user_name} do you want to play Number Guessing game (Y/N) : ').lower()

#     while True:

#         if ('y' not in user_said) and ('n' not in user_said) and (user_said != True):
#             user_said = input('Invalid keyword\nType again : ').lower()

#         elif 'y' in user_said:
#             winning_number = r.randint(1,10)
#             user_guessed = int(input('\nYou have 6 guesses.\nGuess any number between 1 and 10\nGuess the number : '))
#             turn = 1

#             while True:
            
#                 if winning_number == user_guessed:
#                     print(f'Congrats you guessed the number in {turn} times.')
#                     break

#                 elif turn == 6:
#                     print(f'Sorry You can\'t guess the number. The number is {winning_number}.')
#                     break

#                 else:
#                     if winning_number > user_guessed:
#                         print('Too Low')
#                     else:
#                         print('Too High')

#                     print(f'You have {6-turn} guesses left.')
#                     turn += 1
#                     user_guessed = int(input('Guess again : '))

#             user_said = input(f'\n{user_name} do you want to play more (Y/N) : ')

#         else:
#             print(f'\nOk Bye {user_name}. See You soon.')
#             break




# LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_wXdFmB.json")
image_contact_form = Image.open("images/photo_2023-01-01 1.30.40 AM.jpeg")
img_lottie_animation = Image.open("images/victor.png")

# HEADER SECTION
with st.container():
    st.subheader("Hi, You can be a lucky winner today! :wave:")
    st.title("Welcome to Mystery Number Game!")
    st.write("All you have to do is to choose a Level and Guess the right number from 1 to 30. If you win, you stand a chance to earn a mystery coin. You will have limited choices based on the level you choose. There are 3 levels in the Mystery Number Game:")
    st.write("1 for EASY! | 2 for MEDIUM! | 3 for DIFFICULT!")
    st.write("[PLAY NOW >](https://www.awoyemivictor.info)")

# WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("How the game works...")
        st.write("##")
        st.write(
            """
            - In this game, the computer generates a secret number in the range of 1 to 100, and the player has to guess it.\n
            - The game has three difficulty levels. A player’s chances of guessing are limited by the level they choose. The easy level gives the player 10 chances to guess the secret number, the medium level 7 chances, whereas the difficult level only offers 5 chances.\n
            - During the game, a player tells the computer his assumption about a number, and the computer tells if the player is correct. If his number is less or more than the secret number, the computer informs the player, and the player tries again. \n
            - The player can also end the game at any time. \n
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# PROJECTS ---
with st.container():
    st.write("---")
    st.header("About Me")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        with text_column:
            st.subheader("My name is Awoyemi Victor A.")
            st.write(
                """
                I began my career as a Software Engineer & Web Developer in the middle of 2020 while working as a freelancer on the side. I've had a deep passion for programming from childhood and this is what led me to began studying Software Engineering.

                I've also had to foster my knowledge as a Software Engineer and Developer since July 2022 studying in the ALX Cohort 8 Programme which has been so amazing. So far, I have been learning low level programming languages, ranging from C to higher level languages like C++, Python, MySQL, JavaScript, HTML, CSS & Others. 
                
                We were tasked to build a project from scratch and this is what bring the idea of this Mystery Number Game project.

                I currently work as a part-time freelance developer exclusively on Upwork. You can check through my repositories to see projects which I've been able to work on and contribute to both as a student and also as a programmer.

                In case you have any Questions or feel like connecting with me?

                You can reach out to me on:
                """
            )
            st.markdown("[FACEBOOK](https://web.facebook.com/awoyemiavictor)")
            st.markdown("[GITHUB](https://github.com/Awoyemivictor)")
            st.markdown("[WEBSITE](https://awoyemivictor.info)")


# ----CONTACT-----
with st.container():
    st.write("---")
    st.header("Leave Me A Message!")
    st.write("##")

    # form-submit
    contact_form = """
    <form action="https://formsubmit.co/destininoflashmite@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



#--GAME
with st.container():
    st_lottie(game, height=300, key="coding")
