from PIL import Image

def crear_icono(input_png, output_ico):
    try:
        # Abrimos la imagen original
        img = Image.open(input_png)
        
        # Definimos los tamaños estándar que Windows usa para iconos
        # Esto asegura que se vea bien en el explorador, escritorio y barra de tareas
        tamanos = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # Guardamos como .ico especificando los tamaños
        img.save(output_ico, format='ICO', sizes=tamanos)
        
        print(f"✅ ¡Éxito! El icono '{output_ico}' ha sido creado.")
        
    except Exception as e:
        print(f"❌ Error al convertir: {e}")

if __name__ == "__main__":
    # Cambia estos nombres si tus archivos se llaman distinto
    archivo_entrada = "logo_mistral.png"
    archivo_salida = "logo_mistral.ico"
    
    crear_icono(archivo_entrada, archivo_salida)