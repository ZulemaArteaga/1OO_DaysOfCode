# Who Has More Followers Game

## Table of Contents
- [About](#about)
- [Features](#features)
- [How to Use](#how-to-use)
- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)

## About
This is a guessing game where the player tries to determine which of two public figures has more followers.  

The game presents two options, and the player chooses either **A** or **B**. If the guess is correct, the score increases and the game continues with a new comparison. If the guess is wrong, the game ends.

## Features
- Randomly selects two public figures from a dataset.
- Displays each person's name, description, and country.
- Tracks your score as long as you guess correctly.
- Ends the game when you guess incorrectly.
- Handles draws if both have the same follower count.

## How to Use
1. Run the program.
2. View the two options:
   - **A**: Name, description, and country.
   - **B**: Name, description, and country.
3. Type `"A"` if you think **A** has more followers.
4. Type `"B"` if you think **B** has more followers.
5. The program will:
   - Increase your score if you guessed correctly.
   - End the game if you guessed incorrectly.
6. Continue playing until you make a wrong guess.

## Example
![higer_lower_project.gif](followers_game.gif)

## Requirements
- Python 3.12.2 

## Installation
1. Clone this repository:
```git clone https://github.com/ZulemaArteaga/1OO_DaysOfCode ```

2. Navigate to the project directory:
```cd 1OO_DaysOfCode/Day_14/Higher_or_Lower Project```

3. Run the program:
```python main.py```