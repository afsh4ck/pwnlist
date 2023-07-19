import itertools
import os

# Definir variables de color
AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def cabecera():
    print(ROJO + title + RESET)
    print(divider)

title = """
██████╗ ██╗    ██╗███╗   ██╗██╗     ██╗███████╗████████╗
██╔══██╗██║    ██║████╗  ██║██║     ██║██╔════╝╚══██╔══╝
██████╔╝██║ █╗ ██║██╔██╗ ██║██║     ██║███████╗   ██║   
██╔═══╝ ██║███╗██║██║╚██╗██║██║     ██║╚════██║   ██║   
██║     ╚███╔███╔╝██║ ╚████║███████╗██║███████║   ██║   
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚══════╝   ╚═╝                                                                                                                                     
Custom dictionaries for h4cking               < afsh4ck >"""

divider = """---------------------------------------------------------
"""

# Mostrar cabecera
cabecera()

# Función que devuelve una lista de combinaciones de números y caracteres especiales
def get_combinations(word, use_numbers, use_special_chars):
    combinations = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_chars = ['!', '@', '#', '$', '%', '&', '*', '?']
    max_number_count = 5  # Máximo número de veces que aparecen números en la palabra
    for i in range(1, len(word)):
        for subset in itertools.combinations(range(len(word)), i):
            replacements = []
            if use_numbers:
                # Limitar el número de veces que aparecen números en la palabra
                replacements.extend(numbers * min(max_number_count, i))
            if use_special_chars:
                replacements.extend(special_chars)
            for replacement in itertools.product(replacements, repeat=i):
                temp = list(word)
                for index, item in zip(subset, replacement):
                    temp[index] = item
                combination = ''.join(temp)
                combinations.append(combination)
    return combinations

# Función que devuelve una lista de nombres personalizados con mayúsculas y minúsculas alternadas
def get_alternating_cases(word):
    alternating_cases = []
    for i in range(2**len(word)):
        binary = bin(i)[2:].zfill(len(word))
        temp = []
        for j in range(len(word)):
            if binary[j] == "0":
                temp.append(word[j].lower())
            else:
                temp.append(word[j].upper())
        alternating_cases.append(''.join(temp))
    return alternating_cases

# Función que devuelve una lista con todas las combinaciones posibles de mayúsculas, minúsculas, números y caracteres especiales
def get_all_combinations(word, use_numbers, use_special_chars, use_alternating_cases):
    combinations = []
    if use_numbers or use_special_chars:
        combinations = get_combinations(word, use_numbers, use_special_chars)

    alternating_cases = []
    if use_alternating_cases:
        alternating_cases = get_alternating_cases(word)

    result = [word]
    if (use_numbers or use_special_chars) and use_alternating_cases:
        result.extend(combinations + alternating_cases)
    elif use_numbers or use_special_chars:
        result.extend(combinations)
    elif use_alternating_cases:
        result.extend(alternating_cases)

    return result

while True:
    try:
        # Obtiene la palabra del usuario
        word = input(VERDE + "[+] Introduce una palabra: " + RESET)

        # Obtiene la opción del usuario para utilizar números y caracteres especiales
        use_numbers = input(VERDE + "[+] ¿Quieres utilizar números? (s/n): " + RESET).lower() == "s"
        use_special_chars = input(VERDE + "[+] ¿Quieres utilizar caracteres especiales? (s/n): " + RESET).lower() == "s"

        # Obtiene la opción del usuario para alternar mayúsculas y minúsculas
        use_alternating_cases = input(VERDE + "[+] ¿Quieres alternar mayúsculas y minúsculas? (s/n): " + RESET).lower() == "s"

        # Muestra el mensaje sin animación de puntos suspensivos
        print(AMARILLO + "[*] Creando diccionario..." + RESET)

        # Obtiene el listado de nombres personalizados con todas las combinaciones posibles
        names = get_all_combinations(word, use_numbers, use_special_chars, use_alternating_cases)

        # Imprime el listado de nombres personalizados
        print(VERDE + "[+] Listado de nombres personalizados:" + RESET)
        for name in names:
            print(name)

        # Pregunta al usuario si desea guardar el listado de nombres personalizados en un archivo de texto
        export_to_txt = input(VERDE + "[+] ¿Deseas exportar el listado en un archivo de texto? (s/n): " + RESET)

        # Si el usuario desea exportar el listado de nombres personalizados en un archivo de texto, pide al usuario que introduzca el nombre del archivo y guarda el listado de nombres personalizados en un archivo de texto
        if export_to_txt.lower() == "s":
            filename = input("[+] Introduce el nombre del archivo para guardar el listado (sin extensión): ")
            with open(f"{filename}.txt", "w") as file:
                for name in names:
                    file.write(f"{name}\n")
            print(VERDE + f"[!] El listado de nombres personalizados se ha guardado en el archivo {filename}.txt" + RESET)

        # Pregunta al usuario si desea crear otro listado o salir del programa
        create_another = input(ROJO + "[*] ¿Deseas crear otro listado de nombres personalizados? (s/n): " + RESET)
        if create_another.lower() != "s":
            print(VERDE + "[+] Happy hacking ;)" + RESET)
            break

        # Limpia la pantalla y vuelve a la pantalla principal
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecera()

    except KeyboardInterrupt:
        print(ROJO + "[!] Se ha interrumpido el programa. Reiniciando..." + RESET)
        os.system('cls' if os.name == 'nt' else 'clear')
        cabecera()
