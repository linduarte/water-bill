# Introduzindo as variáveis
"""
Prompts the user to enter the dynamic sewage value and stores it in the `valor_fixo` variable.
"""

valor_fixo: float = float(input("Digite o esgoto dinâmico:"))
valor_variavel: float = float(input("Digite abastecimento água:"))
recursos_hidr_agua: float = float(input("Digite recursos hídricos água:"))
recursos_hidr_esg: float = float(input("Digite recursos hídricos esgoto:"))
numero_apartamentos: int = 8
numero_residentes: int = 18

# Calculando o valor total da conta de água
total_conta_agua = valor_fixo + valor_variavel + recursos_hidr_agua + recursos_hidr_esg

# Calculando o valor fixo por apartamento
valor_fixo_por_apartamento = valor_fixo / numero_apartamentos

# Exibindo o valor fixo por apartamento
print(f"Valor fixo: R${valor_fixo_por_apartamento:.2f}")

# Calculando o valor variável por residente
valor_variavel_por_residente = valor_variavel / numero_residentes

# Exibindo o valor variável por residente
print(f"Valor variável: R${valor_variavel_por_residente:.2f}")

# Dicionário com a distribuição de residentes por apartamento
distribuicao_residentes = {
    "apartamento 01": 3,
    "apartamento 02": 3,
    "apartamento 101": 2,
    "apartamento 102": 2,
    "apartamento 201": 3,
    "apartamento 202": 2,
    "apartamento 301": 1,
    "apartamento 302": 2,
}
# Calculando e exibindo os valores a serem pagos por apartamento
print("Valores a serem pagos por apartamento:")
total_pago_por_apartamentos = 0.0  # Initialize as float
for apartamento, residentes in distribuicao_residentes.items():
    valor_total_apartamento = valor_fixo_por_apartamento + (
        valor_variavel_por_residente * residentes
    )
    total_pago_por_apartamentos += valor_total_apartamento

    print(f"{apartamento}: R$ {valor_total_apartamento:.2f}")

# Exibindo a soma total dos valores pagos pelos apartamentos
print(
    "\nSoma total dos valores pagos pelos apartamentos:",
    f"R$ {total_pago_por_apartamentos:.2f}",
)
