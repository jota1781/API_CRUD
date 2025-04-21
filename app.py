# Importando las librerías necesarias
import streamlit as st  # Streamlit permite crear interfaces interactivas para tus aplicaciones web.
import pandas as pd  # Pandas es una librería poderosa para manipulación de datos.
import Libreria_productos as lprod


# Inicializando las bases de datos en `st.session_state` si no existen.
# `st.session_state` se usa para almacenar variables en memoria durante una sesión en Streamlit.
if 'productos' not in st.session_state:
    st.session_state['productos'] = {}  # Diccionario vacío para almacenar los productos.
if 'bombas' not in st.session_state:
    st.session_state['bombas'] = {}  # Diccionario vacío para almacenar las bombas.
if 'estudiantes' not in st.session_state:
    st.session_state['estudiantes'] = {}  # Diccionario vacío para almacenar los estudiantes.

# --- CLASES Y FUNCIONES CRUD --- # Este bloque contiene las funciones que realizan las operaciones CRUD


# --- Funciones para las Bombas ---

# Función para agregar una bomba.
def agregar_bomba(id_creacion, nombre_creacion, presion, amperaje):
    """
    Esta función agrega una bomba al sistema con los parámetros dados.
    """
    st.session_state['bombas'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Presión': presion, 'Amperaje': amperaje}
    st.success(f"Bomba '{nombre_creacion}' agregada.")  # Mensaje de éxito.
    mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.

# Función para ver una bomba.
def ver_bomba(id_busqueda):
    """
    Esta función permite ver una bomba usando su ID.
    """
    if id_busqueda in st.session_state['bombas']:
        st.write(st.session_state['bombas'][id_busqueda])  # Muestra los detalles de la bomba.
    else:
        st.error(f"Bomba con ID '{id_busqueda}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.
    mostrar_bomba()  # Muestra el DataFrame con las bombas.

# Función para eliminar una bomba.
def eliminar_bomba(id_eliminacion):
    """
    Esta función elimina una bomba usando su ID.
    """
    if id_eliminacion in st.session_state['bombas']:
        del st.session_state['bombas'][id_eliminacion]  # Elimina la bomba del diccionario.
        st.success(f"Bomba con ID '{id_eliminacion}' eliminada.")  # Mensaje de éxito.
    else:
        st.error(f"Bomba con ID '{id_eliminacion}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.
    mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.

# Función para actualizar una bomba.
def actualizar_bomba(id_actualizacion, nombre_actualizado, presion_actualizada, amperaje_actualizado):
    """
    Esta función actualiza una bomba con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['bombas']:
        st.session_state['bombas'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Presión': presion_actualizada,
            'Amperaje': amperaje_actualizado
        }
        st.success(f"Bomba con ID '{id_actualizacion}' actualizada.")  # Mensaje de éxito.
        mostrar_bomba()  # Muestra el DataFrame con las bombas actualizadas.
    else:
        st.error(f"Bomba con ID '{id_actualizacion}' no encontrada.")  # Mensaje de error si no se encuentra la bomba.

# --- Funciones para los Estudiantes ---

# Función para agregar un estudiante.
def agregar_estudiante(id_creacion, nombre_creacion, matricula):
    """
    Esta función agrega un estudiante al sistema con los parámetros dados.
    """
    st.session_state['estudiantes'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Matrícula': matricula}
    st.success(f"Estudiante '{nombre_creacion}' agregado.")  # Mensaje de éxito.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para ver un estudiante.
def ver_estudiante(id_busqueda):
    """
    Esta función permite ver un estudiante usando su ID.
    """
    if id_busqueda in st.session_state['estudiantes']:
        st.write(st.session_state['estudiantes'][id_busqueda])  # Muestra los detalles del estudiante.
    else:
        st.error(f"Estudiante con ID '{id_busqueda}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes.

# Función para eliminar un estudiante.
def eliminar_estudiante(id_eliminacion):
    """
    Esta función elimina un estudiante usando su ID.
    """
    if id_eliminacion in st.session_state['estudiantes']:
        del st.session_state['estudiantes'][id_eliminacion]  # Elimina al estudiante del diccionario.
        st.success(f"Estudiante con ID '{id_eliminacion}' eliminado.")  # Mensaje de éxito.
    else:
        st.error(f"Estudiante con ID '{id_eliminacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.
    mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.

# Función para actualizar un estudiante.
def actualizar_estudiante(id_actualizacion, nombre_actualizado, matricula_actualizada):
    """
    Esta función actualiza los datos de un estudiante con los nuevos valores dados.
    """
    if id_actualizacion in st.session_state['estudiantes']:
        st.session_state['estudiantes'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Matrícula': matricula_actualizada
        }
        st.success(f"Estudiante con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_estudiante()  # Muestra el DataFrame con los estudiantes actualizados.
    else:
        st.error(f"Estudiante con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el estudiante.

# Funciones para mostrar los DataFrames


def mostrar_bomba():
    df = pd.DataFrame.from_dict(st.session_state['bombas'], orient='index')
    st.subheader("Listado de Bombas")
    st.write(df)

def mostrar_estudiante():
    df = pd.DataFrame.from_dict(st.session_state['estudiantes'], orient='index')
    st.subheader("Listado de Estudiantes")
    st.write(df)

# --- INTERFAZ STREAMLIT ---

# Página Principal
st.title("📊 Sistema CRUD Interactivo 🚀")

# Título con gradiente en HTML
st.markdown("""
    <h1 style="background: linear-gradient(to right, #ff7e5f, #feb47b); 
    color: white; text-align: center; padding: 30px;">
    Aplicación CRUD para Bombas, Productos y Estudiantes
    </h1>
    """, unsafe_allow_html=True)

# Descripción
st.write("""
    Este aplicativo permite gestionar **Bombas**, **Productos** y **Estudiantes** con operaciones CRUD (Crear, Leer, Eliminar, Actualizar).
    Puedes realizar varias operaciones de manera sencilla y rápida con una interfaz interactiva.
    🚀 ¡Comienza a gestionar tus datos de manera eficiente!
""")

# Menú de selección de página
pagina = st.sidebar.selectbox("Selecciona una página:", ["🏠 Home", "📋 Ejemplos CRUD"])

if pagina == "🏠 Home":
    st.write("""
        **Bienvenido a la página de ejemplos CRUD!** 🛠️
        
        Selecciona **"Ejemplos CRUD"** para gestionar **Estudiantes**, **Bombas** o **Productos**.
    """)

elif pagina == "📋 Ejemplos CRUD":
    tabs = st.tabs(["👤 Ejemplo de Estudiantes", "🛠️ Ejemplo de Bombas", "📦 Ejemplo de Productos"])

    with tabs[0]:
        st.header("👤 Gestión de Estudiantes")
        
        # Expander para agregar estudiante
        with st.expander("Agregar Estudiante"):
            id_creacion = st.text_input("ID del Estudiante")
            nombre_creacion = st.text_input("Nombre del Estudiante")
            matricula = st.text_input("Matrícula del Estudiante")
            if st.button("Agregar Estudiante"):
                agregar_estudiante(id_creacion, nombre_creacion, matricula)

        # Expander para ver estudiante
        with st.expander("Ver Estudiante"):
            id_busqueda = st.text_input("ID del Estudiante para ver detalles")
            if st.button("Ver Estudiante"):
                ver_estudiante(id_busqueda)

        # Expander para actualizar estudiante
        with st.expander("Actualizar Estudiante"):
            id_actualizacion = st.text_input("ID del Estudiante para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre del Estudiante")
            matricula_actualizada = st.text_input("Nueva Matrícula del Estudiante")
            if st.button("Actualizar Estudiante"):
                actualizar_estudiante(id_actualizacion, nombre_actualizado, matricula_actualizada)

        # Expander para eliminar estudiante
        with st.expander("Eliminar Estudiante"):
            id_eliminacion = st.text_input("ID del Estudiante para eliminar")
            if st.button("Eliminar Estudiante"):
                eliminar_estudiante(id_eliminacion)

        # Boton para generar excel de estudiantes
        if st.button('Generar Excel Estudiantes'):
            df_estudiantes = pd.DataFrame.from_dict(st.session_state['estudiantes'], orient='index')
            df_estudiantes.to_excel('Excel_Estudiantes.xlsx', index= False)

    with tabs[1]:
        st.header("🛠️ Gestión de Bombas")
        
        # Expander para agregar bomba
        with st.expander("Agregar Bomba"):
            id_creacion = st.text_input("ID de la Bomba")
            nombre_creacion = st.text_input("Nombre de la Bomba")
            presion = st.number_input("Presión de la Bomba (psi)")
            amperaje = st.number_input("Amperaje de la Bomba (A)")
            if st.button("Agregar Bomba"):
                agregar_bomba(id_creacion, nombre_creacion, presion, amperaje)

        # Expander para ver bomba
        with st.expander("Ver Bomba"):
            id_busqueda = st.text_input("ID de la Bomba para ver detalles")
            if st.button("Ver Bomba"):
                ver_bomba(id_busqueda)

        # Expander para actualizar bomba
        with st.expander("Actualizar Bomba"):
            id_actualizacion = st.text_input("ID de la Bomba para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre de la Bomba")
            presion_actualizada = st.number_input("Nueva Presión de la Bomba", value=0)
            amperaje_actualizado = st.number_input("Nuevo Amperaje de la Bomba", value=0)
            if st.button("Actualizar Bomba"):
                actualizar_bomba(id_actualizacion, nombre_actualizado, presion_actualizada, amperaje_actualizado)

        # Expander para eliminar bomba
        with st.expander("Eliminar Bomba"):
            id_eliminacion = st.text_input("ID de la Bomba para eliminar")
            if st.button("Eliminar Bomba"):
                eliminar_bomba(id_eliminacion)

        # Boton para generar excel de bombas
        if st.button('Generar Excel Bombas'):
            df_bombas = pd.DataFrame.from_dict(st.session_state['bombas'], orient='index')
            df_bombas.to_excel('Excel_Bombas.xlsx', index= False)


    with tabs[2]:
        st.header("📦 Gestión de Productos")
        
        # Expander para agregar producto
        with st.expander("Agregar Producto"):
            id_creacion = st.text_input("ID del Producto")
            nombre_creacion = st.text_input("Nombre del Producto")
            precio = st.number_input("Precio del Producto")
            cantidad = st.number_input("Cantidad en Stock")
            if st.button("Agregar Producto"):
                lprod.agregar_producto(id_creacion, nombre_creacion, precio, cantidad)

        # Expander para ver producto
        with st.expander("Ver Producto"):
            id_busqueda = st.text_input("ID del Producto para ver detalles")
            if st.button("Ver Producto"):
                lprod.ver_producto(id_busqueda)

        # Expander para actualizar producto
        with st.expander("Actualizar Producto"):
            id_actualizacion = st.text_input("ID del Producto para actualizar")
            nombre_actualizado = st.text_input("Nuevo Nombre del Producto")
            precio_actualizado = st.number_input("Nuevo Precio del Producto", value=0)
            cantidad_actualizada = st.number_input("Nueva Cantidad en Stock", value=0)
            if st.button("Actualizar Producto"):
                lprod.actualizar_producto(id_actualizacion, nombre_actualizado, precio_actualizado, cantidad_actualizada)

        # Expander para eliminar producto
        with st.expander("Eliminar Producto"):
            id_eliminacion = st.text_input("ID del Producto para eliminar")
            if st.button("Eliminar Producto"):
                lprod.eliminar_producto(id_eliminacion)

        # Boton para generar excel de productos
        if st.button('Generar Excel Productos'):
            df_productos = pd.DataFrame.from_dict(st.session_state['productos'], orient='index')
            df_productos .to_excel('Excel_Productos.xlsx', index= False)

#Generar archivo de requerimientos
# en la terminal tipificar: pip freeze > "requirements.txt" 
#instalar librerias: pip install -r requirements.txt
