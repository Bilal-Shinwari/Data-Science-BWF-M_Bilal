# 5-8. Hello Admin
usernames=["admin","naruto","bilal","rohail"]

for i in usernames:
    if i=="admin":
        print(f"Hello {i}, would you like to see a status report?")
    else:
        print(f"Hello {i},thank you for loging in again!")

print()
# 5-9. No Users
usernames.clear()

if usernames:
    for i in usernames:
        if i=="admin":
            print(f"Hello {i}, would you like to see a status report?")
        else:
            print(f"Hello {i},thank you for loging in again!")
else:
    print("We need to find users!")

print()
# 5-10. Checking Usernames 

current_users=["bilal","naruto","rohail","ayaz","sufyan"]
new_users=["hassan","rohail","sufyan","uzair","sanaullah"]

for i in new_users:
    if i.lower() in current_users:
        print("Will need to enter new username") 
    else:
        print("The username is available")

print()
# 5-11. Ordinal Numbers
nums=[1,2,3,4,5,6,7,8,9]

for i in nums:
    if i==1:
        print("1st")
    elif i==2:
        print("2nd")
    elif i==3:
        print("3rd")
    else:
        print(f"{i}th")