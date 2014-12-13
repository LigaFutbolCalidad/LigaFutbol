__author__ = 'Grupo 7'
from src.Jugador import *
from src.Entrenador import *
from src.Estadio import *
from src.Equipo import *
from src.Liga import *


class Registro:
    def __init__(self):
        self.ligas = []
        self.equipos = []
        self.jugadores = []
        self.entrenadores = []
        self.estadios = []

    # CRUD JUGADOR
    def existe_jugador(self, dni):
        jugador = None
        for j in self.jugadores:
            if j.get_dni() == dni:
                jugador = j
        return jugador

    def crear_jugador(self):
        nombre = raw_input("Indique el nombre del jugador: ")
        apellidos = raw_input("Indique los apellidos del jugador: ")
        dni = raw_input("Indique el dni del jugador: ")
        fecha_nac = raw_input("Indique la fecha de nacimiento del jugador: ")
        pais_nac = raw_input("Indique el pais de nacimiento del jugador: ")
        dorsal = input("Indique el dorsal del jugador: ")
        posicion = raw_input("Indique la posicion de juego: ")
        if self.existe_jugador(dni) is not None:
            print "El jugador ya existe"
        else:
            j = Jugador(nombre, apellidos, dni, fecha_nac, pais_nac, dorsal, posicion)
            self.aniadir_jugador(j)

    def modificar_jugador(self):
        dni = raw_input("Introduce el dni del jugador ha modificar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print "El dni no se corresponde con ningun jugador"
        else:
            print "Introduzca los nuevos datos:"
            nombre = raw_input("Nombre: ")
            apellidos = raw_input("Apellidos: ")
            fecha_nac = raw_input("Fecha nacimiento: ")
            pais_nac = raw_input("Pais de nacimiento: ")
            dorsal = input("Dorsal: ")
            posicion = raw_input("Posicion: ")
            j.set_nombre(nombre)
            j.set_apellidos(apellidos)
            j.set_fechaNac(fecha_nac)
            j.set_paisNac(pais_nac)
            j.set_dorsal(dorsal)
            j.set_posicion(posicion)
            print "Jugador modificado correctamente"

    def eliminar_jugador(self):
        dni = raw_input("Introduce el dni del jugador a eliminar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print "El dni no se corresponde con ningun jugador"
        else:
            self.jugadores.remove(j)
            print "Jugador eliminado correctamente"

    def consultar_jugador(self):
        dni = raw_input("Introduce el dni del jugador a consultar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print "El dni no se corresponde con ningun jugador"
        else:
            j.mostrar_jugador()

    #CRUD ENTRENADOR
    def existe_entrenador(self, dni):
        entrenador = None
        for e in self.entrenadores:
            if e.get_dni() == dni:
                entrenador = e
        return entrenador

    def crear_entrenador(self):
        nombre = raw_input("Indique el nombre del entrenador: ")
        apellidos = raw_input("Indique los apellidos del entrenador: ")
        dni = raw_input("Indique el dni del entrenador: ")
        fecha_nac = raw_input("Indique la fecha de nacimiento del entrenador: ")
        pais_nac = raw_input("Indique el pais de nacimiento del entrenador: ")
        licencia = raw_input("Indique la licecia del entrenador: ")
        if self.existe_entrenador(dni) is not None:
            print "El entrenador ya existe"
        else:
            e = Entrenador(nombre, apellidos, dni, fecha_nac, pais_nac, licencia)
            self.aniadir_entrenador(e)

    def modificar_entrenador(self):
        dni = raw_input("Introduce el dni del entrenador ha modificar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print "El dni no se corresponde con ningun entrenador"
        else:
            print "Introduzca los nuevos datos:"
            nombre = raw_input("Nombre: ")
            apellidos = raw_input("Apellidos: ")
            fecha_nac = raw_input("Fecha nacimiento: ")
            pais_nac = raw_input("Pais de nacimiento: ")
            licencia = raw_input("Licencia: ")
            e.set_nombre(nombre)
            e.set_apellidos(apellidos)
            e.set_fechaNac(fecha_nac)
            e.set_paisNac(pais_nac)
            e.set_licencia(licencia)
            print "Entrenador modificado correctamente"

    def eliminar_entrenador(self):
        dni = raw_input("Introduce el dni del entrenador a eliminar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print "El dni no se corresponde con ningun entrenador"
        else:
            self.entrenadores.remove(e)
            print "Entrenador eliminado correctamente"

    def consultar_entrenador(self):
        dni = raw_input("Introduce el dni del entrenador a consultar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print "El dni no se corresponde con ningun entrenador"
        else:
            e.mostrar_entrenador()

    #CRUD ESTADIO
    def existe_estadio(self, nombre):
        estadio = None
        for e in self.estadios:
            if e.get_nombre() == nombre:
                estadio = e
        return estadio

    def crear_estadio(self):
        nombre = raw_input("Indique el nombre del estadio: ")
        ciudad = raw_input("Indique la ciudad del estadio: ")
        capacidad = input("Indique la capacidad del estadio: ")
        if self.existe_estadio(nombre) is not None:
            print "El estadio ya existe"
        else:
            e = Estadio(nombre, ciudad, capacidad)
            self.aniadir_estadio(e)

    def modificar_estadio(self):
        nombre = raw_input("Introduce el nombre del estadio ha modificar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun estadio"
        else:
            print "Introduzca los nuevos datos:"
            nombre = raw_input("Nombre: ")
            ciudad = raw_input("Ciudad: ")
            capacidad = input("Capacidad: ")
            e.set_nombre(nombre)
            e.set_ciudad(ciudad)
            e.set_capacidad(capacidad)
            print "Estadio modificado correctamente"

    def eliminar_estadio(self):
        nombre = raw_input("Introduce el nombre del estadio a eliminar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun estadio"
        else:
            self.estadios.remove(e)
            print "Estadio eliminado correctamente"

    def consultar_estadio(self):
        nombre = raw_input("Introduce el nombre del estadio a consultar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun estadio"
        else:
            e.mostrar_estadio()

    #CRUD EQUIPO
    def existe_equipo(self, nombre):
        equipo = None
        for e in self.equipos:
            if e.get_nombre() == nombre:
                equipo = e
        return equipo

    def crear_equipo(self):
        nombre = raw_input("Indique el nombre del equipo: ")
        anio_creacion = raw_input("Indique el anio de creacion del equipo: ")
        ciudad = raw_input("Indique la ciudad del equipo: ")
        if self.existe_equipo(nombre) is not None:
            print "El equipo ya existe"
        else:
            e = Equipo(nombre, anio_creacion, ciudad)
            self.aniadir_equipo(e)

    def modificar_equipo(self):
        nombre = raw_input("Introduce el nombre del equipo ha modificar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun equipo"
        else:
            print "Introduzca los nuevos datos:"
            nombre = raw_input("Nombre: ")
            anio_creacion = raw_input("Anio creacion: ")
            ciudad = raw_input("Ciudad: ")
            e.set_nombre(nombre)
            e.set_anioCreacion(anio_creacion)
            e.set_ciudad(ciudad)
            print "Equipo modificado correctamente"

    def eliminar_equipo(self):
        nombre = raw_input("Introduce el nombre del equipo a eliminar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun equipo"
        else:
            self.equipos.remove(e)
            print "Equipo eliminado correctamente"

    def consultar_equipo(self):
        nombre = raw_input("Introduce el nombre del equipo a consultar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print "El nombre no se corresponde con ningun equipo"
        else:
            e.mostrar_equipo()

    #CRUD LIGA
    def existe_liga(self, nombre):
        liga = None
        for l in self.ligas:
            if l.get_nombre() == nombre:
                liga = l
        return liga

    def crear_liga(self):
        nombre = raw_input("Indique el nombre de la liga: ")
        anio = raw_input("Indique el anio de la liga: ")
        pais = raw_input("Indique el pais de la liga: ")
        if self.existe_liga(nombre) is not None:
            print "La liga ya existe"
        else:
            l = Liga(nombre, anio, pais)
            self.aniadir_liga(l)

    def modificar_liga(self):
        nombre = raw_input("Introduce el nombre de la liga ha modificar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print "El nombre no se corresponde con ninguna liga"
        else:
            print "Introduzca los nuevos datos:"
            nombre = raw_input("Nombre: ")
            anio = raw_input("Anio: ")
            pais = raw_input("Pais: ")
            l.set_nombre(nombre)
            l.set_anio(anio)
            l.set_pais(pais)
            print "Liga modificada correctamente"

    def eliminar_liga(self):
        nombre = raw_input("Introduce el nombre de la liga a eliminar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print "El nombre no se corresponde con ninguna liga"
        else:
            self.ligas.remove(l)
            print "Liga eliminada correctamente"

    def consultar_liga(self):
        nombre = raw_input("Introduce el nombre de la liga a consultar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print "El nombre no se corresponde con ninguna liga"
        else:
            l.mostrar_liga()

    #MOSTRAR LISTAS
    def listar_ligas(self):
        for x in self.ligas:
            x.mostrar_liga()

    def listar_equipos(self):
        for x in self.equipos:
            x.mostrar_equipo()

    def listar_jugadores(self):
        for x in self.jugadores:
            x.mostrar_jugador()

    def listar_entrenadores(self):
        for x in self.entrenadores:
            x.mostrar_entrenador()

    def listar_estadios(self):
        for x in self.estadios:
            x.mostrar_estadio()

    def aniadir_jugador(self, j):
        self.jugadores.append(j)
        print "Jugador creado correctamente"

    def aniadir_entrenador(self, j):
        self.entrenadores.append(j)
        print "Entrenador creado correctamente"

    def aniadir_equipo(self, j):
        self.equipos.append(j)
        print "Equipo creado correctamente"

    def aniadir_liga(self, j):
        self.ligas.append(j)
        print "Liga creada correctamente"

    def aniadir_estadio(self, j):
        self.estadios.append(j)
        print "Estadio creado correctamente"