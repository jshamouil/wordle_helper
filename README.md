# wordle_helper
web app designed to help a user solver world by calculating a list of words based on current and previous guesses


<h1>Wordle helper app overview:</h1>

<h2>summary:
the objective of this application is to assist the user in solving the wordle puzzle so that the user can visualize the pool of possible words the solution is in.

<h2>how to use the app:</h2>
first the user starts the wordle game by guessing the first word and receiving the output from the game which would be the color each letter is highlighted. Next the user needs to go to the wordle helper app entering in each letter into the respective box and selecting the color for each letter that the game gave. Once selected click enter and a list of recommended words will appear in the table below with the guess that was given. The user can then use one of the recommended words as their next guess in the wordle game. After the user enters in their second guess to the game they would then switch back to the wordle helper app and enter in the letters and colors and click enter. A new row will appear in the table with a smaller list of recommended guesses. This process can go on until the user selects the correct word in the game.

<h2>how it works:</h2>
the wordle helper application has a word back containing over 2000 words that are considered possible solutions to wordle directly scraped from the wordle site. When the user makes the input into the app I collect each letter along with the color and do the following:

<h2>create 2 sets:</h2>
 - out words: set containing all words that contain all rejected words
 - in words: set containing all words that contain all accepted words

we do this because a word can contain the same letter twice, one that is yellow and one that is grey. We then parse through the letters in the guessed word:

 - green letters: add each word to "in words" for each word that contains the green letter in the position found in the guess
 - grey letters: add each word to "out words" for each word that contains the grey letter in any position
 - yellow letters: add each word to "out words" for each word that the letter appears in any other position except the one in the guessed letter

lastly we create a set that contains all "in words" and excludes all "out words" and disply those words in the table. we then query the table for the latest set of words to use as the word bank for the next guess to take into account the previous guesses
