# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }


# student_grades ={}

# for key in student_scores:
#     if 91 <= student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
#     elif 81 <= student_scores[key] < 91:
#         student_grades[key] = "Exceeds Expectation"
#     elif 71 <= student_scores[key] < 81:
#         student_grades[key] = "Acceptable"
#     else :
#         student_grades[key] = "Fail"

# print(student_grades)



# * my version
# bid_info = {}

# print("Welcome to the secret auction program. ")
# while True:
#     name = input("What is your name? ")
#     bid_amount = float(input("How much do you want to bid? $"))
#     last_item =  len(bid_info.keys()) and list(bid_info.items())[-1]
#     if len(bid_info.keys()) and bid_amount <= last_item[1]:
#         print(f"You need to bid higher than the last bid {last_item[1]}")
#     else:
#         bid_info[name] = bid_amount

#     cont = input("Do you want to continue bidding? Type 'yes' or 'no' ")
#     if cont.lower() != "yes":
#         break

# highest_bid = max(bid_info.values())
# result = next(
#     ({key: value} for key, value in bid_info.items() if value == highest_bid), None
# )

# name,bid = list(result.items())[0]

# print(f"The winner is {name} with the bid {bid}")


# * gpt version
# Auction Program
def get_highest_bidder(bids):
    """Find the highest bidder and their bid."""
    highest_bid = max(bids.values())
    winner = next(key for key, value in bids.items() if value == highest_bid)
    return winner, highest_bid

def secret_auction():
    """Conduct the secret auction."""
    print("Welcome to the secret auction program.")
    bids = {}
    while True:
        name = input("What is your name? ")
        bid_amount = float(input("How much do you want to bid? $"))

        if bids and bid_amount <= max(bids.values()):
            print(f"You need to bid higher than the current highest bid of ${max(bids.values())}")
        else:
            bids[name] = bid_amount

        cont = input("Do you want to continue bidding? Type 'yes' or 'no': ").strip().lower()
        if cont != 'yes':
            break
        print("\n" * 20)

    name, bid = get_highest_bidder(bids)
    print(f"\nThe winner is {name} with a bid of ${bid:.2f}")

# Run Auction
secret_auction()