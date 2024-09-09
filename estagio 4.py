# Dados de faturamento por estado
faturamento_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o total de faturamento
total_faturamento = sum(faturamento_estado.values())

# Calcular e imprimir o percentual de cada estado
for estado, valor in faturamento_estado.items():
    percentual = (valor / total_faturamento) * 100
    print(f"{estado}: {percentual:.2f}%")
