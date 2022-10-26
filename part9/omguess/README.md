```
   ____  __  ___   ______
  / __ \/  |/  /  / ____/_  _____  _____________  _____
 / / / / /|_/ /  / / __/ / / / _ \/ ___/ ___/ _ \/ ___/
/ /_/ / /  / /  / /_/ / /_/ /  __(__  |__  )  __/ /
\____/_/  /_/   \____/\__,_/\___/____/____/\___/_/

```

# OMGuesser - my final project for CS50P
## Video Demo:
https://youtu.be/ZC2-iMuv2ms
## Description:
As a football fan, I thought that I want to create a project that somehow touches upon this subject. An inspiration came from an awesome Twitter account called [The Wikipedia Footballers Quiz](https://twitter.com/WikiBallersQuiz). It posts daily riddles, in which a screenshot of a football player's career from Wikipedia is all that you have to guess the name of the player. I decided to do something similar, but covering only the former and current players of my favorite team - Olympique de Marseille.
## Flow
The programme starts with prompting the user if they want to update the database. As it takes some time (around 2 minutes), I decided to make it optional, as it's not as important (majority of players are retired).

If the user decides to update the database, it starts the scraping process. Using the BS4 module, the programme loops through the list of players that are hardcoded (200 entries), accesses each one's Wikipedia profile and looks for the infobox, where the data about their career is stored (marked in yellow):

![Wikipedia screenshot](wiki-screenshot.png)

After locating the infobox, it goes through each row to determine the first one and the last one in which the information on senior career of a given player is stored. Then it writes this data to a dictionary of all the players, which is saved in a json file.

After updating the database, the game itself plays out. The programme selects a player randomly, displays his career on the screen (using the json file) and asks the user for the answer. It is case insensitive and accent insensitive (as there are players with accented letters that would be cumbersome to write down). If the guess is correct, the current score is displayed and the player may move on the next one. If not, the game ends.

## TODO - ideas for the future:

I had LOTS of fun doing this project, and learnt a lot - and during that I came up with a long list of things to do differently and ideas for improvement. Some of them are:
- Rewriting the code with OOP, so it would be more flexible and open for improvements.
- Using Selenium instead of BS4, as it's more flexible and allows better handling of exceptions (for example when there is more than one player with a given name).
- Moving the programme to a web environment, so it could be possible to easily play it in a browser.
- Changing logic for the game - instead of guessing all 200 players, do rounds of 10, with no game over after a bad guess.
- Currently the list of players is hardcoded. It would be cool if the user could specify the seasons they want to include, and then the programme would scrape the Internet to make a game library consisiting of the players from that season.
- Similarly, would be awesome if other football teams would be included - that's a lot of new exceptions coming in, I guess.

## Contact

If you have any questions, feel free to reach out to me at ptktmsz@gmail.com. Thanks!