import bubblesort

def link():
    list = []
    email_list = []
    index = 0
    while index<4:
        
        name = input("please enter email:")
        name_length = len(name)
        count = 0
        for K in name:
            ASCII = ord(K)
            count += ASCII
        index += 1
        list.append(count)
        email_list.append(name)
    #index += 1
    sort_list = bubblesort.bubblesort(list)
    print(sort_list)
    print(bubblesort.bubblesort(email_list))

    search = input('Enter search name:')
    num = 0
    for i in range(len(search)):
        num += ord(search[i])
    print(num)

    import math
    def jump_search(A, item):
        print("Entering Jump Search")
        n = len(A)  # Length of the array
        m = int(math.sqrt(n))  # Step length
        i = 0  # Starting interval

        while i != len(A) - 1 and A[i] < item:

            if A[i + m - 1] == item:
                return i + m - 1
            elif A[i + m - 1] > item:
                B = A[i: i + m - 1]
                return linear_search(B, item, i)
            i += m
        B = A[i:i + m]  # Step 5
        print("Processing Block - {}".format(B))
        return linear_search(B, item, i)

    def linear_search(B, item, loc):
        print("Entering Linear Search")
        i = 0
        while i != len(B):
            if B[i] == item:
                return loc + i
            i += 1
        return -1

    print(jump_search(list,num))

