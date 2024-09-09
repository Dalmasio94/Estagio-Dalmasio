def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

# Exemplo de uso
string = input("Digite uma string: ")
print("String invertida:", inverter_string(string))
