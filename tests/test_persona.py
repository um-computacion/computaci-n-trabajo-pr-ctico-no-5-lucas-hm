import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)
    
    def test_pensar_incrementa_contador(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)
    
    def test_pensar_actualiza_ultimaidea():
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar(persona.ultima_idea, "hola mundo")
        
    
if __name__ == "__main__":
    unittest.main()