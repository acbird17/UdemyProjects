import os
def clear():
    os.system('clear')

bids = {}
bidding_finished = False

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}.")

while not bidding_finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    bids_continue = input("Are there any other bidders, type 'yes' or 'no': ")
    if bids_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif bids_continue == "yes":
        clear()
