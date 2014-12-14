__author__ = 'Equipo de Calidad'


class Partido:
    def __init__(self, jornada, equipo_local, equipo_visitante):
        self.jornada = jornada
        self.equipoLocal = equipo_local
        self.equipoVisitante = equipo_visitante
        self.golesLocales = 0
        self.golesVisitantes = 0
        self.jugado = False

    def get_jornada(self):
        return self.jornada

    def get_equipo_local(self):
        return self.equipoLocal

    def get_equipo_visitante(self):
        return self.equipoVisitante

    def get_goles_locales(self):
        return self.golesLocales

    def get_goles_visitantes(self):
        return self.golesVisitantes

    def get_jugado(self):
        return self.jugado

    def set_jornada(self, jornada):
        self.jornada = jornada

    def set_equipo_local(self, equipo):
        self.equipoLocal = equipo

    def set_equipo_visitante(self, equipo):
        self.equipoVisitante = equipo

    def set_goles_locales(self, goles):
        self.golesLocales = goles

    def set_goles_visitantes(self, goles):
        self.golesVisitantes = goles

    def set_jugado(self, jug):
        self.jugado = jug

    def mostrar_partido(self):
        cad = str(self)
        print (cad)

    def __str__(self):
        if not self.jugado:
            return "PARTIDO:\n\tJornada: " + str(
                self.get_jornada()) + "\n\tEquipo local: " + self.get_equipo_local() + "\n\tEquipo visitante: " \
                + self.get_equipo_visitante()
        else:
            return "PARTIDO:\n\tJornada: " + str(
                self.get_jornada()) + "\n\tEquipo local: " + self.get_equipo_local() + "\n\tEquipo visitante: " \
                   + self.get_equipo_visitante() + "\n\tGoles local: " + str(
                self.get_goles_locales()) + "\n\tGoles visitante: " + str(self.get_goles_visitantes())