from src.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.sueldo = sueldo
        
    def __repr__(self):
        return f"profesor: DNI: {self.dni} Nombre: {self.nombre} apellido: {self.apellido} Sueldo: {self.sueldo}"