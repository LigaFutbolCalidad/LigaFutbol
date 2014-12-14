__author__ = 'Grupo 7'

from unittest import TestCase
from src.Entrenador import *


class TestEntrenador(TestCase):
    """
    Clase test de un entrenador de un equipo
    """

    def test_mostrar_entrenador(self):
        """
        Test mostrat entrenador

        Muestra el listado de los entrenadores
        """
        entrenador = Entrenador("Juan", "Garcia Perez", "11867564G", "20/07/1988", "Espania", "1186575X")
        entrenador.mostrar_entrenador()