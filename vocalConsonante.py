letra = input("Por favor, escriba una letra a consultar si es consonante o vocal")
if len(letra) == 1 and letra.isalpha:
    letra.lower()
    vocales=['a','e','i','o','u']
    if letra in vocales:
        print(f"la letra {letra} es una vocal")
    else:
        print(f"la letra {letra} es una consonante")
else:
    print("Por favor, siga las instrucciones del primer mensaje")
