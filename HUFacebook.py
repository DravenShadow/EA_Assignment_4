import sys

from sList import sList

hu_book = {}

def default_list_load():
    friend_list_1 = sList()
    friend_list_2 = sList()
    friend_list_3 = sList()
    friend_list_4 = sList()

    friend_list_1.add_Front("derek")
    friend_list_2.add_Front("zacks beard")
    friend_list_3.add_Front("rowland")
    friend_list_4.add_Front("zack")

    hu_book["rowland"] = friend_list_1
    hu_book["derek"] = friend_list_3
    hu_book["zack"] = friend_list_2
    hu_book["zacks beard"] = friend_list_4


def create_user():
    friends_list = sList()
    username = validate_username(raw_input('Enter in a username: \n'))
    hu_book[username] = friends_list


def add_friend(username, friend):
    if validate_user(friend):
        hu_book[username].add_Front(friend)
        hu_book[friend].add_Front(username)
    else:
        print("Error! Could not complete action!")


def remove_friend(username, friend):
    if validate_user(friend):
        hu_book[username].remove(friend)
        hu_book[friend].remove(username)
    else:
        print("Error! Could not complete action!")


def validate_user(name):
    try:
        hu_book[name]
        return True
    except KeyError:
        return False


def validate_username(username):
    if not validate_user(username):
        pass
    else:
        while validate_user(username):
            print("INVALID USERNAME!  USERNAME ALREADY IN USE!")
            username = raw_input("Enter in a new username: \n")
    return username


def print_users():
    user_list = []
    for x in range(len(hu_book)):
        user_list.append(hu_book.items()[x][0])
    print(user_list)


def print_friends_list(username):
    if validate_user(username):
        print(str(hu_book[username]))
    else:
        print("No user by that name!")


def main():
    cont = True
    print(
        "Welcome to the HU Facebook Program!\nDo ou wish to create or login?")
    user_input = raw_input("[login/create]?\n")
    if user_input.lower() == "create":
        create_user()
    elif user_input.lower() == "login":
        default_list_load()
    else:
        print("Invalid Option!  Good-Bye!\nTerminating program")
        sys.exit()

    print("HU Facebook Main Page")
    while cont:
        print(
            "Do you wish add a friend, remove a friend, print a list of users or print a specific user's friends list...")
        user_input = raw_input("[add/remove/user/friends]?\n")

        if user_input.lower() == "add":
            user = raw_input("Enter in your username:")
            new_friend = raw_input("Enter in friends name:")
            add_friend(user, new_friend)

            user_cont = raw_input("Do you wish to continue?[Y/N]\n")
            if user_cont.lower() == "n":
                cont = False
            else:
                pass
        elif user_input.lower() == "remove":
            user = raw_input("Enter in your username:")
            new_friend = raw_input("Enter in ex-friends name:")
            remove_friend(user, new_friend)

            user_cont = raw_input("Do you wish to continue?[Y/N]\n")
            if user_cont.lower() == "n":
                cont = False
            else:
                pass
        elif user_input.lower() == "user":
            print_users()
            user_cont = raw_input("Do you wish to continue?[Y/N]\n")
            if user_cont.lower() == "n":
                cont = False
            else:
                pass
        elif user_input.lower() == "friends":
            user = raw_input("Enter in the username to see their fiends list:")
            print_friends_list(user)
            user_cont = raw_input("Do you wish to continue?[Y/N]\n")
            if user_cont.lower() == "n":
                cont = False
            else:
                pass
        else:
            print("Invalid Option!")


if __name__ == '__main__':
    main()
