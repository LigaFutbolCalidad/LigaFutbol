from src.Registro import *

__author__ = 'Grupo 7'


#Funciones del menu manual
def administrar_jugadores():
    """
    Metodo administrar_jugadores

    Muestra un menu con todas las opciones para administrar un jugador en el registro
    """
    loop = False
    while not loop:
        print ("=" * 20)
        print ("ADMINISTRAR JUGADORES")
        print ("Que desea hacer: ")
        print ("1 - Crear un jugador")
        print ("2 - Modificar un jugador")
        print ("3 - Eliminar un jugador")
        print ("4 - Consultar un jugador")
        print ("5 - Ver todos los jugadores creados")
        print ("0 - Volver")
        opc1 = input("Opcion: ")
        if opc1 == 1:
            r.crear_jugador()
        elif opc1 == 2:
            r.modificar_jugador()
        elif opc1 == 3:
            r.eliminar_jugador()
        elif opc1 == 4:
            r.consultar_jugador()
        elif opc1 == 5:
            r.listar_jugadores()
        elif opc1 == 0:
            loop = True
            break
        else:
            print ("Opcion incorrecta")


def administrar_entrenadores():
    """
    Metodo administrar_entrenadores

    Muestra un menu con todas las opciones para administrar un entrenador en el registro
    """
    loop = False
    while not loop:
        print ("=" * 20)
        print ("ADMINISTRAR ENTRENADORES")
        print ("Que desea hacer: ")
        print ("1 - Crear entrenador")
        print ("2 - Modificar entrenador")
        print ("3 - Eliminar entrenador")
        print ("4 - Consultar entrenador")
        print ("5 - Ver todos los entrenadores creados")
        print ("0 - Volver")
        opc1 = input("Opcion: ")
        if opc1 == 1:
            r.crear_entrenador()
        elif opc1 == 2:
            r.modificar_entrenador()
        elif opc1 == 3:
            r.eliminar_entrenador()
        elif opc1 == 4:
            r.consultar_entrenador()
        elif opc1 == 5:
            r.listar_entrenadores()
        elif opc1 == 0:
            loop = True
            break
        else:
            print ("Opcion incorrecta")


def administrar_estadios():
    """
    Metodo administrar_estadios

    Muestra un menu con todas las opciones para administrar un estadio en el registro
    """
    loop = False
    while not loop:
        print ("=" * 20)
        print ("ADMINISTRAR ESTADIOS")
        print ("Que desea hacer: ")
        print ("1 - Crear estadio")
        print ("2 - Modificar estadio")
        print ("3 - Eliminar estadio")
        print ("4 - Consultar estadio")
        print ("5 - Ver todos los estadios creados")
        print ("0 - Volver")
        opc1 = input("Opcion: ")
        if opc1 == 1:
            r.crear_estadio()
        elif opc1 == 2:
            r.modificar_estadio()
        elif opc1 == 3:
            r.eliminar_estadio()
        elif opc1 == 4:
            r.consultar_estadio()
        elif opc1 == 5:
            r.listar_estadios()
        elif opc1 == 0:
            loop = True
            break
        else:
            print ("Opcion incorrecta")


def administrar_equipos():
    """
    Metodo administrar_equipos

    Muestra un menu con todas las opciones para administrar un equipo en el registro
    """
    loop = False
    while not loop:
        print ("=" * 20)
        print ("ADMINISTRAR EQUIPOS")
        print ("Que desea hacer: ")
        print ("1 - Crear un equipo")
        print ("2 - Modificar un equipo")
        print ("3 - Eliminar un equipo")
        print ("4 - Consultar un equipo")
        print ("5 - Ver todos los equipos creados")
        print ("0 - Volver")
        opc1 = input("Opcion: ")
        if opc1 == 1:
            r.crear_equipo()
        elif opc1 == 2:
            r.modificar_equipo()
        elif opc1 == 3:
            r.eliminar_equipo()
        elif opc1 == 4:
            r.consultar_equipo()
        elif opc1 == 5:
            r.listar_equipos()
        elif opc1 == 0:
            loop = True
            break
        else:
            print ("Opcion incorrecta")


def administrar_ligas():
    """
    Metodo administrar_ligas

    Muestra un menu con todas las opciones para administrar las ligas en el registro
    """
    loop = False
    while not loop:
        print ("=" * 20)
        print ("ADMINISTRAR LIGAS")
        print ("Que desea hacer: ")
        print ("1 - Crear liga")
        print ("2 - Modificar liga")
        print ("3 - Eliminar liga")
        print ("4 - Consultar liga")
        print ("5 - Ver todas las ligas creadas")
        print ("6 - Administrar una liga")
        print ("0 - Volver")
        opc1 = input("Opcion: ")
        if opc1 == 1:
            r.crear_liga()
        elif opc1 == 2:
            r.modificar_liga()
        elif opc1 == 3:
            r.eliminar_liga()
        elif opc1 == 4:
            r.consultar_liga()
        elif opc1 == 5:
            r.listar_ligas()
        elif opc1 == 6:
            liga = raw_input("Introduzca el nombre de la liga a administrar: ")
            l = r.existe_liga(liga)
            if l is None:
                print ("La liga no existe")
            else:
                administrar_liga(liga)
        elif opc1 == 0:
            loop = True
            break
        else:
            print ("Opcion incorrecta")


def administrar_liga(liga):
    """
    Metodo administrar_liga

    Muestra un menu con todas las opciones para administrar una liga en el registro
    :param liga: Una liga
    :type liga: Liga
    """
    loop1 = False
    while not loop1:
        print ("=" * 20)
        print ("ADMINISTRAR LIGA: " + liga)
        print ("Que desea hacer: ")
        print ("1 - Aniadir un equipo a la liga")
        print ("2 - Ver equipos de la liga")
        print ("3 - Consultar un equipo de la liga")
        print ("4 - Ver partidos de la liga")
        print ("5 - Consultar calendario de la liga")
        print ("6 - Consultar clasificacion de la liga")
        print ("7 - Consultar un partido de la liga")
        print ("8 - Jugar un partido de la liga")
        print ("9 - Consultar mejor estadio de la liga")
        print ("10 - Consultar pichichi de la liga")
        print ("11 - Consultar pichichi de un equipo de la liga")
        print ("0 - Volver")
        opc2 = input("Opcion: ")
        if opc2 == 1:
            equipo = raw_input("Introduzca el nombre del equipo que desea aniadir a la liga: ")
            e = r.existe_equipo(equipo)
            if e is None:
                print ("El equipo no existe (debe ser creado antes)")
            else:
                l.aniadir_equipo(e)
        elif opc2 == 2:
            l.listar_equipos()
        elif opc2 == 3:
            equipo = raw_input("Introduzca el nombre del equipo a consultar")
            e = l.existe_equipo(equipo)
            if e is None:
                print ("El equipo no esta en la liga")
            else:
                l.consultar_equipo(e)
        elif opc2 == 4:
            l.listar_partidos()
        elif opc2 == 5:
            l.consultar_calendario()
        elif opc2 == 6:
            l.consultar_clasificacion()
        elif opc2 == 7:
            jornada = input("Introduzca la jornada del partido a consultar: ")
            p = l.existePartido(jornada)
            if p is None:
                print ("La jornada no coincide con ninguna de la liga")
            else:
                l.consultar_partido(p)
        elif opc2 == 8:
            l.jugar_partido()
        elif opc2 == 9:
            l.consultar_mejor_estadio()
        elif opc2 == 10:
            l.pichichi_liga()
        elif opc2 == 11:
            equipo = raw_input("Introduzca el nombre del equipo a consultar el pichichi: ")
            e = l.existeEquipo(equipo)
            if e is None:
                print ("El equipo no esta en la liga")
            else:
                pichichi_equipo_liga(e)
        elif opc2 == 0:
            loop1 = True
            break
        else:
            print ("Opcion incorrecta")


def pichichi_equipo_liga(e):
    """
    Metodo pichichi_equipo_liga

    Metodo que devuelve el pichichi de un equipo de una liga del registro
    :param e: Un equipo
    :type e: Equipo
    """
    j = e.pichichi_equipo()
    if j is not None:
        j.mostrar_jugador()
    else:
        print ("El equipo no tiene pichichi aun.")


r=Registro()
print ("CARGANDO DATOS...")
#JUGADORES
j1 = Jugador("Leo","Messi","1234M","23/02/1980","Argentina",5,"delantero")
j2 = Jugador("Luis","Suarez","1234S","11/08/1985","Uruguay",12,"delantero")
j3 = Jugador("Neymar","Junior","1234J","19/02/1990","Brasil",15,"delantero")
j4 = Jugador("Cristiano","Ronaldo","1235R","23/02/1980","Portugal",7,"delantero")
j5 = Jugador("Sergio","Ramos","1236R","23/03/1983","Espania",12,"delantero")
j6 = Jugador("Marcelo","Vieira","1234V","24/02/1990","Brasil",5,"defensa")
j7 = Jugador("Alvaro","Negredo","1234N","23/02/1985","Espania",10,"delantero")
j8 = Jugador("Rodrigo","De Paul","1234D","23/02/1991","Espania",2,"centrocampista")
j9 = Jugador("Ruben","Vezo","1235V","03/11/1989","Portugal",3,"defensa")
j10 = Jugador("Carlos","Bacca","1234B","11/02/1985","Colombia",10,"delantero")
j11 = Jugador("Denis","Suarez","1237S","14/02/1992","Espania",5,"centrocampista")
j12 = Jugador("Jose Antonio","Reyes","1238R","14/02/1985","Espania",12,"delantero")
r.aniadirJugador(j1)
r.aniadirJugador(j2)
r.aniadirJugador(j3)
r.aniadirJugador(j4)
r.aniadirJugador(j5)
r.aniadirJugador(j6)
r.aniadirJugador(j7)
r.aniadirJugador(j8)
r.aniadirJugador(j9)
r.aniadirJugador(j10)
r.aniadirJugador(j11)
r.aniadirJugador(j12)

#ENTRENADORES
en1 = Entrenador("Pep","Guardiola","1234P","22/11/1975","Espania","1234L")
en2 = Entrenador("Carlos","Ancelloti","1234A","21/01/1970","Italia","1235L")
en3 = Entrenador("Nunu","Espirito Santo","1235E","20/11/1970","Brasil","1236L")
en4 = Entrenador("Unai","Emery","1236E","01/01/1970","Espania","1237L")
r.aniadir_entrenador(en1)
r.aniadir_entrenador(en2)
r.aniadir_entrenador(en3)
r.aniadir_entrenador(en4)

#ESTADIOS
es1 = Estadio("Camp Nou","Barcelona",1650300)
es2 = Estadio("Bernabeu","Madrid",1500200)
es3 = Estadio("Mestalla","Valencia",1560200)
es4 = Estadio("Sanchez-Pizjuan","Sevilla",1100250)
r.aniadir_estadio(es1)
r.aniadir_estadio(es2)
r.aniadir_estadio(es3)
r.aniadir_estadio(es4)

#EQUIPOS
eq1 = Equipo("FC Barcelona","1900","Barcelona")
eq1.agregar_jugador(j1)
eq1.agregar_jugador(j2)
eq1.agregar_jugador(j3)
eq1.asignar_entrenador(en1)
eq1.asignar_estadio(es1)
r.aniadir_equipo(eq1)

eq2 = Equipo("Real Madrid","1902","Madrid")
eq2.agregar_jugador(j4)
eq2.agregar_jugador(j5)
eq2.agregar_jugador(j6)
eq2.asignar_entrenador(en2)
eq2.asignar_estadio(es2)
r.aniadir_equipo(eq2)

eq3 = Equipo("FC Valencia","1901","Valencia")
eq3.agregar_jugador(j7)
eq3.agregar_jugador(j8)
eq3.agregar_jugador(j9)
eq3.asignar_entrenador(en3)
eq3.asignar_estadio(es3)
r.aniadir_equipo(eq3)

eq4 = Equipo("Sevilla FC","1901","Sevilla")
eq4.agregar_jugador(j10)
eq4.agregar_jugador(j11)
eq4.agregar_jugador(j12)
eq4.asignar_entrenador(en4)
eq4.asignar_estadio(es4)
r.aniadir_equipo(eq4)

#LIGAS
l = Liga("Liga BBVA","2014","Espania")
l.aniadir_equipo(eq1)
l.aniadir_equipo(eq2)
l.aniadir_equipo(eq3)
l.aniadir_equipo(eq4)
r.aniadir_liga(l)

print ("\nLos datos se han cargado, como desea probar la aplicacion?")
print ("1 - AUTO")
print ("0 - MANUAL")
auto = input("Eliga: ")
if auto == 1:
    l.jugar_partidos_auto()
    print ("\nPARTIDOS:\n")
    l.listar_partidos()
    l.consultar_clasificacion()
    print ("\nPICHICHI LIGA:\n")
    l.pichichi_liga()
    print ("\nPICHICHI EQUIPOS:\n")
    l.listar_pichichis_equipos()
elif auto == 0:
    #MENU
    salir=False
    while not salir:
        print ("=" * 20)
        print ("MENU PRINCIPAL")
        print ("Que desea hacer: ")
        print ("1 - Administrar jugadores")
        print ("2 - Administrar entrenadores")
        print ("3 - Administrar estadios")
        print ("4 - Administrar equipos")
        print ("5 - Administrar ligas")
        print ("0 - Salir")
        opc = input("Opcion: ")
        if opc == 1:
            administrar_jugadores()
        elif opc == 2:
            administrar_entrenadores()
        elif opc == 3:
            administrar_estadios()
        elif opc == 4:
            administrar_equipos()
        elif opc == 5:
            administrar_ligas()
        elif opc == 0:
            print ("Hasta pronto!")
            salir=True
        else:
            print ("Opcion incorrecta")
else:
    print ("Opcion incorrecta")