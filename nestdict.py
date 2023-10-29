import os
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidders in bidding_record:
    bid_amount = bidding_record[bidders]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidders
  print(f"The winner is {winner} with a bid of ${highest_bid}.")
  
  
  
while not bidding_finished:
  name = input("What is your name: \n")
  price = int(input("Give your Bidding price: $"))
  bids[name] = price
  should_continue = input ("Are there any others bidders? Type 'yes' or 'no'. \n ")
  
  if should_continue == "no":
    bidding_finished = True
    clear_console()
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear_console()
  
  
  