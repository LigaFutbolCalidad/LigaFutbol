__author__ = 'Grupo 7'

class Partido:
    def __init__(self,jornada,equipoLocal,equipoVisitante):
       self.jornada=jornada
       self.equipoLocal=equipoLocal
       self.equipoVisitante=equipoVisitante
       self.golesLocales = 0
       self.golesVisitantes = 0
       self.jugado = False

    def get_jornada(self):
        return self.jornada

    def get_equipoLocal(self):
        return self.equipoLocal

    def get_equipoVisitante(self):
       return self.equipoVisitante

    def get_golesLocales(self):
       return self.golesLocales

    def get_golesVisitantes(self):
       return self.golesVisitantes

    def get_jugado(self):
        return self.jugado

    def set_jornada(self,jornada):
       self.jornada=jornada

    def set_equipoLocal(self,equipo):
        self.equipoLocal=equipo

    def set_equipoVisitante(self,equipo):
        self.equipoVisitante=equipo

    def set_golesLocales(self,goles):
        self.golesLocales=goles

    def set_golesVisitantes(self,goles):
        self.golesVisitantes=goles

    def set_jugado(self,jug):
        self.jugado=jug

    def mostrar_partido(self):
        cad=str(self)
        print cad

    def __str__(self):
        if self.jugado == False:
            return "PARTIDO:\n\tJornada: " + str(self.get_jornada()) + "\n\tEquipo local: " + self.get_equipoLocal() + "\n\tEquipo visitante: " + self.get_equipoVisitante()
        else:
            return "PARTIDO:\n\tJornada: " + str(self.get_jornada()) + "\n\tEquipo local: " + self.get_equipoLocal() + "\n\tEquipo visitante: " + self.get_equipoVisitante() + "\n\tGoles local: " + str(self.get_golesLocales()) + "\n\tGoles visitante: " + str(self.get_golesVisitantes())