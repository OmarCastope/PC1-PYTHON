

def convertir_fecha(fecha):
    meses = {
        "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
        "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
        "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
    }

    try:
        if "/" in fecha:
            mes, dia, anio = fecha.split("/")
            mes = mes.zfill(2)
            dia = dia.zfill(2)
        else:
            partes = fecha.replace(",", "").split()
            mes = meses.get(partes[0].capitalize())
            dia = partes[1].zfill(2)
            anio = partes[2]

        return f"{anio}-{mes}-{dia}"
    except:
        return "Formato inválido. Intente nuevamente."

# Parte interactiva
entrada = input("Ingrese una fecha (MM/DD/AAAA o 'Mes D, AAAA'): ")
salida = convertir_fecha(entrada)
print(f"Fecha en formato AAAA-MM-DD: {salida}")