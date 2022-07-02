# Welcome to my Battleships game 
This game is a single player game against AI and is Coded entirely on python. Instructions on how to play are given once the game is run.

## Requirements

- You will be required to have an editor that can run python code to play this game
- A recommendation I have is PyCharm 
- Link to download PyCharm can be found here : https://www.jetbrains.com/pycharm/download/#section=windows

## How the game works

- This game can be started by either pressing the run button on python or by typing python3 run.py in the command terminal
- Once the game is started , an introduction message is displayed which explains how to play.
- ![run-game](https://user-images.githubusercontent.com/97538312/177016232-57b648ee-4794-4fc9-9648-61c3a27a2494.jpg)
- The first input will be to guess a row and the only acceptable values for this are whole numbers from 1 to 5
- The next input value will be to guess a column letter ranging from A to E 

## Features
- Any input value that is not an integer between 1 and 5 will throw an error for the row guess
- Any input value that is not between letters A to E will throw an error for the column guess
- If the user enters a lowercase letter, the code will still accept this by converting all input values to uppercase
- The following error occurs for an incorrect input value
- ![incorrect-input](https://user-images.githubusercontent.com/97538312/177016836-1e56e5e7-a773-429f-a6cb-f97e97febb7e.jpg)

- If coordinates have already been guessed then the following error will show :
- ![already-guessed](https://user-images.githubusercontent.com/97538312/177017306-8008e8e3-fa97-4cd4-aed2-c4c5232506ce.jpg)

- When a ship has been hit the message will display and an X will appear in that location 
- ![hit-ship](https://user-images.githubusercontent.com/97538312/177017317-b4bd8dd8-a7a7-4b7b-a2eb-3974c7a530d7.jpg)

- If a ship is missed a message will alert the player and the coordinate is marked with '-'
- ![missed-ship](https://user-images.githubusercontent.com/97538312/177017327-242b8e64-6757-4286-bfc6-312d13a181df.jpg)




## Unfixed Bugs
- There are no unfixed bugs in the code

## Testing
- For the testing process I used print statements and kept running the code after a new function was added which was noticeable when run
- This allowed for me to efficiently pick out any issues in the code as it occured
- I also put the code through PEP8 Online : http://pep8online.com/
- In this there were a few minor issues that are about lines of code being too long.
 ![pep8](https://user-images.githubusercontent.com/97538312/177018534-2c88db68-38be-48a0-a0af-33f88cfcdac5.jpg)

 
 
## Deployment
- The project is deployed to Heroku which is a cloud application platform , link : https://www.heroku.com
- First I created a new app within my account on Heroku.com 
 ![create_new_app](https://user-images.githubusercontent.com/97538312/177018312-f5f5d0fc-3fa9-4bf6-ab25-66f7f26c52d4.jpg)
 
 - Then in the settings I added 2 buildpacks in order, Python and then nodejs since it is part of the template provided.
 ![buildpack](https://user-images.githubusercontent.com/97538312/177018327-df74eafe-c0e3-4443-9ecb-fe68a783e9df.jpg)

 - The code was deployed and pushed to GitHub 
 
## Credits

 - I took inspiration for this project from the Code Institute video for Battleships
 - Some solutions to methods I found on stackoverflow and by referring back to pevious lessons

