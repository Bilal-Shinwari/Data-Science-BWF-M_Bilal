#9.1 Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance called restaurant
restaurant = Restaurant("The Great Panda", "Chinese")
print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#9.2 Three Restaurant
# Using the Restaurant class from above

# Creating three different instances
restaurant1 = Restaurant("Pizza Hut", "Italian")
restaurant2 = Restaurant("Sushi Palace", "Japanese")
restaurant3 = Restaurant("Spice Route", "Indian")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9.3 User
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

# Creating instances representing different users
user1 = User("John", "Doe", "johndoe", "john.doe@email.com", "New York")
user2 = User("Alice", "Smith", "asmith", "alice.smith@email.com", "Los Angeles")
user3 = User("Bob", "Johnson", "bjohnson", "bob.johnson@email.com", "Chicago")

# Calling both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()



#9.4 Number Served 
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

# Creating an instance called restaurant
restaurant = Restaurant("The Great Panda", "Chinese")

# Print the initial number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Change the value and print it again
restaurant.number_served = 100
print(f"Number of customers served: {restaurant.number_served}")

# Using set_number_served() method
restaurant.set_number_served(200)
print(f"Number of customers served: {restaurant.number_served}")

# Using increment_number_served() method
restaurant.increment_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")


#9.5 login attmpts
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Creating an instance of the User class
user = User("John", "Doe", "johndoe", "john.doe@email.com", "New York")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print login attempts to check incrementation
print(f"Login Attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Login Attempts after reset: {user.login_attempts}")


#9.6 Ice Cream
# Using the Restaurant class from Exercise 9-4

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Creating an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Scoops Ahoy", "Ice Cream")
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"]

# Calling the method to display flavors
ice_cream_stand.display_flavors()
