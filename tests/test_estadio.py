from unittest import TestCase
from src.Estadio import *

__author__ = 'Grupo 7'


class TestEstadio(TestCase):
    def test_mostrar_estadio(self):
        """
        Test de mostrar estadio

        Muestra los datos del estadio completo
        """
        estadio = Estadio("Sevilla", "Sevilla FC", "2000")
        estadio.mostrar_estadio()