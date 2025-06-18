# conta_agua_terminal.py


def main():
    print("=== Cálculo da Conta de Água e Esgoto (Terminal) ===\n")

    valor_fixo = float(input("Digite o valor de esgoto dinâmico (fixo): R$ "))
    valor_variavel = float(
        input("Digite o valor de abastecimento de água (variável): R$ ")
    )
    recursos_hidr_agua = float(input("Digite o valor de recursos hídricos - água: R$ "))
    recursos_hidr_esg = float(
        input("Digite o valor de recursos hídricos - esgoto: R$ ")
    )

    numero_apartamentos = 8

    distribuicao_residentes = {
        "apartamento 01": 3,
        "apartamento 02": 3,
        "apartamento 101": 2,
        "apartamento 102": 2,
        "apartamento 201": 2,
        "apartamento 202": 2,
        "apartamento 301": 1,
        "apartamento 302": 2,
    }

    numero_residentes = sum(distribuicao_residentes.values())

    # Total da conta
    total_conta_agua = (
        valor_fixo + valor_variavel + recursos_hidr_agua + recursos_hidr_esg
    )

    # Cálculo inicial (sem correção)
    valor_fixo_por_apartamento = valor_fixo / numero_apartamentos
    valor_variavel_por_residente = valor_variavel / numero_residentes

    total_pago_inicial = 0.0
    for residentes in distribuicao_residentes.values():
        total_pago_inicial += valor_fixo_por_apartamento + (
            valor_variavel_por_residente * residentes
        )

    # Corrige a diferença
    diferenca = total_conta_agua - total_pago_inicial
    ajuste_por_apartamento = diferenca / numero_apartamentos
    valor_fixo_corrigido = valor_fixo_por_apartamento + ajuste_por_apartamento

    print("\n=== Resultado ===")
    print(f"Valor fixo ajustado por apartamento: R$ {valor_fixo_corrigido:.2f}")
    print(f"Valor variável por residente: R$ {valor_variavel_por_residente:.2f}\n")

    total_pago_corrigido = 0.0
    print("Valores a serem pagos por apartamento:")
    for apto, moradores in distribuicao_residentes.items():
        valor_total = valor_fixo_corrigido + (valor_variavel_por_residente * moradores)
        total_pago_corrigido += valor_total
        print(f"{apto}: R$ {valor_total:.2f}")

    print("\n=== Totais ===")
    print(f"Total arrecadado: R$ {total_pago_corrigido:.2f}")
    print(f"Valor total da conta: R$ {total_conta_agua:.2f}")
    print(
        f"Diferença (deve ser zero): R$ {(total_conta_agua - total_pago_corrigido):.2f}"
    )


if __name__ == "__main__":
    main()
