# Blind Auction 
## Table of Contents
- [About](#about)
- [Features](#features)
- [How to Use](#how-to-use)
- [Example](#example)
- [Requirements](#requirements)
- [Installation](#installation)

## About
This program simulates a secret auction where multiple participants submit their bids anonymously. Each participant enters their name and bid amount. The program keeps collecting bids until there are no more participants, then determines and announces the highest bidder(s).

## Features
- Allows multiple participants to submit bids.
- Validates input for both names (alphabetical only) and bids (numeric).
- Supports multiple winners in case of a tie.
- Clears the console output between bidders to keep bids secret.
- Uses a dictionary to store bidder names and their corresponding bids.

## How to Use
1. Run the program.
2. When prompted, enter your name (letters only).
3. Enter your bid amount (numbers only).
4. Indicate if there are more bidders by typing "yes" or "no".
5. The program clears the screen between bidders to maintain secrecy.
6. After all bids are submitted, the program announces the winner(s) and their winning bid amount.

## Example
![auction.gif](auction.gif))

## Requirements
- Python 3.12.2 

## Installation
1. Clone this repository:
```git clone https://github.com/ZulemaArteaga/1OO_DaysOfCode ```

2. Navigate to the project directory:
```cd 1OO_DaysOfCode/Day_9/Blind\ Auction\ Project```

3. Run the program:
```python task.py```