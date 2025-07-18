# water-bill

import ttkbootstrap as tb
from tkinter import messagebox


def calcular_valores():
    try:
        # Recupera e converte os valores de entrada
        valor_fixo = float(entry_fixo.get())
        valor_variavel = float(entry_variavel.get())
        recursos_hidr_agua = float(entry_recursos_agua.get())
        recursos_hidr_esg = float(entry_recursos_esg.get())

        # Total da conta de água
        total_conta_agua = (
            valor_fixo + valor_variavel + recursos_hidr_agua + recursos_hidr_esg
        )

        numero_apartamentos = 8
        valor_fixo_por_apartamento = valor_fixo / numero_apartamentos
        numero_residentes = sum(distribuicao_residentes.values())
        valor_variavel_por_residente = (
            valor_variavel / numero_residentes if numero_residentes > 0 else 0
        )

        # Cálculo do total inicialmente arrecadado
        total_pago = 0
        for res in distribuicao_residentes.values():
            total_pago += valor_fixo_por_apartamento + (
                valor_variavel_por_residente * res
            )

        # Ajuste da diferença
        diferenca = total_conta_agua - total_pago
        ajuste_por_apartamento = diferenca / numero_apartamentos
        valor_fixo_corrigido_por_apartamento = (
            valor_fixo_por_apartamento + ajuste_por_apartamento
        )

        # Limpa resultados anteriores
        listbox_resultados.delete("1.0", "end")

        # Exibe valores fixos e variáveis
        listbox_resultados.insert(
            "end",
            f"Valor fixo (ajustado) por apartamento: R$ {valor_fixo_corrigido_por_apartamento:.2f}\n",
        )
        listbox_resultados.insert(
            "end",
            f"Valor variável por residente: R$ {valor_variavel_por_residente:.2f}\n\n",
        )

        # Calcula e exibe valores por apartamento
        total_pago_corrigido = 0
        for apt, res in distribuicao_residentes.items():
            valor_total_apartamento = valor_fixo_corrigido_por_apartamento + (
                valor_variavel_por_residente * res
            )
            total_pago_corrigido += valor_total_apartamento
            listbox_resultados.insert(
                "end", f"{apt}: R$ {valor_total_apartamento:.2f}\n"
            )

        # Exibe totais e diferença
        listbox_resultados.insert(
            "end", f"\nTotal arrecadado: R$ {total_pago_corrigido:.2f}\n"
        )
        listbox_resultados.insert(
            "end", f"Valor total da conta: R$ {total_conta_agua:.2f}\n"
        )
        listbox_resultados.insert(
            "end", f"Diferença: R$ {(total_conta_agua - total_pago_corrigido):.2f}\n"
        )

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {str(e)}")


def atualizar_residentes():
    apt = entry_apartamento.get()
    res = entry_residentes.get()
    if apt and res.isdigit():
        distribuicao_residentes[apt] = int(res)
        messagebox.showinfo(
            "Atualizado", f"Apartamento {apt} agora tem {res} moradores."
        )
    else:
        messagebox.showerror("Erro", "Digite um número válido de moradores.")


# Distribuição padrão
distribuicao_residentes = {
    "Apto 01": 3,
    "Apto 02": 3,
    "Apto 101": 2,
    "Apto 102": 2,
    "Apto 201": 3,
    "Apto 202": 2,
    "Apto 301": 1,
    "Apto 302": 2,
}

# Interface gráfica
root = tb.Window(themename="cyborg")
root.title("Cálculo de Conta de Água")
root.geometry("750x500")

frame_inputs = tb.Frame(root)
frame_inputs.pack(pady=10)

tb.Label(frame_inputs, text="Abastecimento Água:").grid(row=0, column=0, padx=5)
entry_variavel = tb.Entry(frame_inputs)
entry_variavel.grid(row=0, column=1, padx=5)

tb.Label(frame_inputs, text="Esgoto Dinâmico:").grid(row=0, column=2, padx=5)
entry_fixo = tb.Entry(frame_inputs)
entry_fixo.grid(row=0, column=3, padx=5)

tb.Label(frame_inputs, text="Recursos Hídricos Água:").grid(row=1, column=0, padx=5)
entry_recursos_agua = tb.Entry(frame_inputs)
entry_recursos_agua.grid(row=1, column=1, padx=5)

tb.Label(frame_inputs, text="Recursos Hídricos Esgoto:").grid(row=1, column=2, padx=5)
entry_recursos_esg = tb.Entry(frame_inputs)
entry_recursos_esg.grid(row=1, column=3, padx=5)

tb.Button(root, text="Calcular", bootstyle="success", command=calcular_valores).pack(
    pady=5
)

tb.Label(root, text="Distribuição por Apartamento").pack()
listbox_resultados = tb.ScrolledText(root, height=10)
listbox_resultados.pack()

frame_update = tb.Frame(root)
frame_update.pack(pady=10)

tb.Label(frame_update, text="Apto:").grid(row=0, column=0, padx=5)
entry_apartamento = tb.Entry(frame_update, width=10)
entry_apartamento.grid(row=0, column=1, padx=5)

tb.Label(frame_update, text="Residentes:").grid(row=0, column=2, padx=5)
entry_residentes = tb.Entry(frame_update, width=10)
entry_residentes.grid(row=0, column=3, padx=5)

tb.Button(
    frame_update, text="Atualizar", bootstyle="info", command=atualizar_residentes
).grid(row=0, column=4, padx=5)

frame_bottom = tb.Frame(root)
frame_bottom.pack(pady=10)

tb.Button(frame_bottom, text="Sair", bootstyle="danger", command=root.destroy).pack(
    side="right", padx=5
)

root.mainloop()
