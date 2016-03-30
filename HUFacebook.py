import sys

hu_book = {}


class Node():
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node


class sList:
    def __init__(self):
        self.head_node = None
        self.size = 0

    def __str__(self):
        output = []
        curr = self.head_node
        while curr is not None:
            output.append(str(curr.data, ))
            curr = curr.next
        return ' ,'.join(output)

    def add_Front(self, data):
        self.head_node = Node(data, self.head_node)
        self.size += 1

    def remove(self, data):
        if self.size == 0:
            return False
        elif self.head_node.data == data:
            self.head_node = self.head_node.next
            self.size -= 1
            return True
        else:
            curr = self.head_node
            while curr.next is not None and curr.next.data != data:
                curr = curr.next
            if curr.next is None:
                return False
            else:
                curr.next = curr.next.next
                self.size -= 1
                return True

    def return_node(self, index):
        if index < 0 or self.head_node is None:
            return None
        elif index == 0:
            return self.head_node
        else:
            self.head_node = self.head_node.next
            return self.return_node(index - 1)


def default_list_load():
    friend_list_1 = sList()
    friend_list_2 = sList()
    friend_list_3 = sList()
    friend_list_4 = sList()

    friend_list_1.add_Front("derek")
    friend_list_2.add_Front("zack jr.")
    friend_list_3.add_Front("rowland")
    friend_list_4.add_Front("zack")

    hu_book["rowland"] = friend_list_1
    hu_book["derek"] = friend_list_3
    hu_book["zack"] = friend_list_2
    hu_book["zack jr."] = friend_list_4


def create_user():
    friends_list = sList()
    username = validate_username(raw_input('Enter in a username: '))
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
            username = raw_input("Enter in a new username: ")
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
        user_input = raw_input("[add/remove/user/friends]?")

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
