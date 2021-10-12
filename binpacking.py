# First fit heuristic for bin packing.

# Strategy:
# Open first bin
# for each item:
#    for each open bin:
#       check if item fits in bin.
#       True: place it, move on to next item.
#       False: keep looping over bins.
#    if item still not placed:
#       open new bin, place item in new bin.



def first_fit(item_list, bin_capacity):
    '''
    First fit heuristic for bin packing.
    
    Input:
        item_list, a list of item sizes/volumes
        bin_capacity, a positive number to indicate the size
            of an empty bin.
    
    Output:
    '''
    
    # Open first bin
    bin_list = [0]
    
    # Loop over each item
    for item in item_list:
        
        # Flag to check if item is placed
        placed = False
        
        # Loop over each currently open bin
        for i in range(len(bin_list)):
            
            # Check if item fits in bin
            if item <= bin_capacity - bin_list[i]:
                # Place the item
                bin_list[i] += item
                placed = True
                break
        
        # If item was not placed, open a new bin
        if not placed:
            bin_list.append(item)
    
    return bin_list



# Test the function
item_list = [20] * 15     # [20, 20, 20, ...]
bin_capacity = 50

result = first_fit(item_list, bin_capacity)
print(result)