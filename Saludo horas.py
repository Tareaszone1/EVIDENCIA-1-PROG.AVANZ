def saludo(hora):
    if hora < 12:
        return "Buenos dias"
    elif hora < 19:
        return "Buenas tardes"
    else:
        return "Buenas noches"
for hr in range(25):
    saludo = saludo (hr)
    print(f"{hr}: {saludo}")