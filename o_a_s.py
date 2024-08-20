class Auction:
    def __init__(self, item_name, starting_bid, auctioneer):
        self.item_name = item_name
        self.current_bid = starting_bid
        self.highest_bidder = None
        self.auctioneer = auctioneer
        self.is_active = True

    def place_bid(self, bidder_name, bid_amount):
        if not self.is_active:
            return f"Auction for {self.item_name} is closed."
        
        if bid_amount > self.current_bid:
            self.current_bid = bid_amount
            self.highest_bidder = bidder_name
            return f"Bid placed successfully! Current highest bid: {self.current_bid} by {self.highest_bidder}"
        else:
            return f"Your bid must be higher than the current bid of {self.current_bid}."

    def close_auction(self):
        self.is_active = False
        if self.highest_bidder:
            return f"{self.item_name} sold to {self.highest_bidder} for {self.current_bid}."
        else:
            return f"Auction closed! No bids were placed on {self.item_name}."


class OnlineAuctionSystem:
    def __init__(self):
        self.auctions = []

    def create_auction(self, item_name, starting_bid, auctioneer):
        new_auction = Auction(item_name, starting_bid, auctioneer)
        self.auctions.append(new_auction)
        return f"Auction created for {item_name} starting at $ {starting_bid}."

    def bid_on_auction(self, auction_index, bidder_name, bid_amount):
        if 0 <= auction_index < len(self.auctions):
            return self.auctions[auction_index].place_bid(bidder_name, bid_amount)
        else:
            return "Invalid auction index."

    def close_auction(self, auction_index):
        if 0 <= auction_index < len(self.auctions):
            result = self.auctions[auction_index].close_auction()
            self.auctions.pop(auction_index)  # Remove the auction after it's closed
            return result
        else:
            return "Invalid auction index."

    def list_auctions(self):
        auction_list = []
        for index, auction in enumerate(self.auctions):
            status = "Open" if auction.is_active else "Closed"
            auction_list.append(f"{index}: {auction.item_name} (Highest bid: {auction.current_bid}) - {status}")
        return auction_list

    def show_menu(self):
        while True:
            print("\nOptions:")
            print("1. Sell")
            print("2. Buy")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                item_name = input("Enter the name of the item: ")
                starting_bid = float(input("Enter the starting bid amount: "))
                auctioneer = input("Enter your name (Auctioneer): ")
                print(self.create_auction(item_name, starting_bid, auctioneer))
            elif choice == "2":
                print("\nCurrent Auctions:")
                auctions = self.list_auctions()
                if auctions:
                    for auction in auctions:
                        print(auction)
                    auction_index = int(input("Enter the index of the auction you want to bid on: "))
                    bidder_name = input("Enter your name (Bidder): ")
                    bid_amount = float(input("Enter your bid amount: "))
                    print(self.bid_on_auction(auction_index, bidder_name, bid_amount))

                    # Close auction if user confirms
                    close = input("Do you want to close the auction? (yes/no): ").lower()
                    if close == "yes":
                        print(self.close_auction(auction_index))
                else:
                    print("No auctions available.")
            elif choice == "3":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")


# Running the Online Auction System
system = OnlineAuctionSystem()
system.show_menu()
