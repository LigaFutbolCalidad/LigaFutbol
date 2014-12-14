from unittest import TestCase
from src.Partido import *

__author__ = 'Grupo 7'


class TestPartido(TestCase):
    def test_mostrar_partido(self):
        """
        Test de mostrar partido

        Muestra los datos del partido completo
        """
        partido = Partido(3, "Sevilla", "Betis")
        partido.mostrar_partido()