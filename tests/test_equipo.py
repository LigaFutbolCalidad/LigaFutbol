from unittest import TestCase
from src.Equipo import *
from src.Estadio import *
from src.Entrenador import *
from src.Jugador import *

__author__ = 'Grupo 7'


class TestEquipo(TestCase):
    """
    Clase test de un equipo de una liga
    """
    def test_incrementar_puntos(self):
        """
        Test incrementar puntos

        Crea un equipo, le cambia los puntos, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_puntos(5)
        equipo.incrementar_puntos(5)
        self.assertEqual(equipo.get_puntos(), 10)

    def test_incrementar_goles_favor(self):
        """
        Test incrementar goles a favor

        Crea un equipo, le cambia los goles a favor, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_goles_favor(5)
        equipo.incrementar_goles_favor(5)
        self.assertEqual(equipo.get_goles_favor(), 10)

    def test_incrementar_goles_contra(self):
        """
        Test incrementar goles en contra

        Crea un equipo, le cambia los goles en contra, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_goles_contra(3)
        equipo.incrementar_goles_contra(3)
        self.assertEqual(equipo.get_goles_contra(), 6)

    def test_incrementar_partidos_ganados(self):
        """
        Test incrementar partidos ganados

        Crea un equipo, le cambia los partidos ganados, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_partidos_ganados(2)
        equipo.incrementar_partidos_ganados()
        self.assertEqual(equipo.get_partidos_ganados(), 3)

    def test_incrementar_partidos_empatados(self):
        """
        Test incrementar partidos empatados

        Crea un equipo, le cambia los partidos empatados, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_partidos_empatados(1)
        equipo.incrementar_partidos_empatados()
        self.assertEqual(equipo.get_partidos_empatados(), 2)

    def test_incrementar_partidos_perdidos(self):
        """
        Test incrementar partidos empatados

        Crea un equipo, le cambia los partidos empatados, los incrementa y comprueba si devuelve los correctos
        """
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.set_partidos_empatados(5)
        equipo.incrementar_partidos_empatados()
        self.assertEqual(equipo.get_partidos_empatados(), 6)

    def test_asignar_estadio(self):
        """
        Test asignar estadio

        Crea un estadio y un equipo y le asigna ese estadio. Comprueba si ese equipo devuelve ese estadio
        """
        es1 = Estadio("Camp Nou", "Barcelona", 1650300)
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.asignar_estadio(es1)
        self.assertEqual(equipo.get_estadio(), es1)

    def test_asignar_entrenador(self):
        """
        Test asignar entrenador

        Crea un entrenador y un equipo y le asigna ese entrenador. Comprueba si ese equipo devuelve ese entrenador
        """
        en1 = Entrenador("Pep", "Guardiola", "1234P", "22/11/1975", "Espania", "1234L")
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.asignar_entrenador(en1)
        self.assertEqual(equipo.get_entrenador(), en1)

    def test_agregar_jugador(self):
        """
        Test agregar jugador

        Crea un jugador y un equipo y le agrega ese jugador. Comprueba si existe ese jugador en ese equipo
        """
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        equipo.agregar_jugador(j1)
        self.assertEqual(equipo.existe_jugador(j1.get_dni()), j1)

    def test_pichichi_equipo(self):
        """
        Test pichichi equipo

        Crea 3 jugadores y un equipo y le agrega esos jugadores. Cambia los goles de los jugadores y comprueba que
        devuelve el que tiene mas goles marcados
        """
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        j2 = Jugador("Luis", "Suarez", "1234S", "11/08/1985", "Uruguay", 12, "delantero")
        j3 = Jugador("Neymar", "Junior", "1234J", "19/02/1990", "Brasil", 15, "delantero")
        equipo = Equipo("Barsa", "1990", "Barcelona")
        equipo.agregar_jugador(j1)
        equipo.agregar_jugador(j2)
        equipo.agregar_jugador(j3)
        j1.set_goles_marcados(3)
        j2.set_goles_marcados(4)
        j3.set_goles_marcados(3)
        self.assertEqual(equipo.pichichi_equipo(), j2)

    def test_consultar_jugador(self):
        """
        Test consultar jugador

        Crea un jugador y mustra sus datos
        """
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.agregar_jugador(j1)
        eq1.consultar_jugador(j1)

    def test_existe_jugador(self):
        """
        Test para comprobar si existe un jugador

        Compruieba si existe el jugador creado
        """
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.agregar_jugador(j1)
        eq1.existe_jugador("1234M").mostrar_jugador()

    def test_listar_jugadores(self):
        """
        Test de listar jugadores

        Comprueba que se muestra la lista de los jugadores aniadidos a un equipo
        """
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        j2 = Jugador("Luis", "Suarez", "1234S", "11/08/1985", "Uruguay", 12, "delantero")
        j3 = Jugador("Neymar", "Junior", "1234J", "19/02/1990", "Brasil", 15, "delantero")
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.agregar_jugador(j1)
        eq1.agregar_jugador(j2)
        eq1.agregar_jugador(j3)
        eq1.listar_jugadores()

    def test_consultar_estadio(self):
        """
        Test de consultar estadio

        Comprueba que muestra los datos del estadio creado
        """
        es1 = Estadio("Camp Nou", "Barcelona", 1650300)
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.asignar_estadio(es1)
        eq1.consultar_estadio()

    def test_consultar_entrenador(self):
        """
        Test de consultar entrenador

        Comprueba que muestra los datos del entrenador creado
        """
        en1 = Entrenador("Pep", "Guardiola", "1234P", "22/11/1975", "Espania", "1234L")
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.asignar_entrenador(en1)
        eq1.consultar_entrenador()

    def test_mostrar_equipo(self):
        """
        Test de mostrar equipo

        Comprueba que muestra los datos del equipo
        """
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        eq1.mostrar_equipo()