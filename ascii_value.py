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



