""" Secret Auction Program
Functionality:
- Each person writes their name and bid.
- The program asks if there are others who need to bid.
    If so, then the computer clears the output (prints several blank lines)
    then loops back to asking name and bid.
- Each person's name and bid are saved to a dictionary.
- Once all participants have placed their bid, the program works out who has the highest bid and prints it."""

def secret_auction_game():
    end_bids = False
    name_bid = {}

    while not end_bids:
        # Input: name
        name = input("What is your name?\n").upper()
        if not name.isalpha():
            print("INVALID OPTION. Please enter a valid name with alphabet letters.")
            continue # If the input is not a letter it will enter this loop again

        # Input: bid
        try:
            bid = float(input("What is your bid?\n$"))
        except ValueError:
            print("INVALID OPTION. Please enter a number.")
            continue # If the input is not a float-number it will enter this loop again

        name_bid[name] = bid # Adds name and bid to dictionary if both inputs are valid

        # Input: More bidders
        while True:
            more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
            if more_bidders not in ["yes", "no"]:
                print("INVALID OPTION. Type: yes or not")
            if  more_bidders == "yes":
                break # If more bidders are playing, it will break this loop
            elif more_bidders == "no": # If no more bidders. The bidding game ends
                end_bids = True
                break
        print("\n" * 1000) # Just adding many spaces to leave prints out if sight

    # The winner is the one with the max bid
    winner_name = max(name_bid, key=name_bid.get)  # name_bid.get brings the value (bid) for each bidder(key)
    winning_bid_amount = name_bid[winner_name] # This brings the bid amount per winner name

    # Creating a list of winners in case that is more than one winner
    winners = []
    for name, bid in name_bid.items():
        if bid == winning_bid_amount:
            winners.append(name)

    if len(winners) > 1: # If more than one winner, a list of winners will be created
        winner_list = ', '.join(winners)
        print(f'The winners are "{winner_list}" with a bid of ${winning_bid_amount}.')
    else: # If only one winner, will print the winner name
        print(f'The winner is "{winners[0]}" with a bid of ${winning_bid_amount}.')

secret_auction_game()