import streamlit as st
import pandas as pd

# Función para agregar un producto.
def agregar_producto(id_creacion, nombre_creacion, precio, cantidad):
    """
    Esta función recibe los datos del producto y lo agrega a la base de datos en memoria.
    """
    st.session_state['productos'][id_creacion] = {'id':id_creacion, 'Nombre': nombre_creacion, 'Precio': precio, 'Cantidad': cantidad}
    st.success(f"Producto '{nombre_creacion}' agregado.")  # Muestra un mensaje de éxito.
    mostrar_producto()  # Muestra el DataFrame con los productos actualizados.

# Función para ver un producto.
def ver_producto(id_busqueda):
    """
    Esta función permite ver un producto usando su ID.
    """
    if id_busqueda in st.session_state['productos']:
        st.write(st.session_state['productos'][id_busqueda])  # Muestra los detalles del producto.
    else:
        st.error(f"Producto con ID '{id_busqueda}' no encontrado.")  # Mensaje de error si no se encuentra el producto.
    mostrar_producto()  # Muestra el DataFrame con los productos.

# Función para eliminar un producto.
def eliminar_producto(id_eliminacion):
    """
    Esta función elimina un producto de la base de datos utilizando su ID.
    """
    if id_eliminacion in st.session_state['productos']:
        del st.session_state['productos'][id_eliminacion]  # Elimina el producto del diccionario.
        st.success(f"Producto con ID '{id_eliminacion}' eliminado.")  # Mensaje de éxito.
    else:
        st.error(f"Producto con ID '{id_eliminacion}' no encontrado.")  # Mensaje de error si no se encuentra el producto.
    mostrar_producto()  # Muestra el DataFrame con los productos actualizados.

# Función para actualizar un producto.
def actualizar_producto(id_actualizacion, nombre_actualizado, precio_actualizado, cantidad_actualizada):
    """
    Esta función actualiza los detalles de un producto utilizando su ID.
    """
    if id_actualizacion in st.session_state['productos']:
        st.session_state['productos'][id_actualizacion] = {
            'Nombre': nombre_actualizado,
            'Precio': precio_actualizado,
            'Cantidad': cantidad_actualizada
        }
        st.success(f"Producto con ID '{id_actualizacion}' actualizado.")  # Mensaje de éxito.
        mostrar_producto()  # Muestra el DataFrame con los productos actualizados.
    else:
        st.error(f"Producto con ID '{id_actualizacion}' no encontrado.")  # Mensaje de error si no se encuentra el producto.

# Funciones para mostrar los DataFrames
def mostrar_producto():
    df = pd.DataFrame.from_dict(st.session_state['productos'], orient='index')
    st.subheader("Listado de Productos")
    st.write(df)