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

    def test_get_dorsal(self):
        """
        Test get dorsal

        Crea un jugador y comprueba que devuelve el dorsal correcto
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        self.assertEqual(jugador.get_dorsal(), 14)

    def test_get_posicion(self):
        """
        Test get posicion

        Crea un jugador y comprueba que devuelve la posicion correcta
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        self.assertEqual(jugador.get_posicion(), "Central")

    def test_get_goles_marcados(self):
        """
        Test get goles marcados

        Crea un jugador y comprueba que devuelve los goles marcados correctos
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        self.assertEqual(jugador.get_goles_marcados(), 0)

    def test_set_dorsal(self):
        """
        Test set dorsal

        Crea un jugador, modifica su dorsal y comprueba que devuelve el dorsal correcto
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.set_dorsal(15)
        self.assertEqual(jugador.get_dorsal(), 15)

    def test_set_posicion(self):
        """
        Test set posicion

        Crea un jugador, modifica su posicion y comprueba que devuelve la posicion correcta
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.set_posicion("Portero")
        self.assertEqual(jugador.get_posicion(), "Portero")

    def test_set_goles_marcados(self):
        """
        Test set goles marcados

        Crea un jugador, modifica sus goles marcados y comprueba que devuelve los goles marcados correctos
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.set_goles_marcados(5)
        self.assertEqual(jugador.get_goles_marcados(), 5)

    def test_mostrar_jugador(self):
        """
        Test mostrar jugador

        Crea un jugador, y lo muestra
        """
        jugador = Jugador("Luis", "Ayala Perez", "11867564G", "20/07/1988", "Espania", 14, "Central")
        jugador.mostrar_jugador()


