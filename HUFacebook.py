"""
        HUFacebook.py                   Author: Rowland DePree

        A program to demonstrate the use of link lists and dictionary in the form of a Facebook like application.
        The user can add new users, add friends, remove friends, print out a list of all users, and print out all
        friends of particular user.
"""
import sys

from sList import sList

hu_book = {}


def default_list_load():
    """
    A method to load in a default set of users and friends to use

    :return None
    """
    friend_list_1 = sList()
    friend_list_2 = sList()
    friend_list_3 = sList()
    friend_list_4 = sList()

    friend_list_1.add_Front("derek")
    friend_list_2.add_Front("zack's beard")
    friend_list_3.add_Front("rowland")
    friend_list_4.add_Front("zack")

    hu_book["rowland"] = friend_list_1
    hu_book["derek"] = friend_list_3
    hu_book["zack"] = friend_list_2
    hu_book["zack's beard"] = friend_list_4


def create_user():
    """
    Add a new user to the dictionary with an empty friends list

    :return None
    """
    friends_list = sList()
    username = validate_username(raw_input('Enter in a username: \n'))
    hu_book[username] = friends_list


def add_friend(username, friend):
    """
    Adds a friend to both the user's friends list and then adds the user to the friend's friend list.

    :return None
    """
    if validate_user(friend):
        hu_book[username].add_Front(friend)
        hu_book[friend].add_Front(username)
    else:
        print("Error! Could not complete action!")


def remove_friend(username, friend):
    """
    Removes a friend to both the user's friends list and then adds the user to the friend's friend list.

    :return None
    """
    if validate_user(friend):
        hu_book[username].remove(friend)
        hu_book[friend].remove(username)
    else:
        print("Error! Could not complete action!")


def validate_user(name):
    """
    Checks to see if the username already exists in the dictionary or not

    :param name
    :return True or False
    """
    try:
        hu_book[name]
        return True
    except KeyError:
        return False


def validate_username(username):
    """
    Validates the username against the dictionary to make sure it doesn't already exist.  If it does, then it will force
    the user to use a different username.

    :param username
    :return username
    """
    if not validate_user(username):
        pass
    else:
        while validate_user(username):
            print("INVALID USERNAME!  USERNAME ALREADY IN USE!")
            username = raw_input("Enter in a new username: \n")
    return username


def print_users():
    """
    Prints a list of all usernames

    :return None
    """
    user_list = []
    for x in range(len(hu_book)):
        user_list.append(hu_book.items()[x][0])
    print(user_list)


def print_friends_list(username):
    """
    Prints out lal friends of a particular user

    :param username
    :return None
    """
    if validate_user(username):
        print(str(hu_book[username]))
    else:
        print("No user by that name!")


def main():
    """
    Main method of the program.  Also is the UI for it as well.

    :return None
    """
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


"""
    Starts the main method
"""
if __name__ == '__main__':
    main()
