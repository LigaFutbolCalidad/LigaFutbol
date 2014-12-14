__author__ = 'Equipo de Calidad'


class Equipo:
    def __init__(self, nombre, anio_creacion, ciudad):
        self.nombre = nombre
        self.anioCreacion = anio_creacion
        self.ciudad = ciudad
        self.puntos = 0
        self.golesFavor = 0
        self.golesContra = 0
        self.partidosGanados = 0
        self.partidosEmpatados = 0
        self.partidosPerdidos = 0
        self.estadio = None
        self.entrenador = None
        self.jugadores = []

    def get_nombre(self):
        return self.nombre

    def get_anio_creacion(self):
        return self.anioCreacion

    def get_ciudad(self):
        return self.ciudad

    def get_puntos(self):
        return self.puntos

    def get_goles_favor(self):
        return self.golesFavor

    def get_goles_contra(self):
        return self.golesContra

    def get_partidos_ganados(self):
        return self.partidosGanados

    def get_partidos_perdidos(self):
        return self.partidosPerdidos

    def get_partidos_empatados(self):
        return self.partidosEmpatados

    def get_estadio(self):
        return self.estadio

    def get_entrenador(self):
        return self.entrenador

    def get_jugadores(self):
        return self.jugadores

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_anio_creacion(self, anio_creacion):
        self.anioCreacion = anio_creacion

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_puntos(self, puntos):
        self.puntos = puntos

    def set_goles_favor(self, goles_favor):
        self.golesFavor = goles_favor

    def set_goles_contra(self, goles_contra):
        self.golesContra = goles_contra

    def set_partidos_ganados(self, partidos_ganados):
        self.partidosGanados = partidos_ganados

    def set_partidos_perdidos(self, partidos_perdidos):
        self.partidosPerdidos = partidos_perdidos

    def set_partidos_empatados(self, partidos_empatados):
        self.partidosEmpatados = partidos_empatados

    def incrementar_puntos(self, puntos):
        self.puntos += puntos

    def incrementar_goles_favor(self, goles):
        self.golesFavor += goles

    def incrementar_goles_contra(self, goles):
        self.golesContra += goles

    def incrementar_partidos_ganados(self):
        self.partidosGanados += 1

    def incrementar_partidos_empatados(self):
        self.partidosEmpatados += 1

    def incrementar_partidos_perdidos(self):
        self.partidosPerdidos += 1

    def asignar_estadio(self, estadio):
        self.estadio = estadio
        print ("Estadio asignado al equipo correctamente.")

    def asignar_entrenador(self, entrenador):
        self.entrenador = entrenador
        print ("Entrenador asignado al equipo correctamente.")

    def agregar_jugador(self, jugador):
        if len(self.jugadores) < 11:
            if self.existe_jugador(jugador.get_dni()) is None:
                self.jugadores.append(jugador)
                print ("Jugador aniadido al equipo correctamente.")
            else:
                print ("El jugador ya pertenece al equipo.")
        else:
            print ("El equipo ya esta completo.")

    def pichichi_equipo(self):
        max = 0
        pichichi = None
        for i in self.jugadores:
            if i.get_golesMarcados() > max:
                max = i.get_golesMarcados()
                pichichi = i
        return pichichi

    def consultar_jugador(self, jugador):
        j = self.existe_jugador(jugador.get_dni())
        if j is None:
            print ("El jugador no existe en el equipo.")
        else:
            j.mostrar_jugador()

    def existe_jugador(self, dni):
        jugador = None
        for j in self.jugadores:
            if j.get_dni() == dni:
                jugador = j
        return jugador

    def listar_jugadores(self):
        if len(self.jugadores) > 0:
            for i in self.jugadores:
                i.mostrar_jugador()
        else:
            print ("No hay jugadores en el equipo.")

    def consultar_estadio(self):
        if self.estadio is not None:
            self.estadio.mostrar_estadio()
        else:
            print ("El equipo no tiene un estadio asignado.")

    def consultar_entrenador(self):
        if self.entrenador is not None:
            self.entrenador.mostrar_entrenador()
        else:
            print ("El equipo no tiene entrenador asignado.")

    def mostrar_equipo(self):
        cad = str(self)
        print (cad)

    def __str__(self):
        return "EQUIPO:\n\tNombre: " + self.get_nombre() + "\n\tAnio creacion: " + self.get_anio_creacion() \
               + "\n\tCiudad: " + self.get_ciudad() + "\n\tPuntos: " + str(self.get_puntos()) + "\n\tGoles a favor: " \
               + str(self.get_goles_favor()) + "\n\tGoles en contra: " + str(self.get_goles_contra()) \
               + "\n\tPartidos ganados: " + str(self.get_partidos_ganados()) + "\n\tPartidos perdidos: " \
               + str(self.get_partidos_perdidos()) + "\n\tPartidos empatados: " + str(self.get_partidos_empatados())

    def __cmp__(self, other):
        res = self.get_puntos() - other.get_puntos()
        if res == 0:
            res = self.get_goles_favor() - other.get_golesFavor()
            if res == 0:
                res = other.get_golesContra() - self.get_goles_contra()
        return res
