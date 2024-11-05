# I created one class for the inventory(object)and one class for the cars (object). For the CarsIventory, The init is the first step to create an empty dictionary. 
# then I added functions. One, to add to the datatbase(add_car) and the second to show the results (disply_dictoinary). The third function is to remove a car. the fourth function is to modify an entry (modify_car)
#For the Cars class, I used the init function and the str function to disply the results for the cars object.  
class CarsInventory:
    def __init__(self):
        self.Cars_dict={}
    def add_car(self, car_ID, car):
        self.Cars_dict[car_ID]=car
    def disply_dictionary(self):
        return "\n".join(f" {car_ID} {car} " for car_ID, car in self.Cars_dict.items())
    def remove_car(self,car_ID):
        if car_ID in self.Cars_dict:
            del self.Cars_dict[car_ID]
    def modify_car(self, car_ID, car):
        if car_ID in self.Cars_dict:
            self.Cars_dict[car_ID]= car
        else: 
            print("this car ID has not been created")
class Cars: 
    def __init__(self, brand, model, color, year, mileage): 
        self.brand=brand
        self.model=model
        self.color=color
        self.year=year
        self.mileage=mileage
    def __str__(self):
        return f"{self.brand} {self.model} {self.color} {self.year} {self.mileage}"

#make an example to begin filling the dictionary
r=CarsInventory()
r.add_car("1",Cars("Ford", "Focus", "red", 2023, 10000))
r.disply_dictionary()


# I made a second example to test in my Cars_dict.txt document. 
r.add_car("2",Cars("Dodge", "Durango", "blue", 2021, 15000))

#disply dictionary for reference 
r.disply_dictionary()

#Test remove_car function
r.remove_car("2")
r.disply_dictionary()

# test modify_car function
r.modify_car("1", Cars("Tesla", "Model X", "purple", 2024, 1000))
r.disply_dictionary()

# Create the file that will be utilized. Turning the dictionary into a txt file: 
file_name=r"C:\Users\mrton\Desktop\College Notes\ITS320-2\ITS320Assignments\Cars_dict.txt"
with open(file_name, "w") as file :
    file.write(r.disply_dictionary())