class Czlowiek:
        #Create
        def __init__(self, name, age, weight):
            self.name = name
            self.age = age
            self.weight = weight

        #Update
        def name_change(self, new_name):
            self.name = new_name
        def age_change(self, new_age):
            self.age = new_age    
        def weight_change(self, new_weight):
            self.weight = new_weight   

        #Read
        def print_name(self):
            print("Imie: " + self.name)
        def print_age(self):
            print("Wiek: " + self.age)
        def print_weight(self):
            print("Waga: " + self.weight)

        #Delete
        def delete_user(self, list):
            index = list.index(self)
            list.pop(index)