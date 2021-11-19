#-----------------------------------------------------------------------------
# Name:         Alex ATM System Admin Viewer(AAS)
# Purpose:      To provide an ATM banking solution for businesses while 
#               demonstrating the use of sorting algorithms, search algorithms, 
#               classes, objects, inheritance, and abstract classes
#
# Author:      Alex Lu
# Created:     15-Nov-2021
# Updated:     17-Nov-2021
#-----------------------------------------------------------------------------

#Import
from account import Account
import json
import timeit
from algorithms import insertSort, binarySearch, linearSearch

#Initialize Database
with open("database.json") as f:
    data = json.load(f)

adminPass = "123"
objectData = []

for user in data["users"]:
    objectData.append( Account(user["name"], user["email"], user["username"], user["checking"], user["savings"], user["credit"], user["total"]) )

print("First 20:")
for user in objectData[:20]:
    print(user._total)

print("\nLast 20:")
for user in objectData[-20:]:
    print(user._total)


print(
    '''
    ===============Welcome to the Alex ATM System Administrator!===============
    \nPlease verify your credentials:
    '''
)
password = -1
while password != adminPass:
    password = input("Password: ")
    if password == adminPass:
        print("Login Verified")
    else:
        print("Login Failed")

choice1 = 0
while choice1 != -1:
    alphaSorted = False
    print(
        '''
        ===============What would you like to do?===============
        \nType 1 to sort users
        \nType 2 to edit users
        \nType 3 to create users
        \nType 4 to exit
        '''
    )
    choice1 = input("Enter your choice: ")

    if choice1 == "1":
        print(
        '''
        ===============What would you like to sort by?===============
        \nType 1 to sort users by username (ASCII)
        \nType 2 to sort users by total account balance 
        \nType 3 to sort users by checking account balance
        \nType 4 to sort users by savings account balance
        \nType 5 to sort users by credit account balance
        '''
        )
        choice1 = input("Enter your choice: ")
        if choice1 == "1":
            alphaSorted = True
            print("Processing...")
            objectData = insertSort(objectData, lambda a, b: a._user > b._user)
            print("Top 20:\n")
            for user in objectData[:20]:
                print(user._user + "\n")
            print("Bottom 20:\n")
            for user in objectData[-20:]:
                print(user._user + "\n")
        if choice1 == "2":
            print("Processing...")
            objectData = insertSort(objectData, lambda a, b: a._total > b._total)
            print("Lowest 20 Accounts:\n")
            for user in objectData[:20]:
                print(str(user._total) + "\n")
            print("Largest 20 Accounts:\n")
            for user in objectData[-20:]:
                print(str(user._total) + "\n")
        if choice1 == "3":
            print("Processing...")
            objectData = insertSort(objectData, lambda a, b: a._checkings > b._checkings)
            print("Lowest 20 Checking Accounts:\n")
            for user in objectData[:20]:
                print(str(user._checkings) + "\n")
            print("Largest 20 Checking Accounts:\n")
            for user in objectData[-20:]:
                print(str(user._checkings) + "\n")
        if choice1 == "4":
            print("Processing...")
            objectData = insertSort(objectData, lambda a, b: a._savings > b._savings)
            print("Lowest 20 Savings Accounts:\n")
            for user in objectData[:20]:
                print(str(user._savings) + "\n")
            print("Largest 20 Savings Accounts:\n")
            for user in objectData[-20:]:
                print(str(user._savings) + "\n")
        if choice1 == "5":
            print("Processing...")
            objectData = insertSort(objectData, lambda a, b: a._credit > b._credit)
            print("Lowest 20 Credit Accounts:\n")
            for user in objectData[:20]:
                print(str(user._credit) + "\n")
            print("Largest 20 Credit Accounts:\n")
            for user in objectData[-20:]:
                print(str(user._credit) + "\n")
    elif choice1 == "2":
        targetUser = input("Who would you like to edit? (Search by Username): ")
        if alphaSorted == True:
            index = binarySearch(objectData, targetUser, 0, len(objectData))
        else:
            index = linearSearch(objectData, targetUser)
        
        if index == -1:
            print("User does exist, please try again")
        else:
            name = input("Please enter the new name: ")
            email = input("Please enter the new email: ")
            username = input("Please enterthe new username: ")
            objectData[index].setName(name)
            objectData[index].setEmail(email)
            objectData[index].setUsername(username, objectData)
    elif choice1 == "3":
        username = input("Please enter a username: ")
        flag = linearSearch(objectData, username)
        if flag != -1:
            print("Username already exists, please try again")
        else:
            name = input("Please enter your name: ")
            email = input("Please enter your email: ")
            objectData.append( Account(name, email, username, 0, 0, 0, 0) )
    elif choice1 == "4":
        print("Thank you for banking with Alex ATM Systems. Bye!")
        choice1 = -1
