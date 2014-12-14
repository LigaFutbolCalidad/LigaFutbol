__author__ = 'Grupo 7'

from unittest import TestCase
from src.Persona import *

class TestPersona(TestCase):
    """
    Clase test de una persona
    """
    def test_set_dni(self):
        """
        Test set dni

        Modifica el dni de una persona
        """
        persona = Persona("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania")
        persona.set_dni("1186575Y")
        self.assertEqual(persona.get_dni(), "1186575Y")


    def test_set_nombre(self):
        """
        Test set nombre

        Modifica el nombre de una persona
        """
        persona = Persona("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania")
        persona.set_nombre("Manuel")
        self.assertEqual(persona.get_nombre(), "Manuel")


    def test_set_apellidos(self):
        """
        Test set apellidos

        Modifica los apellidos de la persona
        """
        persona = Persona("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania")
        persona.set_apellidos("Perez Garcia")
        self.assertEqual(persona.get_apellidos(), "Perez Garcia")


    def test_fecha_nac(self):
        """
        Test set fecha nacimiento

        Modifica la fecha de nacimiento de la persona
        """
        persona = Persona("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania")
        persona.set_fecha_nac("1186575Z")
        self.assertEqual(persona.get_fecha_nac(), "1186575Z")


    def test_set_pais_nac(self):
        """
        Test set pais nacimiento

        Modifica el pais de nacimiento de la persona
        """
        persona = Persona("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania")
        persona.set_pais_nac("Francia")
        self.assertEqual(persona.get_pais_nac(), "Francia")