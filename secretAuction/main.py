bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Congratulations {winner} with a bid of ${highest_bid}")


should_continue = True

print("Welcome to the silent auction!\n")
while should_continue:
    name = input("What is your name?\n")
    person_bid = input("What is your bid?\n")
    bids[name] = person_bid

    repeat = input("Is there another person waiting to bid? Type Y or N\n").lower()
    if repeat == "n":
        should_continue = False
        find_highest_bidder(bids)
        