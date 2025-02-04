import time as t

username_list = ["admin", "aaa", "coding"]
password_list = ["admin", "112233", "python"]

in_use = True
while in_use:
    print("initialize login system ...")
    t.sleep(2)
    print("login system is ready for use.")
    fail_cnt = 0
    success  = False
    username = ""
    while True:
        a = input("please enter username: ")
        b = input("please enter password: ")
        if a in username_list:
            i = username_list.index(a)
            p = password_list[i]
            if b == p:
                print("login successfully.")
                success  = True
                username = a
                break
            else:
                fail_cnt += 1
        else:
            fail_cnt +=1    
        if fail_cnt < 3:
            print("invalid username or password, please try again.")
        else:
            print("login terminated.")
            in_use = False
            break
            
    if success:
        while True:
            if username == "admin":
                t.sleep(1)
                print("========================================")
                print(" - 1. display username and password list")
                print(" - 2. add new user account")
                print(" - 3. change admin password")
                print(" - 4. change user password")
                print(" - 5. delete user account")
                print(" - 0. logout")
                option = int(input("choose your option:"))
                if option == 0:
                    print("logout, bye-bye.\n")
                    break
                elif option == 1:
                    print ("username list:", username_list)
                    print ("password list:", password_list)
                elif option == 2:
                    a = input("please enter new username: ")
                    if a in username_list:
                        print("username \"%s\" already exists."%a)
                    else:
                        b = input("please enter new password: ")
                        username_list.append(a)
                        password_list.append(b)
                elif option == 3:
                    b = input("please enter new admin password: ")
                    i = username_list.index(username)
                    password_list[i] = b
                elif option == 4:
                    a = input("please enter the username: ")
                    if a in username_list:
                        b = input("please enter new password for \"%s\": "%a)
                        i = username_list.index(a)
                        password_list[i] = b
                    else:
                        print("username \"%s\" does not exist."%a)
                elif option == 5:
                    a = input("please enter the username to be deleted: ")
                    if a == "admin":
                        print("warning! can not delete admin account!")
                    elif a in username_list:
                        choice = input("are you sure to delete account \"%s\"?(y/n): "%a)
                        if choice == "y" or choice == "Y":
                            i = username_list.index(a)
                            username_list.pop(i)
                            password_list.pop(i)
                    else:
                        print("username \"%s\" does not exist."%a)
                else:
                    print("invalid choice, please try again")
            else:
                t.sleep(1)
                print("========================================")
                print(" - 1. display your username and password")
                print(" - 2. change your password")
                print(" - 3. delete your account")
                print(" - 0. logout")
                option = int(input("choose your option:"))
                if option == 0:
                    print("logout, bye-bye.\n")
                    break
                elif option == 1:
                    i = username_list.index(username)
                    print ("your username:", username_list[i])
                    print ("your password:", password_list[i])
                elif option == 2:
                    b = input("please enter your new password: ")
                    i = username_list.index(username)
                    password_list[i] = b
                elif option == 3:
                    choice = input("are you sure to delete your account?(y/n): "%a)
                    if choice == "y" or choice == "Y":
                        i = username_list.index(username)
                        username_list.pop(i)
                        password_list.pop(i)
                else:
                    print("invalid choice, please try again")
