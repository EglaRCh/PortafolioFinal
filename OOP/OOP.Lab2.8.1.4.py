def read_int(prompt, min, max):
    try: 
        prompt = int(input(prompt))
        assert prompt >= min
        assert prompt <= max
    except ValueError:
        print("Error: entrada incorrecta")
    except AssertionError:
        print("Error: el valor no está dentro del rango permitido")
    

v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)
if v == None:
    quit()
else:
    print("El número es:", v)


