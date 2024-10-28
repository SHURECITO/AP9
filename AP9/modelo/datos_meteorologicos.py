class DatosMeteorologicos():
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo:str = nombre_archivo


    def procesar_datos(self)-> tuple[float, float, float, float, str]:
        suma_temperaturas = 0
        count_temperaturas = 0
        suma_humedad = 0
        count_humedad = 0
        suma_presion = 0
        count_presion = 0
        suma_velocidad_viento = 0
        count_velocidad_viento = 0
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    count_temperaturas += 1 
                    valor = float(linea.split(":")[1].strip())
                    suma_temperaturas += valor

                if "Humedad" in linea:
                    count_humedad += 1
                    valor = float(linea.split(":")[1].split()[0])
                    suma_humedad += valor

                if "Presion" in linea:
                    count_presion += 1
                    valor = float(linea.split(":")[1].split()[0])
                    suma_presion += valor

                if "Viento" in linea:
                    count_velocidad_viento += 1
                    valor = float(linea.split(":")[1].split(",")[0].strip())
                    suma_velocidad_viento += valor

        try:
            print("Promedio de temperaturas:", suma_temperaturas / count_temperaturas)
        except ZeroDivisionError:
            print("No se puede dividir por cero la temperatura")

        try:
            print("Promedio de humedad:", suma_humedad / count_humedad)
        except ZeroDivisionError:
            print("No se puede dividir por cero la humedad")

        try:
            print("Promedio de presión:", suma_presion / count_presion)
        except ZeroDivisionError:
            print("No se puede dividir por cero la presión")

        try:
            print("Promedio de viento:", suma_velocidad_viento / count_velocidad_viento)
        except ZeroDivisionError:
            print("No se puede dividir por cero la viento")