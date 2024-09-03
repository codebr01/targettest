def inverter_string(string):
    string_invertida = ""
    
    i = len(string) - 1

    while i >= 0:
        string_invertida += string[i]
        i -= 1

    return string_invertida

string_original = input("Digite uma string para inverter: ")

resultado = inverter_string(string_original)

print(f"A string invertida é: {resultado}")
