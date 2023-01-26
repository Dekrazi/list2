from class_czlowiek import Czlowiek

list = []

menu_options = {
    1: 'Add User',
    2: 'Update User',
    3: 'See List of Users',
    4: 'Delete User',
    5: 'Exit',
}
print(menu_options)

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

option = int(input('Enter your choice: ')) 
if option == 1:
    print("Who do you want to add? ")
    print(input("Name? "))
    name_variable = input
    print(input("Age? "))
    age_variable = input
    print(input("Weight? "))
    weight_variable = input
    new_user = Czlowiek(name_variable, str(age_variable), str(weight_variable))
    list.append(new_user)
    

elif option == 2:
    print('Update data')

elif option == 3:
    print('Names: ')
    for people in list:
        print(people.name)

elif option == 4:
    print(input('Who do you want to delete? '))
    list.delete_user(input)
   
elif option == 5:
    print('This was the best menu ever!') 
    exit()

else:
    print('Invalid option. Please enter a number between 1 and 5.')
    
print(*list)