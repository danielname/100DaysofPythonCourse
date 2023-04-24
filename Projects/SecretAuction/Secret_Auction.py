import art
print(f"{art.logo}\nWelcome to the secret auction pregram.")
bids = 1
auction = []
while bids > 0:
    new_bid = {}
    new_bid["name"] = input("What is your name?\n")
    new_bid["bid"] = int(input("What is your bid?\n"))
    more = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    if not more == "yes":
        bids -= 1
    auction.append(new_bid)
high_bidder = ""
high_bid = 0
for bidder in auction:
    if bidder["bid"] > high_bid:
        high_bid = bidder["bid"]
        high_bidder = bidder["name"]
print(f"The winner is {high_bidder} with a bid of ${high_bid}")