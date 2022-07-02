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


1. `heroku/python`
2. `heroku/nodejs`


## Unfixed Bugs
## Debugging
## Testing
## Deployment
## Credits

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
