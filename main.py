import random, os, string



numbers_list = string.digits
letters_list = string.ascii_letters
special_chars = string.punctuation
all_chars = numbers_list + letters_list + special_chars

def password_generator(pre_set=19):
    os.system("clear")
    new_password = []
    while len(new_password) <= pre_set:
        item = random.choice(all_chars)
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

    

