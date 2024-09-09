import json

# Exemplo de dados JSON
data = '''
{
    "faturamento": [100, 200, 300, 0, 400, 500, 600, 0, 700, 800, 900, 0]
}
'''

# Carregar os dados
faturamento_diario = json.loads(data)["faturamento"]

# Filtrar valores não-zero
faturamento_validos = [valor for valor in faturamento_diario if valor > 0]

# Calcular o menor e maior valor
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Calcular a média mensal
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Contar dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

# Resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias acima da média: {dias_acima_media}")
