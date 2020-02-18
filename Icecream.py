

class Restaurant ():
    def __init__ (self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print ("El nombre del restaurante es " + self.restaurant_name.title())
        print ("El tipo de comida es " + self.cuisine_type.title())
    def open_restaurant(self):
        print ("El restaurante es " + str('abierto'))
            
class IceCreamStand(Restaurant):
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors = ['chocolate','limon','nuez','fresa','grosella','galleta']
    def read_flavor (self):
        for i in range (len(self.flavors)):
            print (self.flavors[i])
   
my_restaurant = Restaurant ('Salads life','comida vegana')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_ice = IceCreamStand('Holanda', 'Helados')
my_ice.read_flavor()


