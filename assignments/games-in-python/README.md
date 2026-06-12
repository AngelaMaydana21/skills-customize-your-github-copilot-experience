 # 📘 Assignment: Hangman Game Challenge

 ## 🎯 Objective

 Build a Hangman game in Python to practice string manipulation, loops, conditionals, and user input. Students will implement a game loop that selects a secret word, accepts letter guesses, displays progress, and determines win/lose conditions.

 ## 📝 Tasks

 ### 🛠️	Implement the Hangman game

 #### Description
 Create a command-line Hangman game that randomly selects a word from a predefined list and lets a player guess letters until they either reveal the word or run out of attempts.

 #### Requirements
 Completed program should:

 - Randomly select a secret word from a predefined list
 - Accept single-letter guesses from the player and update displayed progress (e.g., `_ a _ _ m a n`)
 - Show the number of incorrect guesses remaining
 - Prevent counting repeated correct guesses as incorrect
 - End when the word is fully guessed or attempts reach zero
 - Display clear win or lose messages and reveal the secret word on loss

 #### Example
 ```
 Secret word: python
 Progress: _ _ _ _ _ _
 Guess: p
 Progress: p _ _ _ _ _
 ...
 ```
