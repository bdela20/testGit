# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


# alien_0 = {'color': 'green'}
# print(alien_0['color'])

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")

# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")




# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))

# # Move the alien to the right.
# # Determine how far to move the alien based an its current speed. 
# if alien_0['speed']  == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be as fast alien. 
#     x_increment = 3

# # The new position is the old position plus the increment. 
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position: " + str(alien_0['x_position'])) 



# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)


# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }

# print("Sarah's favorite language is " +
#      favorite_languages['sarah'].title() +
#      ".")

# favorite_languages['sarah']



# ben_20 = {
#               'Waleska': '100',
#               'Noah': '11',
#               'Mathew': '12',
#               }


# for key, value in ben_20.items():
#     print("\nKey: " + key)
#     print("Value: " + value)



# favorite_languages = {
#        'jen': 'python', 
#        'sarah': 'c', 
#        'edward': 'ruby',
#        'phil': 'python'
#        }
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")




# for name in favorite_languages:
#     print(name.title())



# friends = ['phil', 'jen']
# for name in favorite_languages.keys():
#        print(name.title())
#        if name in friends:
#         print(" Hi " + name.title() +

#             ", I see your favorite language is " +
#             favorite_languages[name].title() + "!")



# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }
# for name in sorted(favorite_languages.keys()):
#        print(name.title() + ", thank you for taking the poll.")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# favorite_languages = {
    # 'jen': 'python',
    # 'sarah': 'c',
    # 'edward': 'ruby',
    # 'phil': 'python',
    # }

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()): print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2] 

# for alien in aliens:
#        print(alien)




# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens.
# for alien_number in range(30):
#   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
#   aliens.append(new_alien)  

#    # Show the first 5 aliens.    
# for alien in aliens[:5]:
#  print(alien)
# print("...")

# # Show how many aliens have been created.
# print("Total number of aliens: " + str(len(aliens)))


# favorite_languages = {
# 'jen': ['python', 'ruby'],
#        'sarah': ['c'],
#        'edward': ['ruby', 'go'],
#        'phil': ['python', 'haskell'],
#        }
# for name, languages in favorite_languages.items():
#  print("\n" + name.title() + "'s favorite languages are:")
#  for language in languages: print("\t" + language.title())


# my_dict = {
#         'soccer', ['Manchester City', 'Bayern Munich', 'Seatlle Sounders'],

# del my_dict[2]


# x = my_dict.get(3)

# print(my_dict)


# for key, value in my_dict.items(): 
    # print(f'The key is {key}')
    # print(f'And this is the value: {value}')

# for value in my_dict.values():
#     print(value)

# for key in my_dict.keys():
#     print(key)

# print(my_dict)