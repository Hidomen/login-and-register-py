# CHALLENGES
    # add logout
    # add a csv datafile for userlist

user_list = {
    # "NAME" : "PASSWORD",
    "hidomen" : "123"

}


def main () :
    
    op = input("FOR LOGIN TYPE 'LOGIN' \nFOR REGISTER TYPE 'REGISTER'\n").upper()
    if op == "LOGIN" :
        login()
    elif op == "REGISTER" :
        register()


def login () :
    nickname = input("NICKNAME : ")
    password = input("PASSWORD : ")

    check_user(nickname, password)

def check_user (nickname,password) :
    if nickname in user_list and user_list[nickname] == password :
        print("WELCOME")


def register () :
    nickname = input("NICKNAME : ")
    password = input("PASSWORD : ")
    if nickname not in user_list :
        user_list.update({nickname : password})
        print("YOU SUCCESFULLY REGISTERED\n**************************")
        main()
    else :
        print("there is an already a user named", nickname)


main()

