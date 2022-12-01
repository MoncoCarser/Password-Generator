import random, os



numbers_list = ["0","1","2","3","4","5","6","7","8","9"]
letters_list = ["a","b","c","d", "e","f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
special_chars = ["!","#","$","&","%","/","@","[","]","?"]


def password_generator(maximum=19):
    os.system("clear")
    new_password = []
    while len(new_password) <= maximum:
            action = random.randint(0,3)
            if action == 0:
                item = random.choice(numbers_list)
                new_password.append(item)
            elif action == 1:
                item = random.choice(letters_list)
                new_password.append(item)
            elif action == 2:
                item = random.choice(letters_list).upper()
                new_password.append(item)
            else:
                item = random.choice(special_chars)
                new_password.append(item)
    print()
    for character in new_password:
        print(f"{character}", end="")
    print()

while True:
    give_password = input("Password contains a-z, A-Z, 0-9 and special characters (e.g. %).\n\nDo you want a 10 character password? (1)\n\nGenerate a password of any length (2)\n\n > ")
    if give_password == "1":
        password_generator(9)
        print()
    elif give_password == "2":
        try:
            length = int(input("How long do you want it to be: "))
            password_generator(length-1)
            print()    
        except:
            password_generator()
            print()

    

