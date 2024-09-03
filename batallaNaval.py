import random

def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tableroDisparosJugador, tableroDisparoOponente):
    print("\nTablero de Disparos: ")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\nTablero de Disparos de Oponente: ")
    for fila in tableroDisparoOponente:
        print(" ".join(fila))
        
def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando {barco['nombre']} de tamaño {barco['dimension']} ")
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                orientacion = input("ingrese la orientación (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice(['h', 'v'])
                
            if validarColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                colocarBarco(tablero, fila, columna, barco ['dimension'], orientacion)
                colocado = True
            elif jugador == "jugador":
                print("Colocacion es invalida. Intenta de nuevo")
                
def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
           if tablero[fila][columna+i] != "~":
               return False
    else: 
        if fila + dimension>len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila+i][columna] != "~":
                return False
    return True

def colocarBarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna+i]="B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna]="B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"
        return "impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True
    
def jugarContraComputadora():
    dimension = 5
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tableroDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre":"Portaaviones","dimension":3},
        {"nombre":"Submarino","dimension":2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputadora, barcos, "computadora")
    turnoJugador = True
    while True:
        if turnoJugador:
            print("\nTu turno")
            mostrarTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa la fila del disparo: "))
            columna = int(input("Ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("¡Genial!,Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado}")
            if verificarVictoria(tableroJugador):
                print("La computadota ganó ")
                return "Computadora"
        turnoJugador = not turnoJugador
    
    
def jugarDosJugadores():
    dimension = 5
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroDisparosJugador1 = crearTablero(dimension)
    tableroDisparosJugador2 = crearTablero(dimension)
    barcos = [
        {"nombre":"Portaaviones","dimension":3},
        {"nombre":"Submarino","dimension":2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    colocarBarcos(tableroJugador2, barcos, "jugador")
    turnoJugador1 = True
    while True:
        if turnoJugador1:
            print("\nTu turno jugador 1")
            mostrarTableros(tableroDisparosJugador1, tableroDisparosJugador2)
            fila = int(input("Ingresa la fila del disparo: "))
            columna = int(input("Ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("Jugador 1 ¡Gano!")
                return "Jugador 1"
        else:
            print("\n Tu turno jugador 2")
            mostrarTableros(tableroDisparosJugador2, tableroDisparosJugador1)
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador1, tableroDisparosJugador2, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado}")
            if verificarVictoria(tableroJugador1):
                print("El jugador 2 ganó ")
                return "Jugador 2"
        turnoJugador1 = not turnoJugador1
def mostrarMenu():
    print("¡¡¡SÉ BIENVENIDO A BATALLA NAVAL!!!")
    print("Selecciona contra quien quieres jugar ")
    print("1. Contra computadora")
    print("2. Contra otro jugador")
    print("3. Salir")
    
def iniciarJuego():
    while True:
        mostrarMenu()
        modo = input("Elige una opción: ")
        if modo == "1":
            ganador = jugarContraComputadora()
        elif modo == "2":
            ganador = jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar con PIO")
            break
        else:
            print("Opcion no válida, por favor elige una opción correcta!")
            continue
        print(f"El ganador es {ganador}")
        jugarDeNuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugarDeNuevo !="s":
            print("Gracias por jugar, Hasta luego, vuelve pronto")
            break
        
iniciarJuego()                              