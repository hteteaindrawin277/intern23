import math
def jump_search(list,key):
    print("Entering Jump Search")
    n = len(list)                          # Length of the array
    m = int(math.sqrt(n))               # Step length
    i = 0                               # Starting interval
    while i != len(list)-1 and list[i] < key:

        if list[i+m-1] == key:            # Found the search key
            return i+m-1
        elif list[i+m-1] > key:           # Linear search for key in block
            B = list[i: i+m-1]
            return linear_search(B, key, i)
        i += m
    B = list[i:i+m]                        # Step 5
    print("Processing Block - {}".format(B))
    return linear_search(B, key, i)
def linear_search(B, key, loc):
    print("Entering Linear Search")
    i = 0
    while i != len(B):
        if B[i] == key:
            return loc+i
        i += 1
    return -1
print(jump_search(list,sum))