import psycopg # Importa la biblioteca psycopg para interactuar con PostgreSQL


# Función para establecer la conexión a la base de datos
def conectar():
    try:
        conexion = psycopg.connect( host="localhost", # Dirección del servidor de la base de datos
        dbname="eSports", # Nombre de la base de datos a la que te quieres conectar
        user="postgres", # Nombre de usuario de la base de datos
        password="12345678" # Contraseña del usuario de la base de datos
        )
        print("Conexión exitosa") # Imprime un mensaje si la conexión fue exitosa return conexion
        # Devuelve el objeto de conexión
        return conexion       
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}") # Muestra un mensaje de error si la conexión falla
    return None # Devuelve None si la conexión falla


# Función para crear un nuevo equipo en la base de datos 
def crear_dato_equipos(id_equipos, nombre, pais, entrenador):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("INSERT INTO public.equipos (id_equipos, nombre, pais, entrenador) VALUES (%s, %s, %s,%s)",
                (id_equipos, nombre, pais, entrenador)) # Inserta los datos proporcionados en la tabla equipos
            conexion.commit() # Confirma la transacción para guardar los cambios
            print("Registro creado exitosamente") # Imprime un mensaje si el registro fue creado exitosamente
            return True       
        except psycopg.Error as e:
            print(f"Error al crear registro: {e}") # Muestra un mensaje de error si la inserción falla
            conexion.rollback() # Deshace los cambios en la base de datos si hay error
            return False  # Retorna false al no lograr crear un nuevo equipo
        finally:
            conexion.close() # Cierra la conexion con la base de datos 

            
# Funcion para leer datos de los equipos
def leer_datos_equipos():
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("SELECT id_equipos, nombre, pais, entrenador FROM public.equipos") # Ejecuta una consulta para obtener todos los registros
                registros = cursor.fetchall() # Recupera todos los registros de la consulta
            for registro in registros: #Itera cada registro dentro de la lista registros para mostrarlos
                print(f"ID: {registro[0]}, Nombre: {registro[1]}, Pais {registro[2]}, Entrenador: {registro[3]}") # Imprime cada registro
        except psycopg.Error as e:
            print(f"Error al leer registros: {e}") # Muestra un mensaje de error si la lectura falla
        finally:
            conexion.close() # Cierra la conexion con la base de datos 

# Funcion para actualizar datos de los equipos 
def actualizar_datos_equipos(id_equipos,nuevo_nombre,nuevo_pais,nuevo_entrenador):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion: 
        try: 
            with conexion.cursor() as cursor:  # Crea un cursor para ejecutar comandos SQL
                cursor.execute("UPDATE public.equipos SET nombre = %s, pais = %s, entrenador = %s WHERE id_equipos = %s", (nuevo_nombre,nuevo_pais,nuevo_entrenador,id_equipos)) # Actualiza los datos del registro especificado
                conexion.commit() # Confirma la transacción para guardar los cambios
                if cursor.rowcount>0:
                    print("Actualizacion exitosa") # Imprime un mensaje si el registro fue actualizado exitosamente
                else:
                    print("Lo sentimos no se pudo actualizar los datos No se encontró un registro con la ID proporcionada ") # Muestra un mensaje si no se encuentra el registro
        except psycopg.Error as e:
            print(f"Error al actualizar los datos {e}")  # Muestra un mensaje de error si la actualización falla

        finally:
            conexion.close() # Cierra la conexion con la base de datos 

 # Función para borrar un equipos de la base de datos           
def eliminar_equipo(id_equipo):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                # Primero, eliminar los jugadores asociados al equipo borrando el registro proporcionado por el ID
                cursor.execute("DELETE FROM public.jugadores WHERE equipo_id = %s", (id_equipo,))
                # Luego, eliminar el equipo
                cursor.execute("DELETE FROM public.equipos WHERE id_equipos = %s", (id_equipo,))
                conexion.commit() # Confirma la transacción para guardar los cambios
                if cursor.rowcount > 0:
                    print("Equipo y jugadores eliminados exitosamente") # Imprime un mensaje si el registro fue borrado exitosamente
                else:
                    print("No se encontró un equipo con el ID proporcionado o no hay jugadores asociados.") # Muestra un mensaje si no se encuentra el registro
        except psycopg.Error as e:
            print(f"Error al eliminar equipo y jugadores: {e}") # Muestra un mensaje de error si el borrado falla
        finally:
            conexion.close() # Cierra la conexión a la base de datos


# Función para crear un nuevo jugador en la base de datos 
def crear_dato_jugador(id_jugadores, nickname, rol, equipo_id):
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("INSERT INTO public.jugadores (id_jugadores, nickname, rol, equipo_id) VALUES (%s, %s, %s,%s)",
                (id_jugadores, nickname, rol, equipo_id)) # Inserta los datos proporcionados en la tabla jugadores
            conexion.commit() # Confirma la transacción para guardar los cambios
            print("Registro creado exitosamente") # Imprime un mensaje si el registro fue creado exitosamente
            return True       
        except psycopg.Error as e:
            print(f"Error al crear registro: {e}") # Muestra un mensaje de error si la inserción falla
            conexion.rollback() # Deshace los cambios en la base de datos si hay error
            return False  # Retorna false al no lograr crear un nuevo equipo
        finally:
            conexion.close() # Cierra la conexion con la base de datos 
            
# Funcion para leer datos de los jugadores
def leer_datos_jugadores():
    conexion = conectar() # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("SELECT id_jugadores, nickname, rol, equipo_id FROM public.jugadores") # Ejecuta una consulta para obtener todos los registros
                registros = cursor.fetchall() # Recupera todos los registros de la consulta
            for registro in registros: #Itera cada registro dentro de la lista registros para mostrarlos
                print(f"ID: {registro[0]}, Nombre: {registro[1]}, Pais {registro[2]}, Entrenador: {registro[3]}") # Imprime cada registro
        except psycopg.Error as e:
            print(f"Error al leer registros: {e}") # Muestra un mensaje de error si la lectura falla
        finally:
            conexion.close() # Cierra la conexion con la base de datos 

# Funcion para actualizar datos de los jugadores 
def actualizar_datos_jugadores(id_jugadores,nuevo_nickname,nuevo_rol,nuevo_equipo):
    conexion = conectar()  # Establece la conexión a la base de datos
    if conexion: 
        try: 
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("UPDATE public.jugadores SET nickname = %s, rol = %s, equipo_id = %s WHERE id_jugadores = %s", (nuevo_nickname,nuevo_rol,nuevo_equipo, id_jugadores)) # Actualiza los datos del registro especificado
                conexion.commit() # Confirma la transacción para guardar los cambios

                if cursor.rowcount>0:
                    print("Actualizacion exitosa") # Imprime un mensaje si el registro fue actualizado exitosamente
                else:
                    print("Lo sentimos no se pudo actualizar los datos No se encontró un registro con la ID proporcionada ") # Muestra un mensaje si no se encuentra el registro
        except psycopg.Error as e:
            print(f"Error al actualizar los datos {e}")  # Muestra un mensaje de error si la actualización falla
        finally:
            conexion.close()    # Cierra la conexión a la base de datos
     
            
# Función para eliminar un jugador
def eliminar_jugador(id_jugadores):
    conexion = conectar()  # Establece la conexión a la base de datos
    if conexion:
        try:
            with conexion.cursor() as cursor: # Crea un cursor para ejecutar comandos SQL
                cursor.execute("DELETE FROM public.jugadores WHERE id_jugadores = %s", (id_jugadores,)) # Borra el registro especificado por la ID
                conexion.commit()  # Confirma la transacción para guardar los cambios
                if cursor.rowcount > 0:
                    print("Jugador eliminado exitosamente")  # Imprime un mensaje si el registro fue borrado exitosamente
                else:
                    print("No se encontró un jugador con el ID proporcionado.")  # Muestra un mensaje si no se encuentra el registro
        except psycopg.Error as e:
            print(f"Error al eliminar jugador: {e}") # Muestra un mensaje de error si el borrado falla
        finally:
            conexion.close() # Cierra la conexión a la base de datos

# Funcion para simplificar la forma en la que el programa recibe los datos          
def obtener_entrada(mensaje):
    return input(mensaje).strip()

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n=========== MENÚ PRINCIPAL ===============")
    print("1. Gestión de Equipos")
    print("2. Gestión de Jugadores")
    print("3. Salir")
    return obtener_entrada("Seleccione una opción: ")

#Funcion para mostrar el menu de los equipos
def menu_equipos():
    while True:
        print("\n------- GESTIÓN DE EQUIPOS -------")
        print("1. Crear nuevo equipo")
        print("2. Actualizar datos de equipo")
        print("3. Eliminar equipo")
        print("4. Ver todos los equipos")
        print("5. Volver al menú principal")
        
        opcion = obtener_entrada("Seleccione una opción: ")
        
        #Segun la respuesta de usuario agregamos, modificamos o borramos pasandole los datos ingresados por el usuario a nuestra funciones correspondientes
        if opcion == '1':
            print("\n--- Crear Nuevo Equipo ---")
            id_equipos = obtener_entrada("Ingrese el ID del equipo: ")
            nombre = obtener_entrada("Ingrese el nombre del equipo: ")
            pais = obtener_entrada("Ingrese el país del equipo: ")
            entrenador = obtener_entrada("Ingrese el entrenador del equipo: ")
            crear_dato_equipos(id_equipos, nombre, pais, entrenador)
            
        elif opcion == '2':
            print("\n--- Actualizar Equipo ---")
            leer_datos_equipos()
            id_equipos = obtener_entrada("Ingrese el ID del equipo a actualizar: ")
            nuevo_nombre = obtener_entrada("Nuevo nombre (deje vacío para no cambiar): ")
            nuevo_pais = obtener_entrada("Nuevo país (deje vacío para no cambiar): ")
            nuevo_entrenador = obtener_entrada("Nuevo entrenador (deje vacío para no cambiar): ")
            actualizar_datos_equipos(id_equipos, nuevo_nombre or None, nuevo_pais or None, nuevo_entrenador or None)
            
        elif opcion == '3':
            print("\n--- Eliminar Equipo ---")
            leer_datos_equipos()
            id_equipo = obtener_entrada("Ingrese el ID del equipo a eliminar: ")
            eliminar_equipo(id_equipo)
            
        elif opcion == '4':
            print("\n--- Lista de Equipos ---")
            leer_datos_equipos()
            
        elif opcion == '5':
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

# Funcion para mostrar menu de los jugadores
def menu_jugadores():
    while True:
        print("\n------- GESTIÓN DE JUGADORES -------")
        print("1. Crear nuevo jugador")
        print("2. Actualizar datos del jugador")
        print("3. Eliminar jugador")
        print("4. Ver todos los jugadores")
        print("5. Volver al menú principal")
        
        opcion = obtener_entrada("Seleccione una opción: ")  
        
        #Segun la respuesta de usuario agregamos, modificamos o borramos pasandole los datos ingresados por el usuario a nuestra funciones correspondientes
        if opcion == '1':
            print("\n--------Crear nuevo jugador------")
            id_jugador = obtener_entrada("Ingrese ID del jugador:")
            nickname = obtener_entrada("Ingrese nickname del jugador: ")
            rol = obtener_entrada("Ingrese rol de jugador: ")
            equipo_id = obtener_entrada("Ingrese ID de equipo en el que juega el jugador: ")
            crear_dato_jugador(id_jugador,nickname,rol,equipo_id)
            
        elif opcion == '2':
            print("-------Actualizar datos de jugador--------")
            leer_datos_jugadores()
            id_jugador = obtener_entrada ("Ingrese el ID del Jugador que desea Actualizar: ")
            nickname = obtener_entrada ("Ingrese el nuevo nickname (deje vacío para no cambiar): ")
            rol = obtener_entrada ("Ingrese el nuevo rol del jugador (deje vacío para no cambiar): ")
            equipo_id = obtener_entrada ("Ingrese nuevo ID del equipo del jugador (deje vacío para no cambiar): ")
            actualizar_datos_jugadores(id_jugador,nickname,rol,equipo_id)
        
        elif opcion == '3':
             print("\n--- Eliminar Jugadores ---")
             leer_datos_jugadores()
             id_jugador = obtener_entrada("Ingrese el ID del jugador a eliminar: ")
             eliminar_jugador(id_jugador)
             
        elif opcion == '4':
            print("\n--- Lista de Jugadores ---")
            leer_datos_jugadores()
            
        elif opcion == '5':
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")
            
# Y finalmente le decimos al programa que se  ejecute llamando a todas las funcione que contienen los menus
if __name__ == "__main__":
   print("=========== SISTEMA DE GESTIÓN DE eSPORTS ===============")
   while True:
        opcion_principal = mostrar_menu()
        
        if opcion_principal == '1':
            menu_equipos()
        elif opcion_principal == '2':
            menu_jugadores()
        elif opcion_principal == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    
    
   
    
   
  
