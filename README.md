Este site tem como propósito calcular o valor da conta de energia levando em conta dois fatores:o valor fixo e o valor variável na conta de água conforme acordo entre os condôminos.
O valor fixo é dividido por 8 condôminos e o valor variável é dividido pelo número de pessoas por apartamento.

O script 'calculo_gui.py' agora mostra uma tela feita usando o 'ttkbootstrap' - A tela é mais rica do que as que são feitas pelo tkinter.
Convém salientar que foi feito um update na versão do python de 3.13.0 para 3.13.2 de tal sorte abrigar o tcl bem caracterizado pela instalação do Activetcl. Ou seja a dependência com o tcl permanece apesar de não apresentar no script menção ao tkinter.

# NOTE: 'bootstyle' is valid for ttkbootstrap, but Astral ty type checker does not recognize it.

Conta Copasa - 25/07/2025

=== Cálculo da Conta de Água e Esgoto (Terminal) ===

Digite o valor de esgoto dinâmico (fixo): R$ 339.41
Digite o valor de abastecimento de água (variável): R$ 458.92
Digite o valor de recursos hídricos - água: R$ 8.73
Digite o valor de recursos hídricos - esgoto: R$ 1.92

=== Resultado ===
Valor fixo ajustado por apartamento: R$ 43.76
Valor variável por residente: R$ 27.00

Valores a serem pagos por apartamento:
apartamento 01: R$ 124.74
apartamento 02: R$ 124.74
apartamento 101: R$ 97.75
apartamento 102: R$ 97.75
apartamento 201: R$ 97.75
apartamento 202: R$ 97.75
apartamento 301: R$ 70.75
apartamento 302: R$ 97.75

=== Totais ===
Total arrecadado: R$ 808.98
Valor total da conta: R$ 808.98
Diferença (deve ser zero): R$ -0.00

__________
Teste SSH
