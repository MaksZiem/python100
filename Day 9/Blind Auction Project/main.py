from art import logo
print(logo)

# TODO-1: Ask the user for input

def highest_bid(bids):
    win_big = 0
    winner = ""
    for bid in bids:
        print(bid)
        if bids[bid] > win_big:
            winner = bid
            win_big = bids[bid]

    print("winner: ", winner)
    print("win bid: ", win_big)
    print(bids)

bids_ends = False
bids = {}
while bids_ends == False:
    name = input("what is your name?: ")
    bid =  int(input("What is your bid?: $"))
    bids[name] = bid
    end = input("End?")

    if end == "tak":
        highest_bid(bids)
        bids_ends = True




