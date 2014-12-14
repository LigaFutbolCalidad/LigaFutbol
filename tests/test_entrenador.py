__author__ = 'Grupo 7'

from unittest import TestCase
from src.Entrenador import *


class TestEntrenador(TestCase):
    """
    Clase test de un entrenador de un equipo
    """
    def test_get_licencia(self):
        """
        Test get licencia

        Consulta la licencia de un entrenador
        """
        entrenador = Entrenador("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania", "1186575X")
        self.assertEqual(entrenador.get_licencia(), "1186575X")

    def test_set_licencia(self):
        """
        Test set licencia

        Modifica la licencia de un entrenador
        """
        entrenador = Entrenador("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania", "1186575X")
        entrenador.set_licencia("1186575Y")
        self.assertEqual(entrenador.get_licencia(), "1186575Y")

    def test_mostrar_entrenador(self):
        """
        Test mostrat entrenador

        Muestra el listado de los entrenadores
        """
        entrenador = Entrenador("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania", "1186575X")
        entrenador.mostrar_entrenador()