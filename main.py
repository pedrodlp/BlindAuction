from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bid_dict = {}
add_bidder = "yes"

def add_bid(namef, bidf,):
  bid_dict[namef] = bidf  

while add_bidder == "yes":
  clear()
  print(logo)
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  add_bid(name, bid)
  add_bidder = input('Are there any other bidders? Type "yes" or "no".\n')

clear()
print(logo)
topbid = 0
winner = ""
for key in bid_dict:
   compare_val = bid_dict[key]
   if compare_val > topbid:
     topbid = compare_val
     winner = key

print(f"The winner is {winner} with a bid of ${topbid}.")
