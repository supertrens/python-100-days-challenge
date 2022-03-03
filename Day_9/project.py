def get_bid():
  new_bid = {}
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")
  
  new_bid[name] = int(bid)
  return new_bid

def is_more_bid():
  more_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if(more_bidder == "yes"):
    return True
  return False

def get_winner(bids):

  bid_values = bids.values()
  bid_names = bids.keys()
  
  max_bid = bid_values[0]
  winner = bid_names[0]
  
  for index, bid in enumerate(bid_values):
    print("HERE" + index)
    if(bid > max_bid):
      max_bid = bid
      # winner = 
      
  return {"name" : winner, "bid" : max_bid}
    

bids = []
continue_bidding = True

while(continue_bidding):
  new_bid = get_bid()
  bids.append(new_bid)
  continue_bidding = is_more_bid()
  
winner = get_winner(bids)
print(f"The winner is {winner['name']} with a bit of ${winner['bid']}")