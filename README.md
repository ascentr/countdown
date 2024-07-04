# COUNTDOWN GAME
# Description
Interactive words, numbers, and Anagram conundrum game inspired by the long-running British TV show of the same name.
You can visit https://www.ascentrick.com/daily_game/ to play the online version of this game.  This stand-alone version
allows multiple players to play the daily generated game and submit their scores. The game is generated in Python and served
to all modern browsers via Django.  JS enables interactive play.
## Features
-Letters Game (Make the longest word from 9 letters)
-Numbers Game (Get the target Number from 6 randomly generated numbers)
-Conundrum Game (Find the 9-letter word that has been scrambled)

##The scoring formula: 
-Word length X 2 for the letters game.  
-Time Left + 10 for the Numbers game
-Time Left + 10 for the Conundrum game.  
## Technologies Used
-Python 3.10
-Django 4.2
-HTML / JS / CSC / Bootstrap 4
-SQLite
-Docker 26.1.4
-docker compose 2.27

## How to Run
Run the compose.yml file 'docker compose up' 
OR
- Clone https://github.com/ascentr/countdown.git to clone to local.  
- python -m venv env_name
- activate the environment and cd into the root folder
- pip install requirements.txt
- python manage.py runserver to run on HTTP://localhost:8000
- Click on the How to Play button on home page and enjoy.

Thanks for taking interest and feedback is welcome at ascentrick@gmail.com


