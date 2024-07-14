"""A string is simply a series of characters.
 Anything inside quotes is considered a string in Python,
 and you can use single or double quotes around"""

#A string is an arraya of characters
note="I am doing the Fellowship of Data Science!" #this is a string

#2-3. personal message 
name="Naruto"
print(f"Hello {name}, Would you like to learn some python today!")

#2-4. Name cases
p_name="Ronaldo cr7"
print(p_name.lower()) #lowercase
print(p_name.upper()) #uppercase
print(p_name.title()) #title is used to make the first letter of every word capital
print(p_name.capitalize()) #it is used to make the first letter of sentance capital

#2-5. print a Famous Quote
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

#2-6. Famous Quote 2: Repeat Exercise 2-5
famous_person="Albert Einstein"
message=f'{famous_person} onec said, "A person who never made a mistake never tried anything new."'

print(message)

#2-7. Stripping Names
Name="\tBilal     "
print(Name)
print(Name.lstrip()) #To remove left side white spaces
print(Name.rstrip()) #To Remove right side White spaces
print(Name.strip()) #To Remove both side white spaces


#2-8. Number Eight
print(3+5) #addition to print number 8
print(10-2) #substraction to print number 8
print(4*2) #multiplication to print number 8 
print(16//2) #division to print number 8 #it will be floor division

#2-9. Favorite Number
fav_num=7
message=f"My Faviorte number is {fav_num}"
print(message)

import this #this the Zen of python 