import random

def obtener_jugada_usuario():
    while True:
        jugada = input("Elige piedra, papel o tijeras: ").lower()
        if jugada in ["piedra", "papel", "tijeras"]:
            return jugada
        else:
            print("Por favor, introduce una opción válida.")

def obtener_jugada_cpu():
    return random.choice(["piedra", "papel", "tijeras"])

def determinar_ganador(jugada_usuario, jugada_cpu):
    if jugada_usuario == jugada_cpu:
        return "Empate"
    elif (jugada_usuario == "piedra" and jugada_cpu == "tijeras") or \
         (jugada_usuario == "papel" and jugada_cpu == "piedra") or \
         (jugada_usuario == "tijeras" and jugada_cpu == "papel"):
        return "¡Ganaste!"
    else:
        return "¡La CPU ganó!"

def main():
    print("Bienvenido al juego de piedra, papel o tijeras.")

    while True:
        jugada_usuario = obtener_jugada_usuario()
        jugada_cpu = obtener_jugada_cpu()

        print("Tu jugada:", jugada_usuario)
        print("Jugada de la CPU:", jugada_cpu)

        resultado = determinar_ganador(jugada_usuario, jugada_cpu)
        print(resultado)

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != "s":
            break

if __name__ == "__main__":
    main()
