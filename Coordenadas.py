import math
class Point():
    def __init__ (self,x,y):
        self.x_punto = x
        self.y_punto = y
        
        
    def Modificar_point (self):
        print ('Ingrese el valor para x')
        x = input()
        print ('Ingrese el valor para y')
        y = input()
        self.x_punto = x
        self.y_punto = y

    def Show_point(self):
        print ('La coordenada es ' + str(self.x_punto) + ' , ' + str(self.y_punto))
        
        
        
mi_coordenada = Point (3,4)
mi_coordenada.Show_point()
mi_coordenada.Modificar_point()
mi_coordenada.Show_point()


class Rectangulo():
    def __init__ (self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1_punto = x1
        self.y1_punto = y1
        self.x2_punto = x2
        self.y2_punto = y2
        self.x3_punto = x3
        self.y3_punto = y3
        self.x4_punto = x4
        self.y4_punto = y4
        
    def Modificar_rectangulo (self):
        print ('Ingrese el valor para x1')
        x1 = input()
        print ('Ingrese el valor para y1')
        y1 = input()
        
        print ('Ingrese el valor para x2')
        x2 = input()
        print ('Ingrese el valor para y2')
        y2 = input()
        
        print ('Ingrese el valor para x3')
        x3 = input()
        print ('Ingrese el valor para y3')
        y3 = input()
        
        print ('Ingrese el valor para x4')
        x4 = input()
        print ('Ingrese el valor para y4')
        y4 = input()
        self.x1_punto = x1
        self.y1_punto = y1
        self.x2_punto = x2
        self.y2_punto = y2
        self.x3_punto = x3
        self.y3_punto = y3
        self.x4_punto = x4
        self.y4_punto = y4
        
     
    def Show_puntos(self):
        print ('La coordenada del punto 1 ubicadaen la esquina superior izquierda del rectangulo es: ' + str(self.x1_punto) + ' , ' + str(self.y1_punto))
        print ('La coordenada del punto 2 ubicadaen la esquina superior derecha del rectangulo es: ' + str(self.x2_punto) + ' , ' + str(self.y2_punto))
        print ('La coordenada del punto 3 ubicadaen la esquina inferior izquierda del rectangulo es: ' + str(self.x3_punto) + ' , ' + str(self.y3_punto))
        print ('La coordenada del punto 4 ubicadaen la esquina inferior derecha del rectangulo es: ' + str(self.x4_punto) + ' , ' + str(self.y4_punto))
      
        
    def Area(self): 
        
        b1 = math.sqrt(((self.x2_punto-self.x1_punto)**2)+((self.y2_punto-self.y1_punto)**2))
        h1 = math.sqrt(((self.x3_punto-self.x2_punto)**2)+((self.y3_punto-self.y2_punto)**2))
        AT= b1*h1
        print ('El area es de: ', AT)
        
    def Perimetro(self):
        b1 = math.sqrt(((self.x2_punto-self.x1_punto)**2)+((self.y2_punto-self.y1_punto)**2))
        h1 = math.sqrt(((self.x3_punto-self.x2_punto)**2)+((self.y3_punto-self.y2_punto)**2))
        P = (b1*2)+(h1*2)
        print ('El perimetro es de: ', P)
        
    
mi_rectangulo = Rectangulo(1,3,5,3,5,1,1,1)
mi_rectangulo.Show_puntos()
mi_rectangulo.Area()
mi_rectangulo.Perimetro()
mi_rectangulo.Modificar_rectangulo()
mi_rectangulo.Show_puntos()   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        