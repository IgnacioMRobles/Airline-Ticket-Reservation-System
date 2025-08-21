#[INTEGRANTES IGNACIO, FRANCO Y VALENTINO COM 11]

import getpass
import random
from datetime import datetime
def cartel():
    VERDE = "\033[32m"
    RESET = "\033[0m"

    print("\n" + "=" * 40)
    print(VERDE + "EN CONSTRUCCIÓN".center(40) + RESET)
    print("=" * 40 + "\n")
    
MAX_USUARIOS = 10
MAX_CEO  = 5
MAX_USUARIOS_NORMALES = 4
usuarios_correo = [None] * MAX_USUARIOS
usuarios_clave = [None] * MAX_USUARIOS
usuarios_tipo = [None] * MAX_USUARIOS

MAX_AEROLINEAS = 5
MAX_VUELOS     = 20
aerolineas_nombres       = [None] * MAX_AEROLINEAS
aerolineas_codigo_iata   = [None] * MAX_AEROLINEAS
aerolineas_descr         = [None] * MAX_AEROLINEAS
aerolinea_contador       = 0
contador_ARG = contador_BRA = contador_CHI = 0


texto_valido = False
texto_conInfo = False

def CargaUsuarios(): 

    usuarios_correo[0] = "admin@ventaspasajes777.com"
    usuarios_clave[0] = "admin123"
    usuarios_tipo[0] = "administrador"

    usuarios_correo[1] = "ceo1@ventaspasajes777.com"
    usuarios_clave[1] = "ceo123"
    usuarios_tipo[1] = "ceo"

    usuarios_correo[2] = "ceo2@ventaspasajes777.com"
    usuarios_clave[2] = "ceo456"
    usuarios_tipo[2] = "ceo"

    usuarios_correo[3] = "usuario1@ventaspasajes777.com"
    usuarios_clave[3] = "usuario123"
    usuarios_tipo[3] = "usuario"

    usuarios_correo[4] = "usuario2@ventaspasajes777.com"
    usuarios_clave[4] = "usuario456"
    usuarios_tipo[4] = "usuario"

vuelos_aerolinea = [None] * MAX_VUELOS
vuelos_codigo    = [None] * MAX_VUELOS
vuelos_origen    = [None] * MAX_VUELOS
vuelos_destino   = [None] * MAX_VUELOS
vuelos_fecha     = [None] * MAX_VUELOS
vuelos_hora      = [None] * MAX_VUELOS
vuelos_precio    = [None] * MAX_VUELOS
vuelos_estado    = [None] * MAX_VUELOS  # "Alta" o "Baja"

# filas totales = MAX_VUELOS × 40, columnas = 6 (A–F)
asientos_vuelo = [
    [None for _ in range(6)]
    for _ in range(MAX_VUELOS * 40)
]

def inicializar_asientos(vuelo_idx):
    estados = ["L", "O", "R"]
    base = vuelo_idx * 40
    for fila in range(40):
        for col in range(6):
            i = base + fila
            if col == 3:
                asientos_vuelo[i][col] = "P"
            else:
                asientos_vuelo[i][col] = random.choice(estados)

def crear_vuelo_ceo():
    print("\n--- Crear Vuelo (CEO) ---")

    if aerolinea_contador == 0:
        print("No hay aerolíneas registradas. Primero cree una.\n")
        return

    indice_vuelo = -1
    i_vuelo = 0
    while i_vuelo < MAX_VUELOS and indice_vuelo == -1:
        if vuelos_codigo[i_vuelo] is None:
            indice_vuelo = i_vuelo
        i_vuelo += 1
    if indice_vuelo == -1:
        print("Máximo de vuelos alcanzado.\n")
        return

    print("\n--- Crear Vuelo (CEO) ---")

    aero_ok = False
    while not aero_ok:
        codigo_aerolinea = input("Código de Aerolínea (IATA): ")
        # buscar exacto en arreglo
        i_aero = 0
        indice_aerolinea = -1
        while i_aero < aerolinea_contador and indice_aerolinea == -1:
            if aerolineas_codigo_iata[i_aero] == codigo_aerolinea:
                indice_aerolinea = i_aero
            i_aero += 1
        if indice_aerolinea != -1:
            aero_ok = True
        else:
            print("IATA no registrada. Reingrese.")

    codigo_vuelo = input("Código de Vuelo (ej: AR1234): ")

    ori_ok = False
    while not ori_ok:
        origen = input("Origen: ")
        validar_vacios(origen)
        if texto_conInfo:
            ori_ok = True
        else:
            print("Debe ingresar origen.")
    dest_ok = False
    while not dest_ok:
        destino = input("Destino: ")
        validar_vacios(destino)
        if texto_conInfo:
            dest_ok = True
        else:
            print("Debe ingresar destino.")

    precio_ok = False
    while not precio_ok:
        entrada = input("Precio: ")
        try:
            precio = float(entrada)
            if precio >= 0:
                precio_ok = True
            else:
                print("Precio negativo.")
        except ValueError:
            print("Formato inválido.")

    hora_ok = False
    while not hora_ok:
        hora = input("Hora (hh:mm): ")
        partes = hora.split(":")
        if len(partes) == 2:
            try:
                h = int(partes[0]); m = int(partes[1])
                if 0 <= h < 24 and 0 <= m < 60:
                    hora_ok = True
                else:
                    print("Hora fuera de rango.")
            except ValueError:
                print("Sólo números y ':'.")
        else:
            print("Formato hh:mm.")

    fecha_ok = False
    while not fecha_ok:
        fecha = input("Fecha (dd/mm/aaaa): ")
        if len(fecha) == 10 and fecha[2] == "/" and fecha[5] == "/":
            fecha_ok = True
        else:
            print("Formato dd/mm/aaaa.")

    vuelos_aerolinea[indice_vuelo] = aerolineas_nombres[indice_aerolinea]
    vuelos_codigo[indice_vuelo]    = codigo_vuelo
    vuelos_origen[indice_vuelo]    = origen
    vuelos_destino[indice_vuelo]   = destino
    vuelos_precio[indice_vuelo]    = precio
    vuelos_hora[indice_vuelo]      = hora
    vuelos_fecha[indice_vuelo]     = fecha
    vuelos_estado[indice_vuelo]    = "Alta"

    inicializar_asientos(indice_vuelo)

    print("Vuelo creado exitosamente.\n")
    listar_vuelos_por_aerolinea()




def listar_vuelos_existentes():
    print("\n--- Vuelos cargados ---")
    existe = False

    for i in range(20):
        if vuelos_codigo[i] is not None and vuelos_estado[i] == "Alta":
            existe = True
            print(f"{i+1}. Código: {vuelos_codigo[i]} | "
                  f"Aerolínea: {vuelos_aerolinea[i]} | "
                  f"Origen: {vuelos_origen[i]} | "
                  f"Destino: {vuelos_destino[i]}")

    if not existe:
        print("No hay vuelos cargados.")

def listar_vuelos_por_aerolinea():
    """Muestra posición, aerolínea y cantidad de vuelos 'Alta'
       sólo para las aerolíneas realmente cargadas."""

    n = aerolinea_contador

    counts = [0] * n
    for i_aero in range(n):
        for v in range(MAX_VUELOS):
            if (vuelos_aerolinea[v] == aerolineas_nombres[i_aero] and
                vuelos_estado[v] == "Alta"):
                counts[i_aero] += 1

    orden = []
    usados = set()
    for _ in range(n):
        max_cnt = -1
        max_idx = -1
        for indice in range(n):
            if indice not in usados and counts[indice] > max_cnt:
                max_cnt, max_idx = counts[indice], indice
        orden.append(max_idx)
        usados.add(max_idx)

    print("\n======================= REPORTE DE VUELOS =======================")
    print("POSICIÓN | AEROLÍNEA          | CANTIDAD DE VUELOS")
    print("-------------------------------------------------------------")
    for pos, indice in enumerate(orden):
        nombre   = aerolineas_nombres[indice]
        cantidad = counts[indice]
        print(f"{pos:^8} | {nombre:<18} | {cantidad:^3}")
    print("===============================================================\n")



def buscar_vuelos():
    print("\n=== Buscar Vuelos ===")
    fecha_actual = datetime.now()

    fecha_input = input("Ingrese la fecha de salida (dd/mm/aaaa): ")
    try:
        fecha_deseada = datetime.strptime(fecha_input, "%d/%m/%Y")
    except ValueError:
        print("Formato de fecha incorrecto.")
        return

    print("\n========================================================================================================")
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA")
    print("========================================================================================================")
    print("{:<10} {:<12} {:<18} {:<15} {:<12} {:<8} {:<10}".format("CÓDIGO", "AEROLÍNEA", "ORIGEN", "DESTINO", "FECHA", "HORA", "PRECIO"))
    print("--------------------------------------------------------------------------------------------------------")

    total = 0
    for i in range(20):
        if vuelos_codigo[i] and vuelos_estado[i] == "Alta":
            try:
                fecha_vuelo = datetime.strptime(vuelos_fecha[i], "%d/%m/%Y")
                if fecha_vuelo >= fecha_deseada:
                    print("{:<10} {:<12} {:<18} {:<15} {:<12} {:<8} ${:<10,.2f}".format(
                        vuelos_codigo[i], vuelos_aerolinea[i], vuelos_origen[i], vuelos_destino[i],
                        vuelos_fecha[i], vuelos_hora[i], vuelos_precio[i]
                    ))
                    total += 1
            except:
                continue  # Por si alguna fecha está mal cargada

    print("--------------------------------------------------------------------------------------------------------")
    print(f"Total de vuelos encontrados: {total}")

def buscar_asientos():
    print("\n=== Buscar Asientos por Código de Vuelo ===")
    codigo = input("Ingrese el código del vuelo: ").upper()
    fecha_actual = datetime.now()
    encontrado = False

    for indice_vuelo in range(MAX_VUELOS):
        if vuelos_codigo[indice_vuelo] == codigo and vuelos_estado[indice_vuelo] == "Alta":
            try:
                fecha_v = datetime.strptime(vuelos_fecha[indice_vuelo], "%d/%m/%Y")
                if fecha_v >= fecha_actual:
                    mostrar_asientos_vuelo(indice_vuelo)
                    encontrado = True
            except ValueError:
                pass
    if not encontrado:
        print("El vuelo no existe, no está vigente o el código es incorrecto.")


def mostrar_asientos_vuelo(vuelo_idx):
    base = vuelo_idx * 40
    print("\n    A B C   P D E F")
    for fila in range(40):
        print(f"F{fila+1:02d}:", end=" ")
        for col in range(6):
            if col == 3:
                print("P", end=" ")
            indice = base + fila
            print(asientos_vuelo[indice][col], end=" ")
        print()
    input("\nPresione Enter para volver...")

def modificar_vuelo_ceo():
    print("\n--- Modificar Vuelo (CEO) ---")

    cod_buscar = input("Código del vuelo i_aero modificar: ")

    indice = -1
    i = 0
    while i < MAX_VUELOS and indice == -1:
        if vuelos_codigo[i] == cod_buscar and vuelos_estado[i] == "Alta":
            indice = i
        i += 1
    if indice == -1:
        print("Vuelo no encontrado o dado de baja.\n")
        return

    print(f"Aerolínea: {vuelos_aerolinea[indice]}")
    print(f"Origen:    {vuelos_origen[indice]}")
    print(f"Destino:   {vuelos_destino[indice]}")
    print(f"Fecha:     {vuelos_fecha[indice]}")
    print(f"Hora:      {vuelos_hora[indice]}")
    print(f"Precio:    ${vuelos_precio[indice]:.2f}\n")


    # Fecha
    entrada_nueva = input("Nueva Fecha (dd/mm/aaaa): ")
    validar_vacios(entrada_nueva)
    if texto_conInfo:
        vuelos_fecha[indice] = entrada_nueva

    # Hora
    entrada_nueva = input("Nueva Hora (hh:mm): ")
    validar_vacios(entrada_nueva)
    if texto_conInfo:
        vuelos_hora[indice] = entrada_nueva

    # Origen
    entrada_nueva = input("Nuevo Origen: ")
    validar_vacios(entrada_nueva)
    if texto_conInfo:
        vuelos_origen[indice] = entrada_nueva

    # Destino
    entrada_nueva = input("Nuevo Destino: ")
    validar_vacios(entrada_nueva)
    if texto_conInfo:
        vuelos_destino[indice] = entrada_nueva

    # Precio
    entrada_nueva = input("Nuevo Precio: ")
    validar_vacios(entrada_nueva)
    if texto_conInfo:
        try:
            p = float(entrada_nueva)
            if p >= 0:
                vuelos_precio[indice] = p
            else:
                print("Precio negativo, no se actualizó.")
        except ValueError:
            print("Formato inválido, no se actualizó.")

    print("Modificación completada.\n")



def eliminar_vuelo():
    print("\n--- Eliminar Vuelo ---")
    codigo = input("Ingrese el código del vuelo que desea eliminar: ").upper().strip()

    
    indices = [i for i, c in enumerate(vuelos_codigo) if c == codigo]
    if not indices:
        print("El código de vuelo no existe.")
        return
    indice = indices[0]

    
    if vuelos_estado[indice] == "Baja":
        print("Este vuelo ya está dado de baja.")
        return

    
    print(f"\nDatos del vuelo {codigo}:")
    print(f"  Aerolínea: {vuelos_aerolinea[indice]}")
    print(f"  Origen:    {vuelos_origen[indice]}")
    print(f"  Destino:   {vuelos_destino[indice]}")

    confirmar = input("\n¿Desea eliminar este vuelo? (s/n): ").strip().lower()
    if confirmar == "s":
        vuelos_estado[indice] = "Baja"
        print("Vuelo eliminado exitosamente.")
    else:
        print("No se realizaron cambios.")

def preguntar_si_no(pregunta: str) -> bool:
    mensaje = f"{pregunta} (si/no): "
    respuesta = input(mensaje)

    while respuesta != "si" and respuesta != "no":
        print("Entrada inválida. Debe escribir exactamente 'si' o 'no'.")
        respuesta = input(mensaje)

    # True si dijo "si", False si dijo "no"
    return respuesta == "si"

def gestion_vuelos():
    opcion_vuelos = ""                         
    while opcion_vuelos != "4":
        print("\n--- Gestión de Vuelos ---")
        print("1. Crear Vuelo")
        print("2. Modificar Vuelo")
        print("3. Eliminar Vuelo")
        print("4. Volver")

        opcion_vuelos = input("Seleccione una opción: ")
        while opcion_vuelos not in ("1", "2", "3", "4"):
            print("Opción inválida. Intente nuevamente.")
            opcion_vuelos = input("Seleccione una opción: ")

        match opcion_vuelos:
            case "1":
                if preguntar_si_no("¿Desea ver los vuelos cargados hasta el momento?"):
                    listar_vuelos_existentes()
                crear_vuelo_ceo()

            case "2":
                if preguntar_si_no("¿Desea ver los vuelos cargados hasta el momento?"):
                    listar_vuelos_existentes()
                modificar_vuelo_ceo()

            case "3":
                if preguntar_si_no("¿Desea ver los vuelos cargados hasta el momento?"):
                    listar_vuelos_existentes()
                eliminar_vuelo()

            case "4":
                print("Volviendo al menú anterior...")

def buscar_vuelo_idx(codigo):
    for i in range(20):
        if vuelos_codigo[i] == codigo:
            return i
    return -1



def menu_ceo():
    opcion_ceo = ""
    while opcion_ceo != "4":
        print("\n======= MENÚ CEO =======")
        print("1. Gestión de Vuelos")
        print("2. Gestión de Promociones")
        print("3. Reportes")
        print("4. Cerrar Sesión")
        opcion_ceo = input("Seleccione una opción: ")
        while opcion_ceo not in ["1", "2", "3", "4"]:
            opcion_ceo = input("Opción inválida. Intente nuevamente: ")

        if opcion_ceo == "1":
            gestion_vuelos()
        elif opcion_ceo == "2":
            submenu_promociones()
        elif opcion_ceo == "3":
            submenu_reportes_ceo()
        elif opcion_ceo == "4":
            print("Cerrando sesión de CEO...")

def menu_admin():
    opcion_admin = ""
    while opcion_admin != "5":
        print("\n======= MENÚ ADMINISTRADOR =======")
        print("1. Gestión de Aerolíneas")
        print("2. Aprobar/Denegar Promociones")
        print("3. Gestión de Novedades")
        print("4. Reportes")
        print("5. Salir")
        opcion_admin = input("Ingrese una opción: ")
        while opcion_admin not in ["1", "2", "3", "4", "5"]:
            opcion_admin = input("Opción inválida. Reintente: ")

        if opcion_admin == "1":
            submenu_aerolineas()
        elif opcion_admin == "2":
            cartel()
        elif opcion_admin == "3":
            gestion_novedades()
        elif opcion_admin == "4":
            submenu_reportes_admin()
        elif opcion_admin == "5":
            print("Cerrando sesión de administrador...")

def menu_usuario():
    opcion_usuario = ""
    while opcion_usuario != "7":
        print("\n======= MENÚ USUARIO =======")
        print("1. Buscar Vuelos")
        print("2. Buscar asientos")
        print("3. Reservar Vuelos")
        print("4. Gestionar Reservas")
        print("5. Ver Historial de Compras")
        print("6. Ver Novedades")
        print("7. Cerrar Sesión")
        opcion_usuario = input("Seleccione una opción: ")
        while opcion_usuario not in ["1", "2", "3", "4", "5", "6", "7"]:
            opcion_usuario = input("Opción inválida. Intente nuevamente: ")

        if opcion_usuario == "1":
            if opcion_usuario == "1":
              buscar_vuelos()
        elif opcion_usuario == "2":
            buscar_asientos()
        elif opcion_usuario == "3":
            cartel()
        elif opcion_usuario == "4":
            gestionar_reservas()
        elif opcion_usuario == "5":
            cartel()
        elif opcion_usuario == "6":
            cartel()
        elif opcion_usuario == "7":
            print("Cerrando sesión de usuario...")

def contar_caract(cant, texto):
    global texto_valido
    texto_valido = False
    validar_vacios(texto)

    contador = 0
    for caracter in texto:
        contador += 1

    texto_valido = texto_conInfo and 0 < contador <= cant 

def validar_vacios(texto):
    global texto_conInfo
    texto_conInfo = False
    cont_info = False

    for caracter in texto:
        if caracter != ' ':
            cont_info = True

    texto_conInfo = cont_info
'''intentos : integer
accesoPermitido, loginCorrecto : Boolean 
'''


def gestionar_reservas():
    opcion = ""
    while opcion != "3":
        print("\n--- Gestionar Reservas ---")
        print("1. Consultar reservas")
        print("2. Cancelar/Confirmar una reserva")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")
        while opcion not in ["1", "2", "3"]:
            opcion = input("Opción inválida. Intente nuevamente: ")

        if opcion == "1":
            cartel()
        elif opcion == "2":
            cartel()

def login():
    global loginCorrecto
    print("\n=== Inicio de Sesión ===")

    # Reinicio estado de login
    intentos = 0
    loginCorrecto = False
    tipoUsuario = ""   

    while intentos < 3 and loginCorrecto == False:
        correo = input("Ingrese su correo: ")
        clave  = getpass.getpass("Ingrese su contraseña: ")

        for i in range(MAX_USUARIOS):
            if usuarios_correo[i] == correo and usuarios_clave[i] == clave:
                loginCorrecto = True
                tipoUsuario  = usuarios_tipo[i]

        if loginCorrecto == True:
            print("Acceso concedido. Bienvenido, " + tipoUsuario + ".")
        else:
            intentos = intentos + 1
            restantes = 3 - intentos
            print("Credenciales incorrectas. Te quedan " + str(restantes) + " intento(s).")

    if loginCorrecto == False:
        print("Se han agotado los intentos. Acceso denegado.")
    else:

        if tipoUsuario == "administrador":
            menu_admin()
        elif tipoUsuario == "ceo":
            menu_ceo()
        elif tipoUsuario == "usuario":
            menu_usuario()

def contar_rol(rol_buscado):
    """Devuelve la cantidad de cuentas segun su rol."""
    return sum(1 for t in usuarios_tipo if t == rol_buscado)

def registrar_usuario():
    print("\n=== Registro de Nuevo Usuario ===")
    pos_libre = -1
    for i in range(MAX_USUARIOS):
        if usuarios_correo[i] is None and pos_libre == -1:
            pos_libre = i

    continuar = True
    if pos_libre == -1:
        print("No hay pos_libre disponible para nuevos usuarios.")
        continuar = False
    if continuar:
        correo = input("Ingrese su correo: ")
        while (correo == "" or correo[0] == " " or correo[-1] == " "
               or "@" not in correo or "." not in correo):
            print("Correo inválido. Debe tener formato correcto y sin espacios al inicio/final.")
            correo = input("Ingrese su correo: ")
        duplicado = False
        for j in range(MAX_USUARIOS):
            if usuarios_correo[j] == correo:
                duplicado = True
        if duplicado:
            print("El correo ya está registrado. Intente con otro.")
            continuar = False

    if continuar:
        tipo = input("Tipo de cuenta ('ceo' o 'usuario'): ")
        while tipo != "ceo" and tipo != "usuario":
            print("Opción inválida. Elija exactamente 'ceo' o 'usuario'.")
            tipo = input("Tipo de cuenta ('ceo' o 'usuario'): ")

        actuales = contar_rol(tipo)
        if tipo == "ceo" and actuales >= MAX_CEO:
            print("No hay cupos para nuevos CEOs (ya hay " + str(actuales) + ").")
            continuar = False
        if tipo == "usuario" and actuales >= MAX_USUARIOS_NORMALES:
            print("No hay cupos para nuevos usuarios (ya hay " + str(actuales) + ").")
            continuar = False

    if continuar:
        clave = input("Ingrese su contraseña: ")
        while clave == "":
            print("La contraseña no puede ser vacía.")
            clave = input("Ingrese su contraseña: ")

        usuarios_correo[pos_libre] = correo
        usuarios_clave [pos_libre] = clave
        usuarios_tipo  [pos_libre] = tipo

        print(tipo + " registrado correctamente en la posición " + str(pos_libre) + ".")

    '''opcionSubmenu, aerolinea_contador, contador_ARG, contador_BRA ,contador_CHI : integer'''


def submenu_aerolineas():
    opcionSubmenu = 1
    while opcionSubmenu != 4:
        print("\n--- Submenú: Gestión de Aerolíneas ---")
        print("1. Crear Aerolínea")
        print("2. Modificar Aerolínea")
        print("3. Eliminar Aerolínea")
        print("4. Volver al menu principal")
        opcionSubmenu = input("Seleccione una opción: ")
        while opcionSubmenu != "1" and opcionSubmenu != "2" and opcionSubmenu != "3" and opcionSubmenu != "4":
            opcionSubmenu = input("Opción inválida. Reintente: ")
        opcionSubmenu = int(opcionSubmenu)
        if opcionSubmenu == 1:
            crear_aerolinea_admin()
        elif opcionSubmenu == 2:
            cartel()
        elif opcionSubmenu == 3:
            cartel()

def crear_aerolinea_admin():
    global aerolinea_contador, contador_ARG, contador_BRA, contador_CHI, texto_conInfo

    indice = -1
    i = 0
    while i < MAX_AEROLINEAS and indice == -1:
        if aerolineas_codigo_iata[i] is None:
            indice = i
        i += 1

    if indice == -1:
        print("Tope de aerolíneas alcanzado.")
        return

    print("--- Registro de Aerolínea ---")

    # 1) Nombre
    nombre_valido = False
    while not nombre_valido:
        nombre = input("Nombre de aerolínea: ")
        validar_vacios(nombre)
        if texto_conInfo:
            nombre_valido = True
        else:
            print("El nombre no puede estar vacío.")

    # 2) Código IATA
    iata_valido = False
    while not iata_valido:
        codigo_iata = input("Código IATA (1–5 chars): ")
        if len(codigo_iata) < 1 or len(codigo_iata) > 5:
            print("Debe tener entre 1 y 5 caracteres.")
            continue

        duplicado = False
        for j in range(MAX_AEROLINEAS):
            if aerolineas_codigo_iata[j] == codigo_iata:
                duplicado = True
        if duplicado:
            print("Ese código IATA ya existe.")
        else:
            iata_valido = True

    # 3) Descripción
    desc_valida = False
    while not desc_valida:
        descripcion = input("Descripción: ")
        validar_vacios(descripcion)
        if texto_conInfo:
            desc_valida = True
        else:
            print("La descripción no puede estar vacía.")

    # 4) País
    pais_valido = False
    while not pais_valido:
        pais = input("País (ARG/BRA/CHI): ")
        if pais == "ARG" or pais == "BRA" or pais == "CHI":
            pais_valido = True
        else:
            print("Debe ingresar ARG, BRA o CHI.")

    # 5) Guardar datos
    aerolineas_nombres[indice]       = nombre
    aerolineas_codigo_iata[indice]   = codigo_iata
    aerolineas_descr[indice]         = descripcion

    if pais == "ARG":
        contador_ARG += 1
    elif pais == "BRA":
        contador_BRA += 1
    else:
        contador_CHI += 1

    aerolinea_contador += 1
    print("Aerolínea creada exitosamente.")
    mostrar_estadisticas()
def mostrar_estadisticas():
    global contador_ARG, contador_BRA, contador_CHI
    # Calcular el país con mayor cantidad de aerolíneas
    max_pais = "ARG"
    max_cant = contador_ARG
    if contador_BRA > max_cant:
        max_pais = "BRA"
        max_cant = contador_BRA
    if contador_CHI > max_cant:
        max_pais = "CHI"
        max_cant = contador_CHI

    # Calcular el país con menor cantidad de aerolíneas
    min_pais = "ARG"
    min_cant = contador_ARG
    if contador_BRA < min_cant:
        min_pais = "BRA"
        min_cant = contador_BRA
    if contador_CHI < min_cant:
        min_pais = "CHI"
        min_cant = contador_CHI

    print("\n--- Estadísticas ---")
    print(f"País con mayor cantidad de aerolíneas:{max_pais}  - Cantidad: {max_cant}")
    print(f"País con menor cantidad de aerolíneas: {min_pais}  - Cantidad: {min_cant}")
    print("---------------------\n")
    if aerolinea_contador >= 5:
        print("Ya se han registrado el máximo de 5 aerolíneas.")

def gestion_novedades():
    opcion_submenu = ""
    while opcion_submenu != "5":
        print("\n--- Gestión de Novedades ---") 
        print("1. Crear Novedad")
        print("2. Modificar Novedad")
        print("3. Eliminar Novedad")
        print("4. Ver Novedades")
        print("5. Salir al menu principal")
        
        opcion_submenu = input("Seleccione una opción: ")
        
        while (opcion_submenu != "1") and (opcion_submenu !="2") and (opcion_submenu != "3") and (opcion_submenu != "4") and (opcion_submenu != "5"):
            opcion_submenu = input("Opción inválida. Intente nuevamente: ")

        if opcion_submenu == "1":
            cartel()
        elif opcion_submenu == "2":
            cartel()
        elif opcion_submenu == "3":
            cartel()
        elif opcion_submenu == "4":
            cartel()

def submenu_reportes_admin():
    opcion_submenu = 1
    while opcion_submenu != 4:
        print("\n---Reportes---")
        print("1.Reporte de ventas")
        print("2.Reporte de vuelos")
        print("3.Reporte de usuarios")
        print("4.Volver al menu principal")
        opcion_submenu =int (input ("Seleccione una opcion: "))
        while opcion_submenu < 1 or opcion_submenu > 5:
            print ("Error, intentelo de nuevo")
        match opcion_submenu:
            case 1: cartel()
            case 2: cartel()
            case 3: cartel()
            case 4: print("Volver")
    
def submenu_promociones():
    opcion = ""
    while opcion != "3":
        print("\n--- Submenú: Gestión de Promociones ---")
        print("1. Crear Promoción")
        print("2. Modificar Promoción")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")
        while opcion not in ["1", "2", "3"]:
            opcion = input("Opción inválida. Intente nuevamente: ")

        if opcion == "1":
            cartel()
        elif opcion == "2":
            cartel()
        elif opcion == "3":
            print("Volviendo al menú principal...")

def submenu_reportes_ceo():
    opcion = ""
    while opcion != "3":
        print("\n--- Reportes del CEO ---")
        print("1. Reporte de ventas de mi Aerolínea")
        print("2. Reporte de ocupación de Vuelos de mi Aerolínea")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")
        while opcion not in ["1", "2", "3"]:
            opcion = input("Opción inválida. Intente nuevamente: ")

        if opcion == "1":
            cartel()
        elif opcion == "2":
            cartel()
        elif opcion == "3":
            print("Volviendo al menú CEO...")

# Programa principal

CargaUsuarios()
opcionInicio = ""
while opcionInicio != "3":
    print("\n======= INICIO DE SESIÓN =======")
    print("1. Registrarme")
    print("2. Iniciar Sesión(login en el sistema)")
    print("3. Salir")
    
    opcionInicio = input("Seleccione una opción: ")
    while opcionInicio not in ["1", "2", "3"]:
        opcionInicio = input("Opción inválida. Intente nuevamente: ")
    
    if opcionInicio == "1":
        registrar_usuario()
    elif opcionInicio == "2":
        login()
    elif opcionInicio == "3":
        print("\nGracias por utilizar el sistema.")

'''
indice, i: integer
codigo_aerolinea, codigo_vuelo, origen, destino, fecha, hora: string
precio: float
'''