from class_czlowiek import Czlowiek
from menu import menu_options

def main():

    

    Michal = Czlowiek('Michal', 37, 200)
    Radek = Czlowiek('Radek', 37, 75)
    
    list = []
            
    list.append(Michal)
    list.append(Radek)

    
                    
    print('Names: ')
    for people in list:
        print(people.name)

    Michal.name_change('Pan Programista Michal')

    print('New names:')
    for people in list:
        print(people.name) 

    print('Overall data: ')
    for data in list:
        print('Name: ' + data.name, 'Age: ' + str(data.age), 'Weight: ' + str(data.weight) + 'kg')
        
    Michal.weight_change(500)
    Radek.weight_change(76)

    for people in list:
        print(people.weight)

    for people in list:
        print('Adjusted weight is: ' + people.name + ' ' + str(people.weight))






# lista przed zmina > druk listy > zmien imie > druk jeszcze raz