#5-3. Alien Colors #1: if satatment

Alien_color="red"
if Alien_color=="red":
    print("The player just earned 5 points.")

if Alien_color =="green":
    print("The player just earned 5 points.")

#5-4. Alien Colors #2: if-else
if Alien_color=="red":
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

if Alien_color=="green":
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")


#5-5. Alien Colors #3: if-elif
Alien_color="red"

if Alien_color == "red":
    print("The player just earned 15 points.")
elif Alien_color =="green":
    print("The player just earned 5 points.")
elif Alien_color == "yellow":
    print("The player just earned 10 points.")

Alien_color="green"
if Alien_color == "red":
    print("The player just earned 15 points.")
elif Alien_color =="green":
    print("The player just earned 5 points.")
elif Alien_color == "yellow":
    print("The player just earned 10 points.")

Alien_color="yellow"
if Alien_color =="red":
    print("The player just earned 15 points.")
elif Alien_color =="green":
    print("The player just earned 5 points.")
elif Alien_color == "yellow":
    print("The player just earned 10 points.")

# 5-6. Stages of Life
age=23
if age<2:
    print("The person is a baby")
elif age>=2 and age<4:
    print("The person is toddler")
elif age>=4 and age<13:
    print("The person is a kid")
elif age>=13 and age<20:
    print("The person is a teenager")
elif age>=20 and age<65:
    print("The person is an adult")
elif age>=65:
    print("The person is an elder")

# 5-7. Favorite Fruit
fav_fruits=["Watermelon","Orange","Mango"]
if "Banana" in fav_fruits:
    print("You really like Bananas!")

if "Watermelon" in fav_fruits:
    print("You really like Watermelons!")

if "Melon" in fav_fruits:
    print("You really like Melons!")

if "Mango" in fav_fruits:
    print("You really like Mangoes!")

if "Orange" in fav_fruits:
    print("You really like Oranges!")