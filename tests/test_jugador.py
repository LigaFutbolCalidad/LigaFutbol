__author__ = 'Grupo 7'

from unittest import TestCase
from src.Jugador import *


class TestJugador(TestCase):
    """
    Clase test de un jugador de un equipo
    """
    def test_incrementar_goles(self):
        """
        Test incrementar goles

        Crea un jugador, le incrementa los goles y comprueba que devuelve los correctos
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.incrementar_goles()
        self.assertEqual(jugador.get_goles_marcados(), 1)

    def test_mostrar_jugador(self):
        """
        Test mostrar jugador

        Crea un jugador, y lo muestra
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.mostrar_jugador()


