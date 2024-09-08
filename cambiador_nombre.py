import streamlit as st
import os
from datetime import datetime
import zipfile
import io

def cambiar_nombre_y_extension(archivo, nuevo_nombre, nueva_extension, contador):
    return f"{nuevo_nombre}({contador}).{nueva_extension}"

st.title("Cambiador de Nombres de Archivos")

archivos_subidos = st.file_uploader("Sube tus archivos", accept_multiple_files=True)

if archivos_subidos:
    st.write("Archivos subidos:")
    for archivo in archivos_subidos:
        st.write(archivo.name)
    
    st.write("Ingresa el nuevo nombre y extensión para todos los archivos:")
    nuevo_nombre_general = st.text_input("Nuevo nombre base para todos los archivos", value="archivo")
    nueva_extension_general = st.text_input("Nueva extensión para todos los archivos", value="txt")
    
    if st.button("Procesar archivos"):
        fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_carpeta = f"conversion_{fecha_hora}"
        
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for i, archivo in enumerate(archivos_subidos, start=1):
                nuevo_archivo = cambiar_nombre_y_extension(archivo, nuevo_nombre_general, nueva_extension_general, i)
                zip_file.writestr(f"{nombre_carpeta}/{nuevo_archivo}", archivo.getvalue())
        
        st.download_button(
            label="Descargar archivos procesados",
            data=zip_buffer.getvalue(),
            file_name=f"{nombre_carpeta}.zip",
            mime="application/zip"
        )
        
        st.success("¡Archivos procesados y listos para descargar!")
