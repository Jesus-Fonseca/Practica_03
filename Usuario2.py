
class User():
	def __init__(self,first,second):
		self.first_name = first
		self.second_name = second
        
	def describe_user (self):
		print ("Primer apellido: " + self.first_name.title())
		print ("Segundo apellido: " + self.second_name.title())

	def greet_user (self):
		print ("Bienvenido " + self.first_name.title() + " " + self.second_name.title())
        
class Admin(User):
    def __init__(self,first,second):
        super().__init__(first,second)
        self.privilegios = Privileges()


class Privileges ():
    def __init__(self):
        self.privileges = ['Puede agregar un post','Puede eliminar post','Puede bannear a un usuario','Puede agregar a un usuario']
    def show_privileges(self):
        for i in range (len(self.privileges)):
            print (self.privileges[i])
            
usuario = User ('Lopez','Perez')
usuario.describe_user()
usuario.greet_user()
users = Admin('Fonseca' , 'Rodriguez')
users.privilegios.show_privileges()
