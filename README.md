# 📝 README - Sistema de Gestión de eSports  

**Aplicación CRUD para administrar equipos y jugadores de eSports usando PostgreSQL y Python.**  

---

## 🚀 Requisitos Previos  
1. **PostgreSQL**: Instalado y corriendo localmente.  
2. **Python 3.8+**: Con las bibliotecas `psycopg` (o `psycopg2`).  
   ```sh
   pip install psycopg
   ```  
3. **Base de datos**:  
   - Crear una DB llamada `eSports` (o modificar el nombre en el código).  
   - Ejecutar estos scripts SQL para crear las tablas:  

   ```sql
   CREATE TABLE public.equipos (
       id_equipos SERIAL PRIMARY KEY,
       nombre VARCHAR(100) NOT NULL,
       pais VARCHAR(50),
       entrenador VARCHAR(100)
   );

   CREATE TABLE public.jugadores (
       id_jugadores SERIAL PRIMARY KEY,
       nickname VARCHAR(50) NOT NULL,
       rol VARCHAR(50),
       equipo_id INTEGER REFERENCES equipos(id_equipos) ON DELETE CASCADE
   );
   ```

---

## 🛠️ Configuración  
1. **Credenciales de la DB**:  
   Editar en `conectar()` los valores:  
   ```python
   host="localhost", 
   dbname="eSports", 
   user="postgres",  # Usuario de tu PostgreSQL
   password="12345678"  # Tu contraseña
   ```  

2. **Ejecutar la aplicación**:  
   ```sh
   python tu_archivo.py
   ```

---

## 🎮 Funcionalidades  

### 🔹 **Menú Principal**  
```
1. Gestión de Equipos  
2. Gestión de Jugadores  
3. Salir  
```

---

### ⚽ **Gestión de Equipos**  
1. **Crear equipo**:  
   - Ingresar: `ID`, `Nombre`, `País`, `Entrenador`.  
   - Ejemplo:  
     ```
     ID: 1  
     Nombre: Furia  
     País: Brasil  
     Entrenador: Coach Carl  
     ```  

2. **Actualizar equipo**:  
   - Seleccionar por `ID` y modificar campos (dejar vacíos para no cambiar).  

3. **Eliminar equipo**:  
   - Automáticamente borra los jugadores asociados (por `ON DELETE CASCADE`).  

4. **Ver todos los equipos**:  
   - Muestra: `ID`, `Nombre`, `País`, `Entrenador`.  

---

### 🎮 **Gestión de Jugadores**  
1. **Crear jugador**:  
   - Ingresar: `ID`, `Nickname`, `Rol`, `ID del equipo` (debe existir).  
   - Ejemplo:  
     ```
     ID: 101  
     Nickname: Coldzera  
     Rol: Sniper  
     ID Equipo: 1  
     ```  

2. **Actualizar jugador**:  
   - Modificar: `Nickname`, `Rol`, o `Equipo`.  

3. **Eliminar jugador**:  
   - Solo requiere el `ID` del jugador.  

4. **Ver todos los jugadores**:  
   - Muestra: `ID`, `Nickname`, `Rol`, `ID Equipo`.  

---

## 🛑 Notas Importantes  
- **Integridad de datos**:  
  - No se puede asignar un jugador a un equipo inexistente.  
  - Al borrar un equipo, sus jugadores se eliminan automáticamente.  

- **Errores comunes**:  
  - Si la aplicación falla, verifica que PostgreSQL esté activo y las credenciales sean correctas.  

---

## 📌 Ejemplo de Uso  
1. **Crear equipo** → **Agregar jugadores** → **Listar datos**:  
   ```sh
   # Menú principal → Opción 1 (Equipos) → Opción 1 (Crear):
   ID: 1  
   Nombre: Team Liquid  
   País: Internacional  
   Entrenador: zews  

   # Volver al menú → Opción 2 (Jugadores) → Opción 1 (Crear):
   ID: 501  
   Nickname: EliGE  
   Rol: Entry Fragger  
   ID Equipo: 1  
   ```



¿Listo para gestionar tu equipo de eSports? 🎮✨
