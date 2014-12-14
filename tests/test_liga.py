__author__ = 'Administrador'

from unittest import TestCase
from src.Equipo import *
from src.Liga import *
from src.Jugador import *
from mockito import *


class TestLiga(TestCase):
    """
    Clase test de una liga
    """
    def test_existe_equipo(self):
        """
        Test existe equipo

        Crea una liga y un equipo y lo aniade a la liga. Comprueba que devuelve ese equipo
        """
        l = Liga("Liga BBVA", "2014", "Espania")
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        l.aniadir_equipo(equipo)
        self.assertEqual(l.existe_equipo(equipo.get_nombre()), equipo)

    def test_crear_partidos(self):
        """
        Test crear partidos

        Crea una liga y 4 equipos y los aniade. Crea dos partidos iguales y los compara para comprobar que se han creado
        los partidos autmaticamente
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        eq4 = Equipo("Sevilla FC", "1901", "Sevilla")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.aniadir_equipo(eq2)
        l.aniadir_equipo(eq3)
        l.aniadir_equipo(eq4)
        p = Partido(1, "FC Barcelona", "Real Madrid")
        p2 = l.existe_partido(1)
        self.assertEqual(p.get_equipo_local(), p2.get_equipo_local())
        self.assertEqual(p.get_equipo_visitante(), p2.get_equipo_visitante())

    def test_existe_partido(self):
        """
        Test existe partido

        Crea una liga y un partido y lo aniade a la liga. Comprueba que devuelve ese partido
        """
        p = Partido(1, "FC Barcelona", "Real Madrid")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.partidos.append(p)
        self.assertEqual(l.existe_partido(1), p)

    def test_pichichi_liga(self):
        """
        Test pichichi liga

        Crea unos equipos con unos jugadores y una liga a la que los aniade. Comprueba que devuelve el jugador
         que mas goles tiene
        """
        j1=mock(Jugador)
        j2=mock(Jugador)
        j3=mock(Jugador)
        when(j1).get_goles_marcados().thenReturn(3)
        when(j2).get_goles_marcados().thenReturn(5)
        when(j3).get_goles_marcados().thenReturn(9)
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        eq1.agregar_jugador(j1)
        eq2.agregar_jugador(j2)
        eq3.agregar_jugador(j3)
        liga = Liga("Liga BBVA", "2014", "Espania")
        liga.aniadir_equipo(eq1)
        liga.aniadir_equipo(eq2)
        liga.aniadir_equipo(eq3)
        self.assertEqual(liga.recorrer_equipos().get_goles_marcados(),9)