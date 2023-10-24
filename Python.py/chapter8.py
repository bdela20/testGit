# #Here’s a simple FUNCTIONS named greet_user() that prints a greeting:
# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")

# greet_user()




# def display_message():
#     """Display a simple greeting"""
#     print("Hello, " "I am learning about Functions" + "!")
          
# display_message()



#EXERCISE
# def favorite_book(book):
#     """"Display a simple message"""
#     print("My favorite book is, " + book.title() + "!")

# favorite_book("The self thaught programmer")




#STUCK 
# def make_shirt(size, message):
#    """"Displaying of a size and message"""""
#    print("\nI have a ", + size + ".")
#    print("My " + size + "shirt message is " + message.title() + ".")

# make_shirt(size='large', message='I love coding')



# def get_formatted_name(first_name, last_name):
#       """"Return a full name, neatly formatted."""
#       full_name = first_name + ' ' + last_name
#       return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix') 
# print(musician)





# def get_formatted_name(first_name, middle_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = first_name + ' ' + middle_name + ' ' + last_name
#        return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)






# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#       full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#        full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee') 
# print(musician)





# #Returning a Dictionary
# def build_person(first_name, last_name):
#        """Return a dictionary of information about a person."""
#        person = {'first': first_name, 'last': last_name}
#        return person

# musician = build_person('jimi', 'hendrix')
# print(musician)





# def build_person(first_name, last_name, age=''):
#        """Return a dictionary of information about a person."""
#        person = {'first': first_name, 'last': last_name}
#        if age:
#            person['age'] = age
#        return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)





# def get_formatted_name(first_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = first_name + ' ' + last_name
#        return full_name.title()
#    # This is an infinite loop!
# while True:
#  print("\nPlease tell me your name:")
# f_name = input("First name: ")
# l_name = input("Last name: ")
# formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")





# def get_formatted_name(first_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = first_name + ' ' + last_name
#        return full_name.title()
# while True:
#        print("\nPlease tell me your name:")
#        print("(enter 'q' at any time to quit)")
#        f_name = input("First name: ")
#        if f_name == 'q':
#            break
#        l_name = input("Last name: ")
#        if l_name == 'q':
#            break
#        formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")






#Returning a Dictionary
# def build_person(first_name, last_name):
#        """Return a dictionary of information about a person."""
#        person = {'first': first_name, 'last': last_name}
#        return person

# musician = build_person('jimi', 'hendrix')
# print(musician)






# def city_country(city_name, country_name):
#     """Return a dictionary of information about a city and country"""
#     city = city_name, country_name
#     return city

# place = city_country("Orlando", "Florida")
# print(place)


# def get_formatted_name(first_name, last_name):
#        """Return a full name, neatly formatted."""
#        full_name = first_name + ' ' + last_name
#        return full_name.title()
# while True:
#        print("\nPlease tell me your name:")
#        print("(enter 'q' at any time to quit)")
#        f_name = input("First name: ")
#        if f_name == 'q':
#            break
#        l_name = input("Last name: ")
#        if l_name == 'q':
#            break
#        formatted_name = get_formatted_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")




# #STUCK!
# def make_album(artist_name, album_name):
#     """Return a full name, neatly formatted."""
#     full_name = "first_name" + '' + "last_name"
#     return full_name.title()

# while True: 
#     print("\nPlease tell me your name:")
#     print("(Enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q': 
#         break
#     alb_name = input("Album name: ")
#     if alb_name == 'q':
#         break
#     formatted_name = (f_name, l_name)
# print ("\nHello, " + f_name +  l_name + "congratulations on your album " + alb_name + "!")






#  # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#    # Simulate printing each design, until none are left.
#    #  Move each design to completed_models after printing.
# while unprinted_designs:
#        current_design = unprinted_designs.pop()
# # Simulate creating a 3D print from the design.
#        print("Printing model: " + current_design)
#        completed_models.append(current_design)
#    # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#        print(completed_model)




# #EXCERCISE Magicians: Make a list of magician’s names . 
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list .
# def show_magicians(names):
#     """Print a simple greeting to each user on the list."""
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# usernames = ['Ben', 'Wale', 'Diego']
# show_magicians(usernames)




# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
       



#VIDEO PRACTICE 
# cars = ["audi", "ferrari", "ford",]
# groceries = ['oranges', 'grapes', 'bananas']

# def car_adder(thing_to_add, target_list):
#     if thing_to_add[0].lower() in 'abcdefg': 
#         print("this cars starts with A-G")
#         target_list.append(thing_to_add)
#     else:
#         print("This item starts with H_Z and we are not allowed it in our club")
# car_adder("BMW", cars)
# car_adder("honda", cars)
# car_adder("cinnamon", groceries)
# car_adder("zapples", groceries)

# print(cars)
# print(groceries)





# #RETURNING THINGS
# def add_two(num):
#     return num + 2

# def addThree(num):
#     return num + 3
# print(addThree(add_two(5)))


# def namePrinter(first, last, middle=''):
#     return f"The name's {last}, {first} {middle} {last}."

# # print(namePrinter("James", "Bond", "Freddy"))




