__author__ = 'Grupo 7'

from unittest import TestCase
from src.Equipo import *
from src.Liga import *
from src.Jugador import *
from src.Estadio import *
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
        j1 = mock(Jugador)
        j2 = mock(Jugador)
        j3 = mock(Jugador)
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
        self.assertEqual(liga.recorrer_equipos().get_goles_marcados(), 9)

    def test_aniadir_equipo(self):
        """
        Test para aniadir un equipo

        Aniade un equipo a la liga y comprueba que esta aniadido
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.existe_equipo("FC Barcelona").mostrar_equipo()

    def test_listar_equipos(self):
        """
        Test listar equipos de la liga

        Imprime los equipos que se aniaden como prueba
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.aniadir_equipo(eq2)
        l.aniadir_equipo(eq3)
        l.listar_equipos()

    def test_consultar_equipo(self):
        """
        Test de consultar equipo

        Comprueba que muestra los datos del equipo
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.consultar_equipo(eq1)

    def test_listar_partidos(self):
        """
        Test de listar los partidos de la liga

        Imprime los datos de los partidos aniadidos como prueba
        """
        p1 = Partido(1, "FC Barcelona", "Real madrid")
        p2 = Partido(2, "FC Valencia", "FC Barcelona")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.partidos.append(p1)
        l.partidos.append(p2)
        l.listar_partidos()

    def test_consultar_calendario(self):
        """
        Test consultar el calendario de la liga

        Imprime los datos de los partidos que aun no se han jugado dado los datos de prueba
        """
        p1 = Partido(1, "FC Barcelona", "Real madrid")
        p2 = Partido(2, "FC Valencia", "FC Barcelona")
        p2.set_jugado(True)
        l = Liga("Liga BBVA", "2014", "Espania")
        l.partidos.append(p1)
        l.partidos.append(p2)
        l.consultar_calendario()

    def test_consultar_clasificacion(self):
        """
        Test consultar la clasificacion

        Imprime los datos de los partidos y las posiciones tras crear los partidos
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        eq1.set_puntos(5)
        eq2.set_puntos(3)
        eq3.set_puntos(3)
        eq1.set_goles_favor(10)
        eq2.set_goles_favor(5)
        eq3.set_goles_favor(1)
        eq1.set_partidos_ganados(1)
        eq1.set_partidos_empatados(2)
        eq2.set_partidos_empatados(3)
        eq3.set_partidos_ganados(1)
        eq3.set_partidos_perdidos(2)
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.aniadir_equipo(eq2)
        l.aniadir_equipo(eq3)
        l.consultar_clasificacion()

    def test_consultar_partido(self):
        """
        Test consultar partido

        Imprime los datos del partido que se introducen como prueba
        """
        p1 = Partido(1, "FC Barcelona", "Real madrid")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.partidos.append(p1)
        l.consultar_partido(p1)

    def test_consultar_mejor_estadio(self):
        """
        Test consultar el mejor estadio de la liga

        Imprime el nombre del estadio con mayor capacidad de la liga dado los datos de prueba
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        es1 = Estadio("Camp Nou", "Barcelona", 1650300)
        es2 = Estadio("Bernabeu", "Madrid", 1500200)
        es3 = Estadio("Mestalla", "Valencia", 1560200)
        eq1.asignar_estadio(es1)
        eq2.asignar_estadio(es2)
        eq3.asignar_estadio(es3)
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.aniadir_equipo(eq2)
        l.aniadir_equipo(eq3)
        l.consultar_mejor_estadio()

    def test_listar_pichichis_equipos(self):
        """
        Test listar los pichichis de los equipos de la liga

        Imprime los datos de los pichichis de los equipos de la liga dado los datos introducidos de prueba
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq2 = Equipo("Real Madrid", "1902", "Madrid")
        eq3 = Equipo("FC Valencia", "1901", "Valencia")
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        j2 = Jugador("Luis", "Suarez", "1234S", "11/08/1985", "Uruguay", 12, "delantero")
        j3 = Jugador("Neymar", "Junior", "1234J", "19/02/1990", "Brasil", 15, "delantero")
        j1.set_goles_marcados(5)
        j2.set_goles_marcados(10)
        j3.set_goles_marcados(1)
        eq1.agregar_jugador(j1)
        eq2.agregar_jugador(j2)
        eq3.agregar_jugador(j3)
        l = Liga("Liga BBVA", "2014", "Espania")
        l.aniadir_equipo(eq1)
        l.aniadir_equipo(eq2)
        l.aniadir_equipo(eq3)
        l.listar_pichichis_equipos()

    def test_mostrar_liga(self):
        """
        Test mostrar liga

        Imprime los datos de la liga dado los de prueba
        """
        l = Liga("Liga BBVA", "2014", "Espania")
        l.mostrar_liga()