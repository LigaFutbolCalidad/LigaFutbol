from unittest import TestCase
from src.Registro import *

__author__ = 'Patry'


class TestRegistro(TestCase):
    """
    Clase test de un registro
    """
    def test_existe_jugador(self):
        """
        Test existe jugador

        Crea un registro y un jugador y lo aniade al registro. Comprueba que devuelve ese jugador
        """
        r = Registro()
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        r.aniadir_jugador(j1)
        self.assertEqual(r.existe_jugador(j1.get_dni()), j1)

    def test_eliminar_jugador(self):
        """
        Test eliminar jugador

        Crea un registro y un jugador y lo aniade al registro. Luego borra ese jugador y comprueba que no lo devuelve
        """
        r = Registro()
        j1 = Jugador("Leo", "Messi", "1234M", "23/02/1980", "Argentina", 5, "delantero")
        r.aniadir_jugador(j1)
        r.jugadores.remove(j1)
        self.assertEqual(r.existe_jugador(j1.get_dni()), None)

    def test_existe_entrenador(self):
        """
        Test existe entrenador

        Crea un registro y un entrenador y lo aniade al registro. Comprueba que devuelve ese entrenador
        """
        r = Registro()
        en1 = Entrenador("Pep", "Guardiola", "1234P", "22/11/1975", "Espania", "1234L")
        r.aniadir_entrenador(en1)
        self.assertEqual(r.existe_entrenador(en1.get_dni()), en1)

    def test_eliminar_entrenador(self):
        """
        Test eliminar entrenador

        Crea un registro y un entrenador y lo aniade al registro. Luego borra ese entrenador y comprueba que no
        lo devuelve
        """
        r = Registro()
        en1 = Entrenador("Pep", "Guardiola", "1234P", "22/11/1975", "Espania", "1234L")
        r.aniadir_entrenador(en1)
        r.entrenadores.remove(en1)
        self.assertEqual(r.existe_entrenador(en1.get_dni()), None)

    def test_existe_estadio(self):
        """
        Test existe estadio

        Crea un registro y un estadio y lo aniade al registro. Comprueba que devuelve ese estadio
        """
        r = Registro()
        es1 = Estadio("Camp Nou", "Barcelona", 1650300)
        r.aniadir_estadio(es1)
        self.assertEqual(r.existe_estadio(es1.get_nombre()), es1)

    def test_eliminar_estadio(self):
        """
        Test eliminar estadio

        Crea un registro y un estadio y lo aniade al registro. Luego borra ese estadio y comprueba que no lo devuelve
        """
        r = Registro()
        es1 = Estadio("Camp Nou", "Barcelona", 1650300)
        r.aniadir_estadio(es1)
        r.estadios.remove(es1)
        self.assertEqual(r.existe_estadio(es1.get_nombre()), None)

    def test_existe_equipo(self):
        """
        Test existe equipo

        Crea un registro y un equipo y lo aniade al registro. Comprueba que devuelve ese equipo
        """
        r = Registro()
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        r.aniadir_equipo(eq1)
        self.assertEqual(r.existe_equipo(eq1.get_nombre()), eq1)

    def test_eliminar_equipo(self):
        """
        Test eliminar equipo

        Crea un registro y un equipo y lo aniade al registro. Luego borra ese equipo y comprueba que no lo devuelve
        """
        r = Registro()
        eq1 = Equipo("FC Barcelona", "1900", "Barcelona")
        r.aniadir_equipo(eq1)
        r.equipos.remove(eq1)
        self.assertEqual(r.existe_equipo(eq1.get_nombre()), None)

    def test_existe_liga(self):
        """
        Test existe liga

        Crea un registro y una liga y la aniade al registro. Comprueba que devuelve esa liga
        """
        r = Registro()
        l = Liga("Liga BBVA", "2014", "Espania")
        r.aniadir_liga(l)
        self.assertEqual(r.existe_liga(l.get_nombre()), l)

    def test_eliminar_liga(self):
        """
        Test eliminar liga

        Crea un registro y una liga y la aniade al registro. Luego borra esa liga y comprueba que no la devuelve
        """
        r = Registro()
        l = Liga("Liga BBVA", "2014", "Espania")
        r.aniadir_liga(l)
        r.ligas.remove(l)
        self.assertEqual(r.existe_liga(l.get_nombre()), None)