class Persona:
    def __init__(self, nombre, apellido, dni, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sueldo = sueldo
        self.pensamientos = 0
        self.ultima_idea = "<no penso en nada>"

    def __repr__(self):
        return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
    
    def pensar(self, idea):
        self.pensamientos += 1
        self.ultima_idea = idea
        
    def pensar(self, idea):
        self.pensamientos += 1
        self.ultima_idea = idea
    