import random
import string
import json

dict = {}
for i in range(10):
    # create email
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 12)))
    mname = f"{username}@gmail.com"
    # print(name)
    user = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, 12)))
    name = f"{user}"

    # create password
    password = ''.join(random.choice(string.printable) for i in range(8))


    # print(password)

    # create phone
    def random_phone_num_generator():
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = (str(random.randint(1, 9998)).zfill(4))
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))
        return '{}-{}-{}'.format(first, second, last)


    num = random_phone_num_generator()

    # print(num)
    dict.update({
        len(dict): {"email":mname,"username":name,"password":password,"phone":num}
    })
print(dict)
f = open('savedata.json', 'w')
f.write(json.dumps(dict))
f.close()
