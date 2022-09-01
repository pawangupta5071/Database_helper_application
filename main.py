from dbhelper import DBHelper


def main():
    db = DBHelper()
    while True:
        print("**********WELCOME**********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to Update user")
        print("PRESS 5 to exit program")
        print()

        try:
            choice = int(input())
            if (choice == 1):
                uid = int(input("Enter UserId: "))
                username = input("Enter UserName: ")
                userphone = input("Enter User Phone: ")
                db.insert_user(uid, username, userphone)

            elif choice == 2:
                db.fetch_all()

            elif choice == 3:
                userid = int(
                    input("Enter UserId to which you want to delete: "))
                db.delete_user(userid)

            elif choice == 4:
                userid = int(input("Enter UserId: "))
                newuserName = input("Enter new User Name: ")
                newphone = input("Enter new User Phone number: ")
                db.update_User(userid, newuserName, newphone)

            elif choice == 5:
                break

            else:
                print("Invalid Input ! Try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__ == "__main__":
    main()
