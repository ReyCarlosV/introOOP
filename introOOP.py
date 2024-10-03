class Persona:
    def __init__(self, nombre, edad, genero, ocupacion, ciudad):
        # Atributos de la clase Persona
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion
        self.ciudad = ciudad

    # Método 1: Saludar
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}.")

    # Método 2: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tienes {self.edad} años.")

    # Método 3: Cambiar de ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    # Método 4: Moverse de ciudad
    def mudarse(self, nueva_ciudad):
        self.ciudad = nueva_ciudad
        print(f"{self.nombre} se ha mudado a {self.ciudad}.")

    # Método 5: Presentarse
    def presentarse(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, soy {self.genero}, trabajo como {self.ocupacion} y vivo en {self.ciudad}.")

    # Método 6: Saludar otra persona
    def saludarA(self,nombreOtraPersona):
        print(f"Hola, {self.nombre}, te manda a saludar {nombreOtraPersona.nombre}.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30, "masculino", "ingeniero", "Madrid")
persona2 = Persona("victor",10,"Hombre","Estudiante","CDMX")
persona3 = Persona("Brenda",21,"Femenino","Ingeniero")

# Usar los métodos de la instancia
persona1.saludar()
persona1.presentarse()
persona1.cumplir_anios()
persona1.cambiar_ocupacion("arquitecto")
persona1.mudarse("Barcelona")
persona1.saludarA(persona2)
persona1.saludar()