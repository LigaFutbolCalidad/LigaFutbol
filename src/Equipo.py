__author__ = 'Grupo 7'

class Equipo:
    def __init__(self,nombre,anioCreacion,ciudad):
        self.nombre=nombre
        self.anioCreacion=anioCreacion
        self.ciudad=ciudad
        self.puntos=0
        self.golesFavor=0
        self.golesContra=0
        self.partidosGanados=0
        self.partidosEmpatados=0
        self.partidosPerdidos=0
        self.estadio=None
        self.entrenador=None
        self.jugadores = []

    def get_nombre(self):
        return self.nombre

    def get_anioCreacion(self):
        return self.anioCreacion

    def get_ciudad(self):
        return self.ciudad

    def get_puntos(self):
        return self.puntos

    def get_golesFavor(self):
        return self.golesFavor

    def get_golesContra(self):
        return self.golesContra

    def get_partidosGanados(self):
        return self.partidosGanados

    def get_partidosPerdidos(self):
        return self.partidosPerdidos

    def get_partidosEmpatados(self):
        return self.partidosEmpatados

    def get_estadio(self):
        return self.estadio

    def get_entrenador(self):
        return self.entrenador

    def get_jugadores(self):
        return self.jugadores

    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_anioCreacion(self,anioCreacion):
        self.anioCreacion=anioCreacion

    def set_ciudad(self,ciudad):
        self.ciudad=ciudad

    def set_puntos(self,puntos):
        self.puntos=puntos

    def set_golesFavor(self,golesFavor):
        self.golesFavor=golesFavor

    def set_golesContra(self,golesContra):
        self.golesContra=golesContra

    def set_partidosGanados(self,partidosGanados):
        self.partidosGanados=partidosGanados

    def set_partidosPerdidos(self,partidosPerdidos):
        self.partidosPerdidos=partidosPerdidos

    def set_partidosEmpatados(self,partidosEmpatados):
        self.partidosEmpatados=partidosEmpatados

    def incrementar_puntos(self,puntos):
         self.puntos+=puntos

    def incrementar_goles_favor(self,goles):
        self.golesFavor+=goles

    def incrementar_goles_contra(self,goles):
        self.golesContra+=goles

    def incrementar_partidos_ganados(self):
         self.partidosGanados+=1

    def incrementar_partidos_empatados(self):
        self.partidosEmpatados+=1

    def incrementar_partidos_perdidos(self):
        self.partidosPerdidos+=1

    def asignar_estadio(self,estadio):
        self.estadio=estadio
        print "Estadio asignado al equipo correctamente."

    def asignar_entrenador(self,entrenador):
        self.entrenador=entrenador
        print "Entrenador asignado al equipo correctamente."

    def agregar_jugador(self,jugador):
        if len(self.jugadores) < 11:
            if (self.existeJugador(jugador.get_dni()) == None):
                self.jugadores.append(jugador)
                print "Jugador aniadido al equipo correctamente."
            else:
                print "El jugador ya pertenece al equipo."
        else:
            print "El equipo ya esta completo."

    def pichichi_equipo(self):
        max = 0
        pichichi = None
        for i in self.jugadores:
            if (i.get_golesMarcados() > max):
                max = i.get_golesMarcados()
                pichichi=i
        return pichichi

    def consultar_jugador(self,jugador):
        j = self.existeJugador(jugador.get_dni())
        if (j == None):
            print "El jugador no existe en el equipo."
        else:
            j.mostrar_jugador()

    def existeJugador(self,dni):
        jugador =  None
        for j in self.jugadores:
            if j.get_dni() == dni:
                jugador = j
        return jugador

    def listar_jugadores(self):
        if len(self.jugadores) > 0:
            for i in self.jugadores:
                i.mostrar_jugador()
        else:
            print "No hay jugadores en el equipo."

    def consultar_estadio(self):
        if self.estadio != None:
            self.estadio.mostrar_estadio()
        else:
            print "El equipo no tiene un estadio asignado."

    def consultar_entrenador(self):
        if self.entrenador != None:
            self.entrenador.mostrar_entrenador()
        else:
            print "El equipo no tiene entrenador asignado."

    def mostrar_equipo(self):
        cad=str(self)
        print cad

    def __str__(self):
        return "EQUIPO:\n\tNombre: " + self.get_nombre() + "\n\tAnio creacion: " + self.get_anioCreacion() + "\n\tCiudad: " \
               + self.get_ciudad() + "\n\tPuntos: " + str(self.get_puntos()) + "\n\tGoles a favor: " + str(self.get_golesFavor()) + "\n\tGoles en contra: " \
                + str(self.get_golesContra()) + "\n\tPartidos ganados: " + str(self.get_partidosGanados()) + "\n\tPartidos perdidos: " \
                + str(self.get_partidosPerdidos()) + "\n\tPartidos empatados: " + str(self.get_partidosEmpatados())

    def __cmp__( self, other ):
        cmp=self.get_puntos() - other.get_puntos()
        if cmp==0:
            cmp=self.get_golesFavor() - other.get_golesFavor()
            if cmp==0:
                cmp=other.get_golesContra() - self.get_golesContra()
        return cmp
