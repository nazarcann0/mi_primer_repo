def decimal_a_base(numero, base):
    if numero == 0:
        return "0", [(0, base, 0, 0)]
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    pasos = []

    while numero > 0:
        resto = numero % base
        cociente = numero // base
        pasos.append((numero, base, cociente, resto))
        resultado = digitos[resto] + resultado
        numero = cociente
    return resultado, pasos


def mostrar_pasos(numero_original, base, resultado, pasos):
    print(f"\nConvirtiendo {numero_original} de decimal a base {base}:")
    print("-" * 40)

    for numero, base_usada, cociente, resto in pasos:
        print(f"{numero:>6} / {base_usada} = {cociente:<6} resto {resto}")
    
    print("-" * 40)
    print(f"Resultado (leyendo los restos de abajo hacia arriba): {resultado}\n")

resultado, pasos = decimal_a_base(47, 2)
mostrar_pasos(47, 2, resultado, pasos)

resultado, pasos = decimal_a_base(47, 16)
mostrar_pasos(47, 16, resultado, pasos)


