__author__ = 'Administrador'

from unittest import TestCase
from src.Equipo import *
from src.Liga import *


class TestLiga(TestCase):
    def test_existe_equipo(self):
        l = Liga("Liga BBVA", "2014", "Espania")
        equipo = Equipo("Sevilla FC", "1905", "Sevilla")
        l.aniadir_equipo(equipo)
        self.assertEqual(l.existe_equipo(equipo.get_nombre()), equipo)

    def test_crear_partidos(self):
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
        p = Partido(1, "FC Barcelona", "Real Madrid")
        l = Liga("Liga BBVA", "2014", "Espania")
        l.partidos.append(p)
        self.assertEqual(l.existe_partido(1), p)

    def test_jugar_partido(self):
        self.fail()

    def test_cofig_partido_local(self):
        self.fail()

    def test_cofig_partido_visitante(self):
        self.fail()

    def test_jugar_partidos_auto(self):
        self.fail()

    def test_consultar_mejor_estadio(self):
        self.fail()

    def test_pichichi_liga(self):
        self.fail()

    def test_recorrer_equipos(self):
        self.fail()