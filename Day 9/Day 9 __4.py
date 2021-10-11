bid_list = {}

def bidding():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    def silent_auction(name,bid):
        bid_list[name] = bid
    
    silent_auction(name,bid)    

    prompt_others = input("Are there others who want to bid 'Yes' or 'No'\n")
    prompt = prompt_others.lower()
    
    if prompt == "yes":
        bidding()
        
    elif prompt == "no":
        highest_bid = 0
        highest_bidder = ""
        
        for name in bid_list:
            
            if bid_list[name] > highest_bid:
                
                highest_bid = bid_list[name]
                highest_bidder = name
                
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
        
    else:
        
        print("Please choose 'Yes' or 'No'")
    
    
    
bidding()
#print(bid_list)

    
    

    
    