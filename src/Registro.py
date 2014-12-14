__author__ = 'Grupo 7'
from src.Jugador import *
from src.Entrenador import *
from src.Estadio import *
from src.Equipo import *
from src.Liga import *


class Registro:
    """
    Clase Registro
    """
    def __init__(self):
        """
        Constructor

        Inicializa el constructor de Registro
        :param ligas: Lista que contiene ligas
        :type ligas: list
        :param equipos: Lista que contiene equipos
        :type equipos: list
        :param jugadores: Lista que contiene jugadores
        :type jugadores: list
        :param entrenadores: Lista que contiene entrenadores
        :type estadios: list
        :param estadios: Lista que contiene estadios
        :type estadios: list
        """
        self.ligas = []
        self.equipos = []
        self.jugadores = []
        self.entrenadores = []
        self.estadios = []

    # CRUD JUGADOR
    def existe_jugador(self, dni):
        """
        Metodo existe_jugador

        Comprueba que existe un jugador en la lista de jugadores del registro
        :param dni: Dni del jugador
        :type dni: String
        :return: jugador
        :rtype: Jugador
        """
        jugador = None
        for j in self.jugadores:
            if j.get_dni() == dni:
                jugador = j
        return jugador

    def crear_jugador(self):
        """
        Metodo crear_jugador

        Crea un nuevo jugador y lo aniade a la lista de jugadores del registro
        :var nombre: Nombre del jugador
        :type nombre: String
        :var apellidos: Apellidos del jugador
        :type apellidos: String
        :var dni: Dni del jugador
        :type dni: String
        :var fecha_nac: Fecha de nacimiento del jugador
        :type fecha_nac: String
        :var pais_nac: Pais de nacimiento del jugador
        :type pais_nac: String
        :var dorsal: Dorsal del jugador
        :type dorsal: int
        :var posicion: Posicion de juego del jugador
        :type posicion: String
        """
        nombre = raw_input("Indique el nombre del jugador: ")
        apellidos = raw_input("Indique los apellidos del jugador: ")
        dni = raw_input("Indique el dni del jugador: ")
        fecha_nac = raw_input("Indique la fecha de nacimiento del jugador: ")
        pais_nac = raw_input("Indique el pais de nacimiento del jugador: ")
        dorsal = input("Indique el dorsal del jugador: ")
        posicion = raw_input("Indique la posicion de juego: ")
        if self.existe_jugador(dni) is not None:
            print ("El jugador ya existe")
        else:
            j = Jugador(nombre, apellidos, dni, fecha_nac, pais_nac, dorsal, posicion)
            self.aniadir_jugador(j)

    def modificar_jugador(self):
        """
        Metodo modificar_jugador

        Modifica un jugador ya existente en la lista de jugadores del registro
        :var dni: Dni del jugador a modificar
        :type dni: String
        :var nombre: Nuevo nombre del jugador
        :type nombre: String
        :var apellidos: Nuevos apellidos del jugador
        :type apellidos: String
        :var fecha_nac: Nueva fecha de nacimiento del jugador
        :type fecha_nac: String
        :var pais_nac: Nuevo pais de nacimiento del jugador
        :type pais_nac: String
        :var dorsal: Nuevo dorsal del jugador
        :type dorsal: int
        :var posicion: Nueva posicion de juego del jugador
        :type posicion: String
        """
        dni = raw_input("Introduce el dni del jugador ha modificar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print ("El dni no se corresponde con ningun jugador")
        else:
            print ("Introduzca los nuevos datos:")
            nombre = raw_input("Nombre: ")
            apellidos = raw_input("Apellidos: ")
            fecha_nac = raw_input("Fecha nacimiento: ")
            pais_nac = raw_input("Pais de nacimiento: ")
            dorsal = input("Dorsal: ")
            posicion = raw_input("Posicion: ")
            j.set_nombre(nombre)
            j.set_apellidos(apellidos)
            j.set_fecha_nac(fecha_nac)
            j.set_pais_nac(pais_nac)
            j.set_dorsal(dorsal)
            j.set_posicion(posicion)
            print ("Jugador modificado correctamente")

    def eliminar_jugador(self):
        """
        Metodo eliminar_jugador

        Elimina un jugador (existente) en la lista de jugadores del registro
        :var dni: Dni del jugador a eliminar
        :type dni: String
        """
        dni = raw_input("Introduce el dni del jugador a eliminar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print ("El dni no se corresponde con ningun jugador")
        else:
            self.jugadores.remove(j)
            print ("Jugador eliminado correctamente")

    def consultar_jugador(self):
        """
        Metodo consultar_jugador

        Consulta los datos un jugador (existente) en la lista de jugadores del registro
        :var dni: Dni del jugador a consultar
        :type dni: String
        """
        dni = raw_input("Introduce el dni del jugador a consultar: ")
        j = self.existe_jugador(dni)
        if j is None:
            print ("El dni no se corresponde con ningun jugador")
        else:
            j.mostrar_jugador()

    #CRUD ENTRENADOR
    def existe_entrenador(self, dni):
        """
        Metodo existe_entrenador

        Comprueba que existe un entrenador en la lista de entrenadores del registro
        :param dni: Dni del entrenador
        :type dni: String
        :return: entrenador
        :rtype: Entrenador
        """
        entrenador = None
        for e in self.entrenadores:
            if e.get_dni() == dni:
                entrenador = e
        return entrenador

    def crear_entrenador(self):
        """
        Metodo crear_entrenador

        Crea un nuevo entrenador y lo aniade a la lista de entrenadores del registro
        :var nombre: Nombre del entrenador
        :type nombre: String
        :var apellidos: Apellidos del entrenador
        :type apellidos: String
        :var dni: Dni del entrenador
        :type dni: String
        :var fecha_nac: Fecha de nacimiento del entrenador
        :type fecha_nac: String
        :var pais_nac: Pais de nacimiento del entrenador
        :type pais_nac: String
        :var licencia: Licencia del entrenador
        :type licencia: String
        """
        nombre = raw_input("Indique el nombre del entrenador: ")
        apellidos = raw_input("Indique los apellidos del entrenador: ")
        dni = raw_input("Indique el dni del entrenador: ")
        fecha_nac = raw_input("Indique la fecha de nacimiento del entrenador: ")
        pais_nac = raw_input("Indique el pais de nacimiento del entrenador: ")
        licencia = raw_input("Indique la licecia del entrenador: ")
        if self.existe_entrenador(dni) is not None:
            print ("El entrenador ya existe")
        else:
            e = Entrenador(nombre, apellidos, dni, fecha_nac, pais_nac, licencia)
            self.aniadir_entrenador(e)

    def modificar_entrenador(self):
        """
        Metodo modificar_entrenador

        Modifica un entrenador ya existente en la lista de entrenadores del registro
        :var dni: Dni del entrenador a modificar
        :type dni: String
        :var nombre: Nuevo nombre del entrenador
        :type nombre: String
        :var apellidos: Nuevos apellidos del entrenador
        :type apellidos: String
        :var fecha_nac: Nueva fecha de nacimiento del entrenador
        :type fecha_nac: String
        :var pais_nac: Nuevo pais de nacimiento del entrenador
        :type pais_nac: String
        :var licencia: Nueva licencia del entrenador
        :type licencia: String
        """
        dni = raw_input("Introduce el dni del entrenador ha modificar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print ("El dni no se corresponde con ningun entrenador")
        else:
            print ("Introduzca los nuevos datos:")
            nombre = raw_input("Nombre: ")
            apellidos = raw_input("Apellidos: ")
            fecha_nac = raw_input("Fecha nacimiento: ")
            pais_nac = raw_input("Pais de nacimiento: ")
            licencia = raw_input("Licencia: ")
            e.set_nombre(nombre)
            e.set_apellidos(apellidos)
            e.set_fecha_nac(fecha_nac)
            e.set_pais_nac(pais_nac)
            e.set_licencia(licencia)
            print ("Entrenador modificado correctamente")

    def eliminar_entrenador(self):
        """
        Metodo eliminar_entrenador

        Elimina un entrenador (existente) en la lista de entrenadores del registro
        :var dni: Dni del entrenador a eliminar
        :type dni: String
        """
        dni = raw_input("Introduce el dni del entrenador a eliminar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print ("El dni no se corresponde con ningun entrenador")
        else:
            self.entrenadores.remove(e)
            print ("Entrenador eliminado correctamente")

    def consultar_entrenador(self):
        """
        Metodo consultar_entrenador

        Consulta los datos un entrenador (existente) en la lista de entrenadores del registro
        :var dni: Dni del entrenador a consultar
        :type dni: String
        """
        dni = raw_input("Introduce el dni del entrenador a consultar: ")
        e = self.existe_entrenador(dni)
        if e is None:
            print ("El dni no se corresponde con ningun entrenador")
        else:
            e.mostrar_entrenador()

    #CRUD ESTADIO
    def existe_estadio(self, nombre):
        """
        Metodo existe_estadio

        Comprueba que existe un estadio en la lista de estadios del registro
        :param nombre: Nombre del estadio
        :type nombre: String
        :return: estadio
        :rtype: Estadio
        """
        estadio = None
        for e in self.estadios:
            if e.get_nombre() == nombre:
                estadio = e
        return estadio

    def crear_estadio(self):
        """
        Metodo crear_estadio

        Crea un nuevo estadio y lo aniade a la lista de estadios del registro
        :var nombre: Nombre del estadio
        :type nombre: String
        :var ciudad: Ciudad del estadio
        :type ciudad: String
        :var capacidad: Capacidad del estadio
        :type capacidad: String
        """
        nombre = raw_input("Indique el nombre del estadio: ")
        ciudad = raw_input("Indique la ciudad del estadio: ")
        capacidad = input("Indique la capacidad del estadio: ")
        if self.existe_estadio(nombre) is not None:
            print ("El estadio ya existe")
        else:
            e = Estadio(nombre, ciudad, capacidad)
            self.aniadir_estadio(e)

    def modificar_estadio(self):
        """
        Metodo modificar_estadio

        Modifica un estadio ya existente en la lista de estadios del registro
        :var nombre: Nombre del estadio a modificar
        :type nombre: String
        :var ciudad: Nueva ciudad del estadio
        :type ciudad: String
        :var capacidad: Nueva capacidad del estadio
        :type capacidad: int
        """
        nombre = raw_input("Introduce el nombre del estadio ha modificar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun estadio")
        else:
            print ("Introduzca los nuevos datos:")
            ciudad = raw_input("Ciudad: ")
            capacidad = input("Capacidad: ")
            e.set_ciudad(ciudad)
            e.set_capacidad(capacidad)
            print ("Estadio modificado correctamente")

    def eliminar_estadio(self):
        """
        Metodo eliminar_estadio

        Elimina un estadio (existente) en la lista de estadios del registro
        :var nombre: Nombre del estadio a eliminar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre del estadio a eliminar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun estadio")
        else:
            self.estadios.remove(e)
            print ("Estadio eliminado correctamente")

    def consultar_estadio(self):
        """
        Metodo consultar_estadio

        Consulta los datos un estadio (existente) en la lista de estadios del registro
        :var nombre: Nombre del estadio a consultar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre del estadio a consultar: ")
        e = self.existe_estadio(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun estadio")
        else:
            e.mostrar_estadio()

    #CRUD EQUIPO
    def existe_equipo(self, nombre):
        """
        Metodo existe_equipo

        Comprueba que existe un equipo en la lista de equipos del registro
        :param nombre: Nombre del equipo
        :type nombre: String
        :return: equipo
        :rtype: Equipo
        """
        equipo = None
        for e in self.equipos:
            if e.get_nombre() == nombre:
                equipo = e
        return equipo

    def crear_equipo(self):
        """
        Metodo crear_equipo

        Crea un nuevo equipo y lo aniade a la lista de equipos del registro
        :var nombre: Nombre del equipo
        :type nombre: String
        :var anio_creacion: Anio de creacion del equipo
        :type anio_creacion: String
        :var ciudad: Ciudad del equipo
        :type ciudad: String
        """
        nombre = raw_input("Indique el nombre del equipo: ")
        anio_creacion = raw_input("Indique el anio de creacion del equipo: ")
        ciudad = raw_input("Indique la ciudad del equipo: ")
        if self.existe_equipo(nombre) is not None:
            print ("El equipo ya existe")
        else:
            e = Equipo(nombre, anio_creacion, ciudad)
            self.aniadir_equipo(e)

    def modificar_equipo(self):
        """
        Metodo modificar_equipo

        Modifica un equipo ya existente en la lista de equipos del registro
        :var nombre: Nombre del equipo a modificar
        :type nombre: String
        :var anio_creacion: Nuevo anio de creacion del equipo
        :type anio_creacion: String
        :var ciudad: Nueva ciudad del equipo
        :type ciudad: String
        """
        nombre = raw_input("Introduce el nombre del equipo ha modificar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun equipo")
        else:
            print ("Introduzca los nuevos datos:")
            anio_creacion = raw_input("Anio creacion: ")
            ciudad = raw_input("Ciudad: ")
            e.set_anio_creacion(anio_creacion)
            e.set_ciudad(ciudad)
            print ("Equipo modificado correctamente")

    def eliminar_equipo(self):
        """
        Metodo eliminar_equipo

        Elimina un equipo (existente) en la lista de equipos del registro
        :var nombre: Nombre del equipo a eliminar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre del equipo a eliminar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun equipo")
        else:
            self.equipos.remove(e)
            print ("Equipo eliminado correctamente")

    def consultar_equipo(self):
        """
        Metodo consultar_equipo

        Consulta los datos un equipo (existente) en la lista de equipos del registro
        :var nombre: Nombre del equipo a consultar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre del equipo a consultar: ")
        e = self.existe_equipo(nombre)
        if e is None:
            print ("El nombre no se corresponde con ningun equipo")
        else:
            e.mostrar_equipo()

    #CRUD LIGA
    def existe_liga(self, nombre):
        """
        Metodo existe_liga

        Comprueba que existe una liga en la lista de ligas del registro
        :param nombre: Nombre de la liga
        :type nombre: String
        :return: liga
        :rtype: Liga
        """
        liga = None
        for l in self.ligas:
            if l.get_nombre() == nombre:
                liga = l
        return liga

    def crear_liga(self):
        """
        Metodo crear_liga

        Crea una nueva liga y la aniade a la lista de ligas del registro
        :var nombre: Nombre de la liga
        :type nombre: String
        :var anio: Anio de la liga
        :type anio: String
        :var pais: Pais de la liga
        :type pais: String
        """
        nombre = raw_input("Indique el nombre de la liga: ")
        anio = raw_input("Indique el anio de la liga: ")
        pais = raw_input("Indique el pais de la liga: ")
        if self.existe_liga(nombre) is not None:
            print ("La liga ya existe")
        else:
            l = Liga(nombre, anio, pais)
            self.aniadir_liga(l)

    def modificar_liga(self):
        """
        Metodo modificar_liga

        Modifica una liga ya existente en la lista de ligas del registro
        :var nombre: Nombre de la liga a modificar
        :type nombre: String
        :var anio: Nuevo anio de la liga
        :type anio: String
        :var pais: Nuevo pais de la liga
        :type pais: String
        """
        nombre = raw_input("Introduce el nombre de la liga ha modificar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print ("El nombre no se corresponde con ninguna liga")
        else:
            print ("Introduzca los nuevos datos:")
            anio = raw_input("Anio: ")
            pais = raw_input("Pais: ")
            l.set_anio(anio)
            l.set_pais(pais)
            print ("Liga modificada correctamente")

    def eliminar_liga(self):
        """
        Metodo eliminar_liga

        Elimina una liga (existente) en la lista de ligas del registro
        :var nombre: Nombre de la liga a eliminar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre de la liga a eliminar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print ("El nombre no se corresponde con ninguna liga")
        else:
            self.ligas.remove(l)
            print ("Liga eliminada correctamente")

    def consultar_liga(self):
        """
        Metodo consultar_liga

        Consulta los datos una liga (existente) en la lista de ligas del registro
        :var nombre: Nombre de la liga a consultar
        :type nombre: String
        """
        nombre = raw_input("Introduce el nombre de la liga a consultar: ")
        l = self.existe_liga(nombre)
        if l is None:
            print ("El nombre no se corresponde con ninguna liga")
        else:
            l.mostrar_liga()

    #MOSTRAR LISTAS
    def listar_ligas(self):
        """
        Metodo listar_ligas

        Muestra todas las ligas de la lista de ligas del registro
        """
        for x in self.ligas:
            x.mostrar_liga()

    def listar_equipos(self):
        """
        Metodo listar_ligas

        Muestra todas las ligas de la lista de ligas del registro
        """
        for x in self.equipos:
            x.mostrar_equipo()

    def listar_jugadores(self):
        """
        Metodo listar_jugadores

        Muestra todss los jugadores de la lista de jugadores del registro
        """
        for x in self.jugadores:
            x.mostrar_jugador()

    def listar_entrenadores(self):
        """
        Metodo listar_entrenadores

        Muestra todos los entrenadores de la lista de entrenadores del registro
        """
        for x in self.entrenadores:
            x.mostrar_entrenador()

    def listar_estadios(self):
        """
        Metodo listar_estadios

        Muestra todos los estadios de la lista de estadios del registro
        """
        for x in self.estadios:
            x.mostrar_estadio()

    def aniadir_jugador(self, j):
        """
        Metodo aniadir_jugador

        Aniade un jugador a la lista de jugadores del registro
        :param j: Un jugador
        :type j: Jugador
        """
        self.jugadores.append(j)
        print ("Jugador creado correctamente")

    def aniadir_entrenador(self, j):
        """
        Metodo aniadir_entrenador

        Aniade un entrenador a la lista de entrenadores del registro
        :param j: Un entrenador
        :type j: Entrenador
        """
        self.entrenadores.append(j)
        print ("Entrenador creado correctamente")

    def aniadir_equipo(self, j):
        """
        Metodo aniadir_jugador

        Aniade un equipo a la lista de equipos del registro
        :param j: Un equipo
        :type j: Equipo
        """
        self.equipos.append(j)
        print ("Equipo creado correctamente")

    def aniadir_liga(self, j):
        """
        Metodo aniadir_jugador

        Aniade una liga a la lista de ligas del registro
        :param j: Una liga
        :type j: Liga
        """
        self.ligas.append(j)
        print ("Liga creada correctamente")

    def aniadir_estadio(self, j):
        """
        Metodo aniadir_jugador

        Aniade un estadio a la lista de estadios del registro
        :param j: Un estadio
        :type j: Estadio
        """
        self.estadios.append(j)
        print ("Estadio creado correctamente")