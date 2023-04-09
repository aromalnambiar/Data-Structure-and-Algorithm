def card_game(cards, query):
    
    # Create a variable position with the value 0    
    position = 0
    
    #print cards and query 
    print("cards : " , cards)
    print("query : ", query)
    
    # Set up a loop for repetition
    while True:
        
        #print the position
        print("position : ", position)
        
        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! 
            print("\nAnwser is ", position)
            return position
        
         # If its not the position then increment the position
        position += 1
        
        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1
        

#funtion calling
card_game([13, 11, 10, 7, 4, 3, 2, 1, 0], 7)