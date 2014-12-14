__author__ = 'Grupo 7'

from src.Partido import *
import random


class Liga:
    def __init__(self, nombre, anio, pais):
        self.nombre = nombre
        self.anio = anio
        self.pais = pais
        self.equipos = []
        self.partidos = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_anio(self):
        return self.anio

    def set_anio(self, anio):
        self.anio = anio

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def get_equipos(self):
        return self.equipos

    def existe_equipo(self, nombre):
        equipo = None
        for e in self.equipos:
            if e.get_nombre() == nombre:
                equipo = e
        return equipo

    def aniadir_equipo(self, equipo):
        if self.existe_equipo(equipo.get_nombre()) is None:
            if len(self.equipos) == 4:
                print ("No se pueden aniadir mas equipos a la liga.")
            else:
                self.equipos.append(equipo)
                print ("Equipo aniadido correctamente.")
                if len(self.equipos) == 4:
                    self.crear_partidos()
        else:
            print ("El equipo ya esta aniadido en la liga.")

    def crear_partidos(self):
        i = 0
        for x in self.equipos:
            for y in self.equipos:
                equipo_local = x.get_nombre()
                equipo_visitante = y.get_nombre()
                if x.get_nombre() != y.get_nombre():
                    i += 1
                    p = Partido(i, equipo_local, equipo_visitante)
                    self.partidos.append(p)

    def listar_equipos(self):
        for equipo in self.equipos:
            equipo.mostrar_equipo()

    @staticmethod
    def consultar_equipo(equipo):
        equipo.mostrar_equipo()

    def listar_partidos(self):
        for partido in self.partidos:
            partido.mostrar_partido()

    def consultar_calendario(self):
        for partido in self.partidos:
            if not partido.get_jugado():
                partido.mostrar_partido()

    def consultar_clasificacion(self):
        self.get_equipos().sort(reverse=True)
        igual = "=" * 20
        lin = "-" * 53
        print ("\n" + igual + "CLASIFICACION" + igual)
        print ("EQUIPO\t\t\t\tG\tE\tP\tGF\tGC\tPUNTOS\n" + lin)
        for e in self.equipos:
            tam = len(e.get_nombre())
            space = " " * (20 - tam)
            cadena = e.get_nombre() + space + str(e.get_partidosGanados()) + "\t" + str(e.get_partidosEmpatados())
            cadena += "\t" + str(e.get_partidosPerdidos()) + "\t" + str(e.get_golesFavor())
            cadena += "\t" + str(e.get_golesContra()) + "\t" + str(e.get_puntos())
            print (cadena)

    def existe_partido(self, jornada):
        partido = None
        for p in self.partidos:
            if p.get_jornada() == jornada:
                partido = p
        return partido

    @staticmethod
    def consultar_partido(partido):
        partido.mostrar_partido()

    def jugar_partido(self):
        jornada = input("Seleccione la jornada: ")
        p = self.existe_partido(jornada)
        if p is None:
            print ("La jornada no coincide con ninguna de la liga")
        else:
            if p.get_jugado():
                print ("El partido ya se ha jugado")
            else:
                local = self.existe_equipo(p.get_equipoLocal())
                visitante = self.existe_equipo(p.get_equipoVisitante())
                p.mostrar_partido()

                goles_local = self.cofig_partido_local(local)
                goles_visitante = self.cofig_partido_visitante(visitante)

                local.incrementar_goles_contra(goles_visitante)
                visitante.incrementar_goles_contra(goles_local)

                if goles_local == goles_visitante:
                    local.incrementar_partidos_empatados()
                    visitante.incrementar_partidos_empatados()
                    local.incrementar_puntos(2)
                    visitante.incrementar_puntos(2)
                elif goles_local > goles_visitante:
                    local.incrementar_puntos(3)
                    local.incrementar_partidos_ganados()
                    visitante.incrementar_partidos_perdidos()
                else:
                    visitante.incrementar_puntos(3)
                    visitante.incrementar_partidos_ganados()
                    local.incrementar_partidos_perdidos()
                p.set_golesLocales(goles_local)
                p.set_golesVisitantes(goles_visitante)
                p.set_jugado(True)

    @staticmethod
    def cofig_partido_local(local):
        goles_local = -1
        while goles_local < 0:
            goles_local = input("Inserte los goles marcados del equipo local: ")
            if goles_local < 0:
                print ("Goles incorrectos")
        x = 1
        while x <= goles_local:
            dni = raw_input(
                "Inserte el dni del jugador que ha marcado el gol " + str(x) + " del equipo local: ")
            j = local.existeJugador(dni)
            if j is None:
                print ("El jugador no existe")
            else:
                j.incrementar_goles()
                x += 1
        local.incrementar_goles_favor(goles_local)
        return goles_local

    @staticmethod
    def cofig_partido_visitante(visitante):
        goles_visitante = -1
        while goles_visitante < 0:
            goles_visitante = input("Inserte los goles marcados del equipo visitante: ")
            if goles_visitante < 0:
                print ("Goles incorrectos")
        x = 1
        while x <= goles_visitante:
            dni = raw_input(
                "Inserte el dni del jugador que ha marcado el gol " + str(x) + " del equipo visitante:")
            j = visitante.existeJugador(dni)
            if j is None:
                print ("El jugador no existe")
            else:
                j.incrementar_goles(1)
                x += 1
        visitante.incrementar_goles_favor(goles_visitante)
        return goles_visitante

    def jugar_partidos_auto(self):
        for p in self.partidos:
            if not p.get_jugado():
                g1 = random.randint(0, 5)
                l = self.existe_equipo(p.get_equipoLocal())
                p.set_golesLocales(g1)
                for i in range(0, g1):
                    indice = random.randint(0, len(l.get_jugadores()) - 1)
                    l.get_jugadores()[indice].incrementar_goles()

                g2 = random.randint(0, 5)
                v = self.existe_equipo(p.get_equipoVisitante())
                p.set_golesVisitantes(g2)
                for i in range(0, g2):
                    indice = random.randint(0, len(v.get_jugadores()) - 1)
                    v.get_jugadores()[indice].incrementar_goles()

                l.incrementar_goles_favor(g1)
                v.incrementar_goles_favor(g2)
                l.incrementar_goles_contra(g2)
                v.incrementar_goles_contra(g1)

                if g1 == g2:
                    l.incrementar_puntos(1)
                    v.incrementar_puntos(1)
                    l.incrementar_partidos_empatados()
                    v.incrementar_partidos_empatados()
                elif g1 > g2:
                    l.incrementar_puntos(3)
                    l.incrementar_partidos_ganados()
                    v.incrementar_partidos_perdidos()
                else:
                    v.incrementar_puntos(3)
                    v.incrementar_partidos_ganados()
                    l.incrementar_partidos_perdidos()

                p.set_jugado(True)

    def consultar_mejor_estadio(self):
        capacidad_estadio = 0
        mayor_estadio = None
        for equipo in self.equipos:
            estadio = equipo.get_estadio()
            if estadio.get_capacidad() > capacidad_estadio:
                capacidad_estadio = estadio.get_capacidad()
                mayor_estadio = estadio
        if mayor_estadio is None:
            print ("Ningun equipo tiene estadio")
        else:
            print ("El estadio con mayor capacidad es: " + mayor_estadio.get_nombre())

    def pichichi_liga(self):
        pichichi = None
        if len(self.equipos) > 0:
            self.recorrer_equipos(pichichi)
            if pichichi is not None:
                print ("El pichichi de la liga con " + str(pichichi.get_golesMarcados()) + " goles marcados es: ")
                pichichi.mostrar_jugador()
            else:
                print ("La liga no tiene pichichi aun.")
        else:
            print ("La liga no tiene equipos aun.")

    def recorrer_equipos(self, pichichi):
        goles = 0
        for equipo in self.equipos:
            jugador = equipo.pichichi_equipo()
            if jugador is not None and jugador.get_golesMarcados() > goles:
                goles = jugador.get_golesMarcados()
                pichichi = jugador
        return pichichi

    def listar_pichichis_equipos(self):
        for e in self.get_equipos():
            if e.pichichi_equipo() is not None:
                e.pichichi_equipo().mostrar_jugador()

    def mostrar_liga(self):
        cad = str(self)
        print (cad)

    def __str__(self):
        return "LIGA: \n\tNombre: " + self.nombre + "\n\tAnio: " + str(self.anio) + "\n\tPais: " + self.pais