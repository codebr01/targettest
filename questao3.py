import json

soma_valor_de_faturamento = 0
contador_de_dias = 0

numero_de_dias_maior_que_media = 0

with open('dados.json', 'r') as file:
    data = json.load(file)

    menor_valor_de_faturamento = data[0]['valor']
    maior_valor_de_faturamento = data[0]['valor']

for registro in data:
    dia = registro["dia"]
    valor = registro["valor"]

    if valor < menor_valor_de_faturamento:
        menor_valor_de_faturamento = valor

    if valor > maior_valor_de_faturamento:
        maior_valor_de_faturamento = valor

    if valor > 0:
        contador_de_dias += 1
        soma_valor_de_faturamento += valor

media_mensal_sem_finais_de_semana = soma_valor_de_faturamento / contador_de_dias

for registro in data:
    dia = registro["dia"]
    valor = registro["valor"]

    if valor > media_mensal_sem_finais_de_semana:
        numero_de_dias_maior_que_media += 1
    

print(f"Menor faturamento: {menor_valor_de_faturamento}")
print(f"Maior faturamento: {maior_valor_de_faturamento}")
print(f"Número de dias com faturamento maior que à média mensal: {numero_de_dias_maior_que_media}")