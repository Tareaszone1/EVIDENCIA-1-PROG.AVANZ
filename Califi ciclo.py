def get_int():
    while True:
        numero = input("Dame un numero entero: ")
        try:
            numero = int(numero)
            if 0 <= numero <= 100:
                return numero
            else:
                print("La calificacion debe ser entre 1 y 100.")
        except ValueError as err:
            print(f"Debe ingresar un numero entero. {err}")
        except Exception as ex:
            print(f"Ha ocurrido un problema. {ex}")
numero = get_int()