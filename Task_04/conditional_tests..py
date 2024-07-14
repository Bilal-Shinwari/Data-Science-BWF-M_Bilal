#5-1. Conditional Tests

#Test 1
car = "corolla x"
print("Is car == 'corolla x'? I predict True.")
print(car == 'corolla x')
#Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#Test 3
num = 7
print("\nIs Num == 7 ? I predict True.")
print(num == 7)
#Test 4
print("\nIs Num == 10 ? I predict False.")
print(num == 10)

#Test 5
num > 5
print("\nIs Num > 5 ? I predict True.")
print(num == 7)
#Test 6
print("\nIs Num > 5 ? I predict False.")
print(num == 2)


#Test 7
Name="Naruto"
print("\nIs Name length == 6 ? I predict True.")
print(len(Name) == 6)
#Test 8
print("\nIs Name length == 7  ? I predict False.")
print(len(Name) == 7)

#Test 9
languges=["Python","C++","Java"]
print("\nIs Python present in languges list ? I predict True.")
print("Python" in languges)
#Test 10
print("\nIs C# present in languges list  ? I predict False.")
print("c#" in languges)


#5-2. More Conditional Tests
languges=["Python","C++","Java"]
print("\nIs Python is not present in languges list ? I predict False.")
print("Python" not in languges)

#with and and or keyword
print("\nIs Python  and C# present in languges list ? I predict False.")
print("Python" in languges and "C#" in languges)

print("\nIs Python  or C# present in languges list ? I predict True.")
print("Python" in languges or "C#" in languges)


name="naruto"
print("\nIs naruto in lowercase ? I predict True.")
print("naruto" == name.lower())

print("\nIs naruto in uppercase ? I predict False.")
print("naruto" == name.upper())
